#!/usr/bin/env python
# coding: utf-8

# # Web scrapping

# In[1]:


import requests
from bs4 import BeautifulSoup


# In[2]:


#fetch the webiste
website = requests.get('https://quotes.toscrape.com/')


# In[3]:


# to get website Html
print(website.text)


# In[4]:


#defining object
soup = BeautifulSoup(website.text,'html.parser')


# In[5]:


# to get particular tag
title = soup.find('title')     # parameter is Tag name
print(title)


# In[6]:


print(title.text)


# In[7]:


first_quote=soup.find(class_='text')
print(first_quote.text)


# In[8]:


#to find all the links on website
links=soup.find_all('a')
for link in links:
    print(link)


# In[9]:


#to find all the quotes
quotes=soup.find_all(class_='text')
for quote in quotes:
    print(quote.text)


# In[10]:


# to select child class
quote=soup.find(class_='quote')

quote_text=quote.find(class_='text')

author_of_quote=quote.find(class_='author')
print(quote_text.text)
print(author_of_quote.text)


# In[16]:


#using CSS selector
quote_text=soup.select_one('.text')
all_quote_text=soup.select('.text')
for a in all_quote_text:
    print(a.text)
#print(quote_text.text)


# In[21]:


#scrapping multiple pages


page_no=1
next_button= True
while next_button:
    website = requests.get('https://quotes.toscrape.com/page/'+str(page_no))
    soup=BeautifulSoup(website.text,'html.parser')
    next_button=soup.select_one('.next > a')
    quotes=soup.select('.quote')
    for q in quotes:
        text=q.select_one('.text')
        author=q.select_one('.author')
        tags=q.select('.tag')
        print(text.text)
        print(author.text)
        for t in tags:
            print(t.text,end='    ')
        print('\n')
        print('-----*-----*-----*-----*----*-----')
    
    print('We Scraped page number  '+str(page_no))
    print()
    page_no += 1
    


# In[ ]:




