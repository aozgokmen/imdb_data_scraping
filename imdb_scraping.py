import requests
from bs4 import BeautifulSoup
import pandas as pd
import re

url = "https://m.imdb.com/chart/top/?ref_=nv_mv_250"

headers = {
    'User-Agent': '',
    'Accept': '',
    'Accept-Language': '',
    'Referer': '',
    'DNT': '',}

response = requests.get(url, headers=headers)

titles = []
ratings = []

if response.status_code == 200:
    print("Successfully fetched the page")
    html = response.content
    soup = BeautifulSoup(html, "html.parser")

    # Adjust these class names based on the current website structure
    product_list = soup.find("ul", {"class": "ipc-metadata-list ipc-metadata-list--dividers-between sc-9d2f6de0-0 iMNUXk compact-list-view ipc-metadata-list--base"})
    if product_list:
        products = product_list.find_all("li", {"class": "ipc-metadata-list-summary-item sc-59b6048d-0 cuaJSp cli-parent"})
        for product in products:
            product_card = product.find_all("div", {"class": "ipc-metadata-list-summary-item__c"})
            for p in product_card:
                a_tag = p.find('a')
                rating = p.find('span', {"class" : "sc-479faa3c-1 iMRvgp"})
                if a_tag:
                    h3_tag = a_tag.find('h3', class_='ipc-title__text')
                    title =h3_tag.get_text(strip=True)
                    modified_title = re.sub(r'\b\d+\.', '', title)
                    titles.append(modified_title)
                       
                if rating:
                    rating_span = rating.find('span', class_='ipc-rating-star ipc-rating-star--base ipc-rating-star--imdb ratingGroup--imdb-rating')
                    rating = rating_span.get_text(strip=True)[0:3]
                    #print(rating)
                    ratings.append(rating)   
    else:
        print("Product list not found")
else:
    print(f"Failed to fetch the page, status code: {response.status_code}")

df = pd.DataFrame({
    'Title': titles,
    'Rating': ratings
})

print(df)