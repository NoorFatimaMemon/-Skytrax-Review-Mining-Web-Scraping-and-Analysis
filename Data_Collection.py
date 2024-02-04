from bs4 import BeautifulSoup
import pandas as pd
import requests

# Base URL for British Airways reviews on airlinequality.com
base_url = "https://www.airlinequality.com/airline-reviews/british-airways"
# Number of pages to scrape
pages = 38
# Number of reviews to collect per page
page_size = 100
# List to store all reviews
reviews = []

# Loop through each page to collect reviews
for i in range(1, pages):
    print(f"Scraping page {i}")

    # Create URL for the current page
    url = f"{base_url}/page/{i}/?sortby=post_date%3ADesc&pagesize={page_size}"

    # Make a GET request to the URL
    response = requests.get(url)

    # Parse the HTML content using BeautifulSoup
    content = response.content
    parsed_content = BeautifulSoup(content, 'html.parser')

    # Extract text content from the 'text_content' div class and append to the reviews list
    for para in parsed_content.find_all("div", {"class": "text_content"}):
        reviews.append(para.get_text())

    print(f"---> {len(reviews)} total reviews")

# Create a DataFrame to store the reviews
df = pd.DataFrame()
df["reviews"] = reviews

# Save the DataFrame to a CSV file
df.to_csv("BA_reviews.csv")
