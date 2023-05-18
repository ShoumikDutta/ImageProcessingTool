# Image Processing Tool

This is a Python script that processes images by applying a shirt overlay on them. The script takes two command-line arguments: the input file path and the output file path. It performs the following steps:

1. Checks if the correct number of command-line arguments is provided. If there are too few or too many arguments, it exits with an appropriate error message.

2. Extracts the input file format and output file format from the command-line arguments. It ensures that the input and output formats have the same extension and are either PNG, JPG, or JPEG. If the formats are invalid or different, the script exits with an appropriate error message.

3. Opens the shirt image file called "shirt.png".

4. Retrieves the size of the shirt image.

5. Opens the input image file specified in the command-line argument and resizes it to fit the size of the shirt image using the `ImageOps.fit()` function from the Pillow library.

6. Pastes the shirt image on top of the resized input image using the `paste()` method.

7. Saves the modified image to the output file path specified in the command-line argument. The `Save_all=True` parameter ensures that the entire image is saved, including all frames if the image is an animated GIF.

If the input file is not found, the script exits.

## Requirements

- Python 3.x
- Pillow library (install using `pip install Pillow`)

## Usage

Run the script from the command line with the following format:

```
python image_processing_tool.py <input_file> <output_file>
```

Replace `<input_file>` with the path to your input image file and `<output_file>` with the desired path to save the processed image.

Ensure that the input and output file extensions are the same and supported formats (PNG, JPG, or JPEG). The script will exit with an error message if the formats are invalid or different.

## Example

```
python image_processing_tool.py input.jpg output.jpg
```

This example runs the script to process an input image called "input.jpg" and saves the output image as "output.jpg" in the same directory.

## Limitations

- The script assumes that the shirt image is named "shirt.png" and located in the same directory as the script. Make sure to provide the correct shirt image if it's located elsewhere.
- The script overwrites the output file if it already exists. Make sure to provide a unique output file path to avoid unintentional data loss.
- The script only supports PNG, JPG, and JPEG image formats for both input and output files. Other formats are not supported.
