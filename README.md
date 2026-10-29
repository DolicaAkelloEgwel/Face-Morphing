# Face Morphing

Create a morphing video between two or more faces.

![Morphed Video](results/output.gif)

## Requirements

- [pixi](https://pixi.prefix.dev/latest/)
- A collection of face images

## Installation

1. Clone the repository.
2. In the repository folder, enter the following command:

```
pixi install
```

You should now be able to use the code.

## Getting Started

### Run with Demo Images

Generate a morphing animation video sequence.

```
pixi run demo
```

This will create a file called output.mp4 that morphs between the demo images.

### Run with Own Images

#### (Optional) Align Images

The program expects input images to all be 1024x1024. You can align them yourself, or run images of any size through the alignment code, which will prepare them for you. To align images of faces, run the following command:

```
pixi run align YOUR_NONALIGNED_IMAGES_INPUT_FOLDER YOUR_ALIGNED_IMAGES_OUTPUT_FOLDER
```

This will look for faces in the input folder - crop out, align (center the nose and make the eyes horizontal), and then rescale the resulting images and save them in the output folder.

#### Run Morphing

When a collection of 1024x1024 face images have been prepared, run the following command:

```
pixi run morph YOUR_INPUT_FOLDER YOUR_OUTPUT_FILENAME.mp4
```

The output video will show the morph sequence.

## Citations

Advice on working with facial landmarks with dlib and opencv: https://www.pyimagesearch.com/2017/04/03/facial-landmarks-dlib-opencv-python/ 
