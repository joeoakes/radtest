import bs4
import urllib.request
import ssl
import json
import requests
from Zoro import Zoro
from os.path import exists

# --- ignore ssl certificate ---
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE





master_list = []
def get_products(productIDs):
    if len(productIDs) == 0:
        print("page results not scrapable")
        return
    base_url = "https://www.zoro.com/product/?products="
    query = ",".join(productIDs)
    url = base_url + query
    payload = {}
    headers = {
        'authority': 'www.zoro.com',
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'en-US,en;q=0.9',
# removed 'cookies' and 'referer'
        'sec-ch-ua': '"Chromium";v="106", "Google Chrome";v="106", "Not;A=Brand";v="99"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"macOS"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36'
    }
    print("making request")
    response = requests.request("GET", url, headers=headers, data=payload)
    print(response)
    items = json.loads(response.content)

    for i in items["products"]:
        master_list.append(i)

class Scraper:
    def __init__(self):
        self.config = Zoro()

        self.page = 1
        self.pagesToScrape = 1
        self.results = []

        self.IDs = []

    def start_scrape(self):
        while self.page <= self.pagesToScrape:
            full_link = self.config.getFullURL() + str(self.page)
            self.get_page_results(full_link)
            self.page+=1

    def get_page_results(self, url):
        IDs = []
        content = urllib.request.urlopen(url, context=ctx).read()  # Get page content
        full_soup = bs4.BeautifulSoup(content, 'html.parser')  # Parse page content
        all_results = full_soup.findAll(self.config.cardTags[0], self.config.cardTags[1])

        for i in all_results:
            IDs.append(i["gtm-data-productid"])
        get_products(IDs)





s = Scraper()
searchFor = input("enter search terms: ")
s.pagesToScrape = int(input("how many pages would you like to scrape? "))
s.config.search_terms = searchFor.split(" ")
print(s.config.search_terms)
s.start_scrape()
print("total products scraped: ", len(master_list))
with open("results.txt", "w") as file:
    file.write(json.dumps(master_list, indent=2))