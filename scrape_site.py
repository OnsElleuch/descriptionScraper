import requests
from bs4 import BeautifulSoup


def extract(url, page= None):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36'}
    if(page != None):
        url= url.format(page=page)
    r = requests.get(url, headers)
    soup = BeautifulSoup(r.content, 'html.parser')
    return soup

def transform(soup : BeautifulSoup):
    divs = soup.find_all('div', class_="card-list__item")
    soups = []
    for item in divs:
        title = item.find('a', href=True)
        href = ("https://www.propertyfinder.ae"+ title['href'])
        detail_soup= extract(href)
        print("new item added")
        soups.append(detail_soup)
    return soups
     
def extract_details(soups):
    for item in soups:
        try: 
            property_type = item.find_all('div', class_="property-facts__content")[0].text.strip().replace('\n', '')
            property_size = item.find_all('div', class_="property-facts__content")[1].text.strip().replace('\n', '')
            bedrooms = item.find_all('div', class_="property-facts__content")[2].text.strip().replace('\n', '')
            bathrooms = item.find_all('div', class_="property-facts__content")[3].text.strip().replace('\n', '')
            amenities = item.find_all('div', class_="property-amenities__list")
        except:
            property_type = ''
            property_size = ''
            bedrooms = ''
            bathrooms = ''
            amenities = ''

        '''amenities_dict = {}
        for amenity in amenities:
            amenities_dict[amenity]=True'''
        description = item.find('div', class_="property-description__text-trim").text.strip().replace('\n', ' ')
        listing = {
            'type' : property_type,
            'size' : property_size,
            'bedrooms' : bedrooms,
            'bathrooms' : bathrooms,
            'description' : description
        }
        #### listing = listing | amenities_dict
        listings.append(listing)
    return
        

listings = []
