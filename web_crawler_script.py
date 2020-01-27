'''
THIS IS A WEB CRAWLER(SPIDER-FLIPKART)
'''

from bs4 import BeautifulSoup
import requests



def spider(max_pages):
    page = 1
    while page <= max_pages:
        print("<" * 10, page, ">" * 10)
        url = "https://www.flipkart.com/search?q=redmi+note+8+phone&sid=tyy%2C4io&as=on&as-show=on&otracker=AS_QueryStore_OrganicAutoSuggest_0_18_na_na_na&otracker1=AS_" \
              "QueryStore_OrganicAutoSuggest_0_18_na_na_na&as-pos=0&as-type=HISTORY&suggestionId=redmi+note+8+phone%7CM" \
              "obiles&requestId=0d6464f5-cd8f-4d8f-b881-470855bdb433&page=" + str(page)
        source_code = requests.get(url)
        plain_text = source_code.text
        soup = BeautifulSoup(plain_text , features="html.parser")
        for a_tag in soup.findAll("a" , {"class" : "_31qSD5"}):
            href = a_tag.get("href")
            link = "https://www.flipkart.com" + href
            spider_page(link)
        page += 1

def spider_page(link):
    source_code = requests.get(link)
    plain_text = source_code.text
    soup = BeautifulSoup(plain_text, features="html.parser")
    for name_tag in soup.findAll("span" , {"class" : "_35KyD6"}):
        print(name_tag.text)
    for price_tag in soup.findAll("div" , {"class" : "_1vC4OE _3qQ9m1"}):
        print(price_tag.string)



spider(2)