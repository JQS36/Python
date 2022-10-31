import requests
from bs4 import BeautifulSoup

if __name__ == "__main__":
    asin = "B0B16656Z2"
    url = f"https://www.amazon.com/dp/{asin}"
    headers = {
        "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36"
    }
    result = requests.get(url, headers=headers)
    doc = BeautifulSoup(result.content, "lxml")

    with open(f"./asins/{asin}.txt", 'w', encoding='utf-8') as html:
        html.write(str(doc))