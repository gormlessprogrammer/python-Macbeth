"""Created so Pylint shuts the fuck up."""
import requests
from bs4 import BeautifulSoup
from nltk.tokenize import word_tokenize

#Scraping Macbeth, here's the URL
URL = 'http://shakespeare.mit.edu/macbeth/full.html'

# Grabbing HTML from website
response = requests.get(URL, verify=False)
 
 # Parsing text w. beautifulsoup
soup = BeautifulSoup(response.text, 'html.parser')

# Extracting text from the HTML
text = soup.get_text().lower()

# Break up the text into invdidual words 
words = word_tokenize(text)

# Count the occurance of the Word Macbeth
count = len([word for word in words if 'macbeth' in word])

# Creating loop to print occurances
occurance = 0
for i, word in enumerate(words):
    if 'macbeth' in word:
        occurance += 1

print(f"{occurance}")