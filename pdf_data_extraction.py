import pdfplumber
import csv
from PIL import Image
import os
import pytesseract

def extract_data_from_file(file_path):
    file_extension = os.path.splitext(file_path)[1].lower()

    if file_extension == '.pdf':
        return extract_data_from_pdf(file_path)
    elif file_extension in ['.png', '.jpg', '.jpeg']:
        return extract_data_from_image(file_path)
    else:
        raise ValueError('Unsupported file format.')
def extract_data_from_pdf(pdf_file_path):
    with pdfplumber.open(pdf_file_path) as pdf:
        extracted_data = []

        # For Extracting header data
        first_page = pdf.pages[0]
        header_data = first_page.extract_text().split('\n')
        extracted_data.append(header_data)

        # For Extracting  table data
        for page in pdf.pages:
            tables = page.extract_tables()
            for table in tables:
                extracted_data.extend(table)

    return extracted_data

# def save_data_to_csv(data, csv_file_path):
#     with open(csv_file_path, 'w', newline='') as csv_file:
#         writer = csv.writer(csv_file)
#         writer.writerows(data)


def extract_data_from_image(image_file_path):
    extracted_data = []

    # Perform OCR on the image using pytesseract
    image = Image.open(image_file_path)
    text = pytesseract.image_to_string(image)

    # Extract relevant data from the OCR text
    # Add your code to process the OCR text and extract the required information
    # Populate the extracted_data list with the extracted information

    return extracted_data

def save_data_to_csv(data, csv_file_path):
    with open(csv_file_path, 'w', newline='', encoding='utf-8') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerows(data)

if __name__ == '__main__':
    pdf_file_path = 'sample14.pdf'
    csv_file_path = 'sample14.csv'

    extracted_data = extract_data_from_pdf(pdf_file_path)
    save_data_to_csv(extracted_data, csv_file_path)
