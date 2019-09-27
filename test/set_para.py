#!/usr/bin/env python
"""
    This module helps with the tests.
"""
import os
import sys
from PIL import Image, ImageDraw
crtScriptDir = os.path.dirname(sys.argv[0])
root = os.path.abspath(crtScriptDir)

outputPath = os.path.join(root, "output")
outputPath = os.path.abspath(outputPath)

referencePath = os.path.join(root, "reference")
referencePath = os.path.abspath(referencePath)

drawReferencePath = os.path.join(referencePath, "draw")
drawReferencePath = os.path.abspath(drawReferencePath)
drawOutputPath = os.path.join(outputPath, "draw")
drawOutputPath = os.path.abspath(drawOutputPath)

polygonOutputPath = os.path.join(outputPath, "polygon")
polygonOutputPath = os.path.abspath(polygonOutputPath)
polygonReferencePath = os.path.join(referencePath, "polygon")
polygonReferencePath = os.path.abspath(polygonReferencePath)

transformOutputPath = os.path.join(outputPath, "transform")
transformOutputPath = os.path.abspath(transformOutputPath)
transformReferencePath = os.path.join(referencePath, "transform")
transformReferencePath = os.path.abspath(transformReferencePath)
# Result image for draw


def filename(name):

    return name + '.png'


def validate(reference_file, result_file):

    """
    compare results against reference data
    inputs : the path to the reference file, path to resultant file
    returns : True or False
    """
    print(result_file)
    print(reference_file)
    with open(result_file, "rb") as result:
        with open(reference_file, "rb") as reference:
            assert(reference.read() == result.read())


def get_image(imagemode, imagesize, imagebackground):
    """
    This function is to generate an image with a specific background, mode, and size
    inputs: plotting mode, image size in tuple (x,y), background color 'while' for ex.
    returns: image , and canvas objects

    """
    image = Image.new(imagemode, imagesize, imagebackground)
    canvas = ImageDraw.Draw(image)

    return image, canvas


def get_path(image_name):
    """
    This function is to set a path to resultant and reference files
    inputs: path to (drawing, polygon, transform) folder, path to (drawing, polygon, transform, depends on
     from which test is being called ) reference folder, image name!
    outputs: full path to resultant, and reference files.
    """

    if image_name.find('draw') != -1:

        result_file = os.path.join(drawOutputPath, image_name)
        reference_file = os.path.join(drawReferencePath, image_name)

    elif image_name.find('Polygon') != -1:

        result_file = os.path.join(polygonOutputPath, image_name)
        reference_file = os.path.join(polygonReferencePath, image_name)

    elif image_name.find('transform') != -1:

        result_file = os.path.join(transformOutputPath, image_name)
        reference_file = os.path.join(transformReferencePath, image_name)

    return result_file, reference_file
