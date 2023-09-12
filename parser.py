import pdfplumber
import json

def pdf_to_text(pdf_path):
    with pdfplumber.open(pdf_path) as pdf:
        text = ''
        for page in pdf.pages:
            text +=page.extract_text()
    return text


def parse_resume(pdf_path):
    text_content = pdf_to_text(pdf_path)
    data = {
        "parsed_text": text_content
    }
    return data

def main():
    pdf_path = 'test.pdf'
    parsed_data = parse_resume(pdf_path)
    with open('output.json', 'w') as json_file:
        json.dump(parsed_data, json_file, indent=4)

if __name__ == '__main__':
    main()