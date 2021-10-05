""" This is a simple dictionary created using 
python re and requests library"""

from icecream import ic

import requests   #importing the two libraries
import re

payload = {'page':1, 'count':25}
word = input("Enter the word to search: ") #user input
url = f'https://www.dictionary.com/browse/{word}' # the user input is formatted into the url
print(url)
response = requests.get(url, params=payload).text #i request the data to be printed in a text form

""" searching for the location of the information (defition) in the response"""
data = re.search('meta name="description" content=', response)
start = data.end()  # the end of the content=' marks the beginning of the definition
end = start + 300   #added this few spaces to cover for the end of the definition

data1 = (response[start:end]) #from here, data1 is giving us the definition and some unnecessary info
m = re.search(">", data1) #so we have to scrap it out

""" so this section will grab data1 and remove any unnecessary details from (">") in the previous section"""
start = 0
end = m.end()-1 
data2 = (data1[start:end])
ic(data2)
