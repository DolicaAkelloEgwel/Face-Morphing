# Face Morphing

Create a morphing video between two or more faces.

![Morphed Video](results/output.gif)

## Requirements

This code assumes all input images are 1024x1024. You may crop them yourself, or use the alignment code to do this for you. The code requires [pixi](https://pixi.prefix.dev/latest/) to run.

## Installation

1. Clone the repository.
2. In the repository folder, enter the following command:

```
pixi install
```

You should now be able to use the code.

## Getting Started

### Test with Demo Images

Generate a morphing animation video sequence.

```
pixi run python code/__init__.py --images demo-images --output output.mp4
```

### Test with Own Images

1. Prepare a folder of images

2. Auto align faces with `pixi run python code/utils/align_images.py nonaligned/images/path aligned/images/path --output_size=1024`  
This will look for faces in your input folder - crop out, align (center the nose and make the eyes horizontal), and then rescale the resulting images and save them in "aligned_images" folder.

3. Run `pixi run python code/__init__.py --images input/images/path --output output-video-filename.mp4`.

## Citations

Advice on working with facial landmarks with dlib and opencv: https://www.pyimagesearch.com/2017/04/03/facial-landmarks-dlib-opencv-python/ 
