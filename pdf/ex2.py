#Exercício 2 - extrair texto
from pypdf import PdfReader

reader = PdfReader("/home/isaac/Documents/Livros/Computacao/swebok-v4.pdf")

page = reader.pages[100]
text = page.extract_text()

print(text)

if text and text.strip():
    print("PDF tem texto extratível")
else:
    print("PDF talvez seja escaneado")
