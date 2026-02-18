import requests
from bs4 import BeautifulSoup
import json

def saveJson(fileName, dataToSave):
    try:
        with open(fileName, "w") as json_file:
            json.dump(dataToSave, json_file, indent=4)
        print(f"Data saved in: {fileName}")
    except IOError as e:
        print(f"Error on saving: {e}")

def main():
    url = "https://dummit.cos.northeastern.edu/handouts"
    fileNameJson = "dados_s1.json"

    response = requests.get(url)

    if response.status_code == 200:
        with open("dados1_s1.txt", "w") as file1:
            file1.write(response.text)
    else:
        print(f"Error {response.status_code}")

    html = response.text

    soup = BeautifulSoup(html, "html.parser")

    bold_text = [b.text.strip() for b in soup.find_all("b")]
    links = [a.text.strip() for a in soup.find_all("a")]
    list_items = [li.text.strip() for li in soup.find_all("li")]

    dados = {
        "boldTextCount": len(bold_text),
        "linksCount": len(links),
        "listItemsCount": len(list_items),
        "bold_text": bold_text,
        "links": links,
        "list_items": list_items
    }

    saveJson(fileNameJson, dados)

if __name__ == "__main__":
    main()
    print()