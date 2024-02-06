# -*- coding: utf-8 -*-
"""Web_scrapping_sindu.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Dvhz2J3f1QeDmGvjxpgarUMzH6iWfGmg
"""

#Import the libraries

import requests
from bs4 import BeautifulSoup as bs

#Get the response of the URL

url='https://books.toscrape.com/'
response=requests.get(url)
response

# Get the status code of the URL

response.status_code

# Know the typr of the response

type(response)

# Print the response by converting it to the Text form.

print(response.text[:100])

# Again check for the type of the response.

type(response.text)

#Soup the response using BeautifulSoup "bs"

soup=bs(response.text)
type(soup)

#Find the title of the webpage using "find()" method and "title" parameter.

soup.find('title').text.strip()

#get the code of each book which is in "article" tag with class as "product_pod"

book_tag=soup.find_all('article',class_='product_pod')

#Print the data retrieved above

book_tag

# check the length of the "book_tag" that represents "Number of books retreived in that page."

len(book_tag)

# get the details of the first book.

book=book_tag[0]
book

#To get the link,Book Name whic are in "a" tag using find function where title is True.

title_tag=book.find('a',title=True)
title_tag

#Title_tag is converted into next or the text in the retreived data is printed.

title_tag.text

# the hyperlink of the title_tag is retreived from the title_tag

title_tag['href']

#retreive the title in the title_tag

title_tag['title']

# To get the price of the book in "p" tag with class as "price_color"

price=book.find('p','price_color')
price.text

#retreive the price from the "p" tag in "class" wher ethe element is in second line.

price=book.find('p')['class'][1]
price

# Take empty lists--------href[Hyperlinks], titles[Title of the book], ratings[rating of the book], prices[Price of the book]


href=[]
titles=[]
ratings=[]
prices=[]

# Run a for loop with length of the "book_tag" and append the title,price,hyperlink,rating in respective lists.

for i in range(len(book_tag)):
  book=book_tag[i]
  title_tag=book.find('a',title=True)
  href.append(title_tag['href'])
  titles.append(title_tag['title'])
  ratings.append(book.find('p')['class'][1])
  price=book.find('p','price_color')
  prices.append(price.text[1:])

#Import pandas

import pandas as pd

# Create a dataframe using the four lists--

web_data=pd.DataFrame({'Title':titles,'Rating':ratings,'Price':prices,'Href':href})

#print the above dataframe.

web_data

"""# Method-**2**"""

# Create a function for each book_tag title,hyper links,ratings,prices naming as "book_info" and return the price,title,rating and hyperlink.

def book_info(book_tag):

  title_tag=book_tag.find('a',title=True)
  href=(title_tag['href'])
  titles=(title_tag['title'])
  ratings=(book_tag.find('p')['class'][1])
  price=book_tag.find('p','price_color')
  prices=(price.text[1:])
  return titles,ratings,prices,href

# create a function called "get_url" to check the response of the website.

def get_url(url):
  response = requests.get(url)

  if response.status_code == 200:
    titles=bs(response.text)
    return titles
  else:
    print(f"Failed to retrieve page {url}. Status code: {response.status_code}")
    return None

# Create a function to soup the response of each website and extract the information from each website.


def get_books(url):
  soup=get_url(url)
  book_tags=soup.find_all('article',class_='product_pod')
  books=[]
  for i in book_tags:
    books.append(book_info(i))
  return books

# Enetr the url and call get_books function in which the remaining functions are called for response and books extraction.

url='https://books.toscrape.com/'
books=get_books(url)
len(books)

# Display first three books of the books list.

books[:3]