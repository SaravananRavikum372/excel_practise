from PIL import Image
import pytesseract

# Specify the path to the Tesseract executable
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# Load the image and perform OCR
image_path = r'C:\path\to\your\image.jpg'
text = pytesseract.image_to_string(Image.open(image_path))

# Print the extracted text
print("Extracted Text:")
print(text)

