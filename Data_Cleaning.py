from nltk.tokenize import word_tokenize
from textblob import TextBlob
from nltk.corpus import stopwords
import pandas as pd
import json
import re

# Create an empty JSON file to store cleaned review data
with open("D:\Pycharm Project Instructios\Britisis_Airways\Cleaned_Review_Data.json", "w") as outfile:
    outfile.write('[]')
    outfile.close()

# Load the scraped data into a DataFrame
df = pd.read_csv('D:\Pycharm Project Instructios\Britisis_Airways\BA_reviews.csv')
review_list = df.values.tolist()

# Iterate through each review element in the list
for review_element_index, review_element in enumerate(review_list):

    # Extract verification status from the scraped data
    if '|' in review_element[1]:
        verification_status = review_element[1].split('|')[0]
    else:
        verification_status = None
    
    # Extract and clean the review text: remove special characters and convert to lowercase
    if '|' in review_element[1]:
        review_text_1 = re.sub(r'[^a-zA-Z\s]', '', review_element[1].split('|')[1].lower())
    else:
        review_text_1 = re.sub(r'[^a-zA-Z\s]', '', review_element[1].lower()) 
    
    # Handle missing values and create a cleaned review text
    review_text_2 = review_text_1 if pd.notna(review_text_1) else ''
    stop_words = set(stopwords.words('english'))
    review_text_tokens = word_tokenize(review_text_2)
    filtered_review_text = ' '.join([word for word in review_text_tokens if word.lower() not in stop_words])

    # Analyze sentiment of the cleaned review text
    sentiment = TextBlob(filtered_review_text).sentiment.polarity

    # Create a new data entry with cleaned review text, verification status, and sentiment
    new_data = [{"Index": review_element_index, 'CleanedReviewText': filtered_review_text, 
                 'VerificationStatus': verification_status, 'Sentiment': sentiment}]
    
    # Filepath for the cleaned review data JSON file
    filename = "D:\Pycharm Project Instructios\Britisis_Airways\Cleaned_Review_Data.json"
    
    # Open the JSON file and update its content
    with open(filename, 'r+') as file:
        # Load existing data into a dictionary
        file_data = json.load(file)
        # Append new data to existing data
        file_data.append(new_data)
        # Set file's current position at offset
        file.seek(0)
        # Convert the combined data back to JSON format
        json.dump(file_data, file, indent=4)
        file.close() 

# Print a message when the process is finished
print('Data cleaning and sentiment analysis finished')
