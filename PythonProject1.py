import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

data = pd.read_csv('/Users/sithiasma/Downloads/Womens Clothing E-Commerce Reviews.csv')
data.head()

sns.countplot(x='Rating', data=data)
plt.xlabel('Rating')
plt.ylabel('Count')
plt.title('Distribution of Ratings')
plt.show()

sns.boxplot(x='Rating', y='Age', data=data)
plt.xlabel('Rating')
plt.ylabel('Age')
plt.title('Relationship between Age and Ratings')
plt.show()

 
sns.barplot(x='Department Name', y='Positive Feedback Count', data=data, errorbar=None)
plt.xlabel('Department Name')
plt.ylabel('Positive Feedback Count')
plt.title('Positive Feedback Count by Department Name')
plt.show()

division_counts = data.groupby('Division Name')['Positive Feedback Count'].sum()
plt.pie(division_counts, labels=division_counts.index, autopct='%1.1f%%', startangle=140)
plt.title('Performance of Division based on Positive Feedback Count')
plt.axis('equal') 
plt.show()


common_complaints = data[data['Rating'] <= 3][['Rating', 'Title']]
common_complaints.to_csv('common_complaints.csv', index=False, mode='w')

