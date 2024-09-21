Organize Your Image Files:

Place all the image files you want to convert into a single PDF in a directory of your choice.
Supported image formats: JPEG, JPG, and PNG.

Update Script Variables:

Open the Python script (image_to_pdf.py) in a text editor.
Locate the following variables at the beginning of the script:
initial_location: Set this to the path of the directory containing your image files.
destination: Specify the desired output PDF file path (including the filename and extension, e.g., "E:\\img_out.pdf").

Run the Script:

Open a terminal or command prompt.
Navigate to the directory where your script is located.
Execute the script using the following command:
python image_to_pdf.py

Check the Output:

The script will process the eligible image files and create a single PDF file.
If no eligible images are found, it won't create an empty pdf
