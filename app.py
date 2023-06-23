from flask import Flask, render_template, request
import os
import pdfplumber
import csv

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        file = request.files['file']
        if file:
            file_path = os.path.join(app.root_path, 'uploads', 'sample14.pdf')
            file.save(file_path)
            extracted_data = extract_data_from_pdf(file_path)
            csv_file_path = os.path.join(app.root_path, 'uploads', 'sample14.csv')
            save_data_to_csv(extracted_data, csv_file_path)
            return render_template('result.html', data=extracted_data)
    return render_template('index.html')

def extract_data_from_pdf(pdf_file_path):
    with pdfplumber.open(pdf_file_path) as pdf:
        extracted_data = []

        first_page = pdf.pages[0]
        header_data = first_page.extract_text().split('\n')
        extracted_data.append(header_data)

        for page in pdf.pages:
            tables = page.extract_tables()
            for table in tables:
                extracted_data.extend(table)

    return extracted_data

# def save_data_to_csv(data, csv_file_path):
#     with open(csv_file_path, 'w', newline='') as csv_file:
#         writer = csv.writer(csv_file)
#         writer.writerows(data)


def save_data_to_csv(data, csv_file_path):
    with open(csv_file_path, 'w', newline='', encoding='utf-8') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerows(data)
if __name__ == '__main__':
    app.run(debug=True)


