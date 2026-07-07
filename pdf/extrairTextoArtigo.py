#Extrair texto de artigo
#Lib principal: pip install pypdf

import re
import sys
from pypdf import PdfReader

def main():
    if len(sys.argv) != 2:
        print("Error. Run: $ python3 extrairTextArtigo.py <arquivo>")
        sys.exit(1)

    pathFile = sys.argv[1]

    stringTarget = "Abstract"

    reader = PdfReader(pathFile)
    numPages = len(reader.pages)

    finalText = ""

    with open("textArticle.txt", "w", encoding="utf-8") as file:
        for i in range(1, numPages):
            currentPage = reader.pages[i]
            currentText = currentPage.extract_text()

            if currentText and currentText.strip():
                if stringTarget in currentText:
                    cutText = currentText.split(stringTarget, 1)[0]
                    finalText += cutText
                    break
                else:
                    finalText += currentText
            else:
                print(f"Can't extract text from {i}")                

        finalText = re.sub(r'\s+\d+\s+\.', '.', finalText)
        file.write(finalText)

    file.close()
if __name__ == "__main__":
    main()
