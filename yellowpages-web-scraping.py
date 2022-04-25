import requests
from bs4 import BeautifulSoup
import pandas as pd

url = 'https://www.yellowpages.com/new-york-ny/car-insurance'
page = requests.get(url)

soup = BeautifulSoup(page.content,'html.parser')

#gets all tags with class info
divInfo = soup.find_all(class_='info')

#lists
businessNameList = []
categoryList = []
ratingList = []
linkList = []
phoneList=[]

# Create a Pandas Excel writer using XlsxWriter as the engine.
writer = pd.ExcelWriter('demo1.xlsx', engine='xlsxwriter')

print('Web scrapped started....')
#iterate through all div tags with class info
for tag in divInfo:
    #get contents needed for scraping
    business_name = tag.find(class_='business-name')
    categories = tag.find(class_='categories')
    ratings = tag.find(class_='ratings')
    links = tag.find(class_='links')
    phone = tag.find(class_='phone')

    #insert and add contents to respecive lists
    businessNameList.append(business_name.text)
    categoryList.append(categories.find('a').text)
    ratingList.append('N/A')
    linkList.append(links.a.get('href'))
    phoneList.append(phone.text)


# dataframe Name and Age columns
df = pd.DataFrame({
    'Business Name': businessNameList,
    'Category': categoryList,
    'Ratings': ratingList,
    'Links': linkList,
    'Phone': phoneList,
}) 

# Convert the dataframe to an XlsxWriter Excel object.
df.to_excel(writer, sheet_name='Sheet1', index=False)

# Close the Pandas Excel writer and output the Excel file.
writer.save()
print('Web scrapped successfully.')

    
