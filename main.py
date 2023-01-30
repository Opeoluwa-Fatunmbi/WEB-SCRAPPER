import requests
from bs4 import BeautifulSoup
import csv

# The URL to scrape
url = "https://www.example.com"

# Send a request to the URL and get the response
response = requests.get(url)

# Parse the HTML content of the page
soup = BeautifulSoup(response.content, "html.parser")

# Find the data to scrape
data = soup.find_all("div", class_="data-item")

# Store the data in a list
data_list = []
for item in data:
    item_data = item.text.strip()
    data_list.append(item_data)

# Write the data to a CSV file
with open("data.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Data"])
    for item in data_list:
        writer.writerow([item])
