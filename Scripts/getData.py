import csv
import os
import re
from urllib.parse import urlparse
from bs4 import BeautifulSoup
import requests


# gets the home link of the website
def get_home_link(product_link):
    parsed_url = urlparse(product_link)
    home_link = parsed_url.scheme + "://" + parsed_url.netloc
    return home_link


def get_text_content():
    # create a file to save the working links
    working_links = open("working_links.txt", 'a')
    data_dir = "C:/Users/Laurentiu/PycharmProjects/FurnitureStoresExtraction/Data"
    with open("furniture_stores_pages.csv", 'r') as file:
        reader = csv.reader(file)
        # number of the file to save the text content
        x = 1
        # for every url in the csv file
        for row in reader:
            try:
                url = row[0]
                # get the response and verify if the link is working
                # then save the working links to a file
                response = requests.get(url)
                if response.status_code != 200:
                    continue
                working_links.write(url + "\n")
                # get the text content of the page, clean it and save it to a file
                soup = BeautifulSoup(response.text, 'html.parser')
                body_text = soup.find('main')
                text_content = body_text.get_text()
                # remove empty lines, tabs and spaces
                cleaned_text = re.sub(r'\n\s*', '\n', text_content.strip(), flags=re.M)
                file_text_content = open(os.path.join(data_dir, f"text_content_{x}.txt"), 'w')
                file_text_content.write(cleaned_text)
                x += 1
                file_text_content.close()
            except Exception as e:
                print(e)
                continue
    working_links.close()

