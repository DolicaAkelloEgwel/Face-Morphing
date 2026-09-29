import argparse
import os
import shutil
from subprocess import PIPE, Popen

import cv2
from delaunay_triangulation import make_delaunay
from face_landmark_detection import generate_face_correspondences
from face_morph import generate_morph_sequence


def doMorphing(images, duration, frame_rate, output):

    p = Popen(
        [
            "ffmpeg",
            "-y",
            "-f",
            "image2pipe",
            "-r",
            str(frame_rate),
            "-s",
            str(1204) + "x" + str(1024),
            "-i",
            "-",
            "-c:v",
            "libx264",
            "-crf",
            "25",
            "-vf",
            "scale=trunc(iw/2)*2:trunc(ih/2)*2",
            "-pix_fmt",
            "yuv420p",
            output,
        ],
        stdin=PIPE,
    )

    for i in range(len(images) - 1):

        img1 = images[i]
        img2 = images[i + 1]

        [size, img1, img2, points1, points2, list3] = generate_face_correspondences(
            img1, img2
        )

        tri = make_delaunay(size[1], size[0], list3, img1, img2)

        imgs = generate_morph_sequence(
            duration, frame_rate, img1, img2, points1, points2, tri, size, output
        )
        for img in imgs:
            img.save(p.stdin, "JPEG")


def read_images_in_folder(images_folder: str) -> list:
    images = []
    for filename in os.listdir(images_folder):
        img = cv2.imread(os.path.join(images_folder, filename))
        if img is not None:
            images.append(img)

    if len(images) <= 1:
        # make sure nothing happens here
        exit()
    return images


if __name__ == "__main__":

    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--images", required=True, help="The location of the images folder"
    )
    parser.add_argument("--duration", type=int, default=5, help="The duration")
    parser.add_argument("--frame", type=int, default=20, help="The frameame Rate")
    parser.add_argument("--output", required=True, help="Output Video Path")
    args = parser.parse_args()

    images = read_images_in_folder(args.images)

    doMorphing(images, args.duration, args.frame, args.output)
