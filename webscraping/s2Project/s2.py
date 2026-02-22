from bs4 import BeautifulSoup
import requests

def main():
    url = "http://books.toscrape.com/"

    response = requests.get(url)

    html = response.text

    soup = BeautifulSoup(html, 'html.parser')

    all_h3 = soup.find_all("h3")

    with open("dados2_s2.txt", "w") as file1:
        for h3 in all_h3:
            all_a = h3.find("a")
            file1.write(f"Title: {all_a["title"]}\n")

    print(f"h3: {len(all_h3)}")

    file1.close()

if __name__ == "__main__":
    main()
    print()