from bs4 import BeautifulSoup
import requests

def main():
    for i in range(1, 51):
        url = f'http://books.toscrape.com/catalogue/page-{i}.html'

        response = requests.get(url)
        if response.status_code == 200:
            print(f'Resquest {i} succefull. Link: {url}')
        else:
            print(f'Error on request {i}')
            exit()

        html = response.text

        soup = BeautifulSoup(html, 'html.parser')

        all_h3 = soup.find_all('h3')

        with open('dados3_s2.txt', 'a+') as file1:
            file1.write(f'Books on page {i}:\n')
            for h3 in all_h3:
                all_a = h3.find('a')
                file1.writelines(f'{all_a['title']}\n')

            file1.write(f'Total: {len(all_h3)}\n\n\n')

    file1.close()

if __name__ == '__main__':
    main()
    print('Done')