from bs4 import BeautifulSoup
import requests

def main():
    url = "http://books.toscrape.com/"

    response = requests.get(url)

    if response.status_code == 200:
        with open("dados_s2.txt", "w") as file1:
            file1.write(response.text)
        print(f"Data saved in {file1}")
    else:
        print("Error on saving")

if __name__ == "__main__":
    main()
    print()