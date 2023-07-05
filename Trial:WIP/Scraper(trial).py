#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 26 11:25:36 2023

@author: shadow
"""

import requests
from bs4 import BeautifulSoup
import csv


def scrape_sephora_perfumes():
    url = 'https://www.sephora.com/shop/perfume'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36'
    }
    
    # Send HTTP GET request and retrieve the HTML content
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.content, 'html.parser')
    
    # Extract perfume data from HTML
    perfumes = soup.find_all('div', {'class': 'css-1qe8tjm'})
    
    # Store the extracted data in a CSV file
    with open('sephora_perfumes.csv', 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['Name', 'Brand', 'Price'])
        
        for perfume in perfumes:
            if perfume.find('span', {'class': 'ProductTile-name css-h8cc3p eanm77i0'}):
                name = perfume.find('span', {'class': 'ProductTile-name css-h8cc3p eanm77i0'}).text.strip() 
            else: name = None
            if perfume.find('span', {'class': 'css-12z2u5 eanm77i0'}):
                brand = perfume.find('span', {'class': 'css-12z2u5 eanm77i0'}).text.strip()
            else: brand = None
            if perfume.find('span', {'class': 'css-0'}):
                price = perfume.find('span', {'class': 'css-0'}).text.strip()
            else: price = None
            
            writer.writerow([name, brand, price])
            print([name,brand,price])
        
    print("Scraped")
    

# Run the scraper
scrape_sephora_perfumes()