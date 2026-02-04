import requests
from bs4 import BeautifulSoup

url = "https://dummit.cos.northeastern.edu/handouts"

response = requests.get(url)

if response.status_code == 200:
    with open("dados1_s1.txt", "w") as file1:
        file1.write(response.text)
else:
    print(f"Error {response.status_code}")

html = response.text

soup = BeautifulSoup(html, "html.parser")

bs = soup.find_all("b")
count = 0
for b in bs:
    print(b.text)
    count += 1

print(f"{count}\n\n")

links = soup.find_all("a")
count = 0
for link in links:
    print(link.text)
    count += 1

print(f"{count}\n\n")