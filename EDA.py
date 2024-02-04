import matplotlib.pyplot as plt
import json

# Load the JSON data
with open("Cleaned_Review_Data.json") as json_file:
    json_data = json.load(json_file)

Positive = []
Negative = []
Neutral = []

# Analyze and categorize sentiment for each review

for data in json_data:
    for review in data:
        sentiment_score = review["Sentiment"]*100
        if sentiment_score > 10:
            Positive.append(sentiment_score)
        elif sentiment_score >= 0 and sentiment_score <= 10:
            Neutral.append(sentiment_score)
        else:
            Negative.append(sentiment_score)


# Data for the pie chart
labels = ['Positive', 'Negative', 'Neutral']
sizes = [len(Positive), len(Negative), len(Neutral)]

print("Review Analysis")
print("Total Count of Positive: ", len(Positive))
print("Total Count of Negative: ", len(Negative))
print("Total Count of Neutral: ", len(Neutral))
print("Total Reviews: ", len(Positive)+len(Neutral)+len(Neutral))

colors = ['green', 'gray', 'orange']
explode = (0.1, 0, 0)  # explode the 1st slice (Positive) for emphasis

# Plotting the pie chart
plt.pie(sizes, explode=explode, labels=labels, colors=colors, autopct='%1.1f%%', shadow=True, startangle=140)
plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

# Display the pie chart
plt.title('Sentiment Distribution')
plt.show()
