from scrape_site import extract, extract_details, transform, listings
import time
import pandas as pd

def main():
    url ='https://www.propertyfinder.ae/en/buy/properties-for-sale.html?c=1&ob=mr&page={page}'
    for page in range(1,300):
        c= (extract(url, page))
        soups= (transform(c))
        extract_details(soups)
        print('for sale page ', page)
        time.sleep(5)
    url ='https://www.propertyfinder.ae/en/rent/properties-for-rent.html?c=2&fu=0&ob=mr&page={page}'
    for page in range(1,300):
        c= (extract(url, page))
        soups= (transform(c))
        extract_details(soups)
        print('for rent page ',page)
        time.sleep(5)
    df = pd.DataFrame(listings)
    df.to_csv('listings.csv')
    print('Done')

main()