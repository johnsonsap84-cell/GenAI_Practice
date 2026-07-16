import pandas as pd

#load my csv file using pandas in a dataframe
df = pd.read_csv('dataset/nyc_weather.csv')

#printing top 5 row
# print(df.head())

#Accessing specific column
# print(df['EST'])

#Accessing specific cell
# print(df['EST'][0])

#Accessing specific columns
# print(df[['EST', 'VisibilityMiles','Humidity']])

#select the max value of temperature
# print(df['Temperature'].max())

#get all the dates when it raind
# print(df['EST'][df['Events'] == 'Rain'])

#Add new colum to the output table
# df['newTempCol'] = df['Temperature'] + 10
# print(df)

#updating the df

# print(df['WindSpeedMPH'].mean())
# df.fillna(0, inplace=True)
# print(df)
# print(df['WindSpeedMPH'].mean())





