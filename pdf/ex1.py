#Exercício 1 - metadados: número de páginas, título e autor
from pypdf import PdfReader

reader = PdfReader("/home/isaac/Documents/Livros/Computacao/ArtificialIntelligence_3dEdition_HenryWinston.pdf")

numPaginas = len(reader.pages)
print(f"Número de páginas: {numPaginas}")

metadata = reader.metadata
print(f"Metadata: {metadata}")

print("\nTítulo: ", metadata.get("/Title", "Nao informado"))
print("\nAutor: ", metadata.get("/Author", "Nao informado"))
print("\nData de criação: ", metadata.get("/CreationDate", "Nao informado"))
