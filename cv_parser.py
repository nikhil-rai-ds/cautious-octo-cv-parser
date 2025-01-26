import PyPDF2
from docx import Document

doc = Document('CV Nikhil Netcore.docx')
text = '\n'.join([para.text for para in doc.paragraphs])
print(text)
