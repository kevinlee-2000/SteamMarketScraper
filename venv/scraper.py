import requests
from bs4 import BeautifulSoup

###########################################################################
###########################################################################
###########################################################################

'''CHANGE THIS FOR THE NUMBER OF STEAM MARKET PAGES WE WANT TO LOOP THROUGH'''
NUM_PAGES = 100

##########################################################################
###########################################################################
###########################################################################

quantity_arr = []
price_arr = []
for i in range(NUM_PAGES):
    url = "https://steamcommunity.com/market/search?q=#p" + str(i+1) + "_popular_desc"
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')

    quantity_tags = soup.find_all("span", class_="market_listing_num_listings_qty")
    for q_tag in quantity_tags:
        quantity = int(q_tag['data-qty'])
        quantity_arr.append(quantity)

    price_tags = soup.find_all("span", class_="normal_price")
    for p_tag in price_tags:
        try:
            str_price = p_tag.contents[0]
            price = str_price[str_price.find("$"):]
            if price.find(":"):
                price = float(price[1:])
                price_arr.append(price)
        except:
            pass

total_price = 0
total_quantity = 0
for q,p in zip(quantity_arr, price_arr):
    amount = q*p
    total_quantity += q
    total_price += amount

print("total quantity = " + str(total_quantity))
print("total price = " + str(total_price))

