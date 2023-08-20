import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#Read Data
Mock_Data = pd.read_csv('ExerciseData_combined_csv_user1.csv')
print(Mock_Data.head())

Mock_Data['distance'] = pd.to_numeric(Mock_Data['distance'], errors='coerce')
Mock_Data['calories'] = pd.to_numeric(Mock_Data['calories'], errors='coerce')

Mock_Data['distance'].fillna(method='ffill', inplace=True)
Mock_Data['calories'].fillna(method='bfill', inplace=True)

#Visualising data 
plt.hist(Mock_Data['distance'], bins=20)
plt.xlabel('calories')
plt.ylabel('Frequency')
plt.title('Distance Covered')
plt.show()

plt.hist(Mock_Data['distance'], bins=20)
plt.xlabel('calories')
plt.ylabel('Frequency')
plt.title('Calories Chart')
plt.show()

# Summary Statistics
print(Mock_Data[['distance', 'calories']].describe())

#Histogram
plt.scatter(Mock_Data['distance'], Mock_Data['calories'])
plt.xlabel('Distance')
plt.ylabel('Calories')
plt.title('Distance vs Calories')
plt.show()

#Matrix
correlation_matrix = Mock_Data[['distance', 'calories']].corr()
print(correlation_matrix)

sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm')
plt.title('Correlation Heatmap')
plt.show()

Mock_Data['timestamp'] = pd.to_datetime(Mock_Data['timestamp'])
Mock_Data.set_index('timestamp', inplace=True)

plt.plot(Mock_Data['distance'], label='Distance')
plt.plot(Mock_Data['calories'], label='Calories')
plt.xlabel('Timestamp')
plt.ylabel('Value')
plt.title('Time Series Analysis')
plt.legend()
plt.show()



