from bs4 import BeautifulSoup
import requests

def main():
    url = "http://books.toscrape.com/"

    response = requests.get(url)
    if response.status_code == 200:
        print("URL getting suceeded")
    else:
        print("Error on URL getting")
        exit()

    html = response.text

    soup = BeautifulSoup(html, 'html.parser')

    allTags = soup.find_all()

    allTagNames = [tag.name for tag in allTags]

    uniqueTagNames = list(set(allTagNames))

    with open("allTags_s2.txt", "w") as file1:
        file1.writelines(tag + '\n' for tag in uniqueTagNames)

if __name__ == "__main__":
    main()
    print()