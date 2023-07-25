import os
import PyPDF2

def extract_pages_from_pdf(pdf_path):
    with open(pdf_path, 'rb') as pdf_file:
        pdf_reader = PyPDF2.PdfReader(pdf_file)

        for page_num in range(len(pdf_reader.pages)):
            pdf_writer = PyPDF2.PdfWriter()
            pdf_writer.add_page(pdf_reader.pages[page_num])

            base_name = os.path.splitext(os.path.basename(pdf_path))[0]
            page_filename = f"{base_name}_{page_num+1}.pdf"
            page_path = os.path.join(os.path.dirname(pdf_path), page_filename)

            with open(page_path, 'wb') as page_file:
                pdf_writer.write(page_file)

def main(root_folder):
    for root, dirs, files in os.walk(root_folder):
        for file in files:
            if file.lower().endswith(".pdf"):
                pdf_path = os.path.join(root, file)
                extract_pages_from_pdf(pdf_path)

if __name__ == "__main__":
    root_folder = "CAMINHO PARA A PASTA AQUI"
    main(root_folder)
