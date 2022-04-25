import requests 
from lxml import etree
from bs4 import BeautifulSoup

url = "https://edition.cnn.com/travel/article/macau-style-pork-chop-sandwich-recipe-anthony-bourdain-wellness/index.html"
page = requests.get(url)
# print(page.text)

#get html page contents
soup = BeautifulSoup(page.content, "html.parser")

article_title = soup.find('h1')
#print('Title: \n'+ article_title.text)

#Article title
#<div class='Article__subtitle'>..</div>
article_subtitle = soup.find_all('div',class_='Article__subtitle')

updated_date = article_subtitle[0].text.split('Updated ')[1]
#print('\nUpdated Date: \n'+updated_date)

#Article content
#<div class='Paragraph__component'>..</div>
article_content = soup.find_all(class_ ='Paragraph__component')

r = open("cnn.txt", "w+", encoding='utf-8')
r.write(article_title.text+'\n')

#print('\nArticle Content:')
for div in article_content:
    r.write(div.span.text+'\n')
    #3print(div.span.text)
    
r.close()
print("File Saved as cnn.txt")