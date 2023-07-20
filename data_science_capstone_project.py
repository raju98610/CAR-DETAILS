# -*- coding: utf-8 -*-
"""Data Science Capstone Project.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1ZqTdhWD_sGLgkFusUUk4U7REESAGD8xl

***Importing the Dependencies***
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

"""***Data Collection and Processing***"""

# loading the data from csv file to pandas dataframe
df = pd.read_csv('CAR DETAILS.csv')
# inspecting the first 5 rows of the dataframe
df.head()  # top 5 rows

"""***Handling null values***"""

# View the shape and info of the dataset
row, col = df.shape
print('Row = ', row, 'Col = ', col)

df.info()

# Split the column name to get the model of the car
df["model"] = df.name.apply(lambda x : ' '.join(x.split(' ')[:1]))
df['model'].value_counts()

# Check null values in dataset
df.isnull().sum()

# Check duplicated row in dataset
df[df.duplicated()]

# Drop all duplicated row
df = df.drop_duplicates()

df.shape

# View unique values from categorical features
categorical = [col for col in df.columns if df[col].dtypes == 'O']

for col in categorical:
  print(df[col].unique())

# Summary of the data set
df.describe()

"""***Exploratory Data Analysis***"""

car = df.copy()

"""***Model Distribution***"""

car["model"].value_counts().index

def percent(ax):
    heightlst = []
    for i in ax.patches:
        heightlst.append(i.get_height())
    total = sum(heightlst)

    for i in ax.patches:
        x = i.get_x()+0.2
        height = i.get_height()+4.3
        value = ("{0:.2f}".format((i.get_height()/total)*100)+'%')

        ax.text(x, height, value, fontsize=14,color='black')

# Plot of Car Models Distribution
figure = plt.figure(figsize=(12,8))
plt.title('Car Models Distribution', fontsize=18)
plot = sns.countplot(x="model", data=car, order = car['model'].value_counts().index[:5], palette='Blues_r')
percent(plot)

plt.show()

"""***Categorical Summary***"""

def categorical_summarized(dataframe, x=None, y=None, hue=None, palette='Blues_r', verbose=True):
    '''
    Helper function that gives a quick summary of a given column of categorical data
    Arguments
    =========
    dataframe: pandas dataframe
    x: str. horizontal axis to plot the labels of categorical data, y would be the count
    y: str. vertical axis to plot the labels of categorical data, x would be the count
    hue: str. if you want to compare it another variable (usually the target variable)
    palette: array-like. Colour of the plot
    Returns
    =======
    Quick Stats of the data and also the count plot
    '''
    if x == None:
        column_interested = y
    else:
        column_interested = x
    series = dataframe[column_interested]
    print(series.describe())
    print('mode: ', series.mode())
    if verbose:
        print('='*80)
        print(series.value_counts())

    sns.countplot(x=x, y=y, hue=hue, data=dataframe, palette=palette)
    plt.show()

categorical_summarized(car, x='fuel')

categorical_summarized(car, x='seller_type')

categorical_summarized(car, x='transmission')

categorical_summarized(car, x='owner')

# Subplot of Categorical Summary
plt.figure(figsize=(18,8))

plt.subplot(2,2,1)
plt.title('Fuel Summary', fontsize=18)
sns.countplot(data=car, x='fuel', palette='Blues_r')
plt.xlabel('')
plt.subplot(2,2,2)
plt.title('Transmission Summary', fontsize=18)
sns.countplot(data=car, x='transmission', palette='Blues_r')
plt.xlabel('')
plt.subplot(2,2,3)
plt.title('Owner Summary', fontsize=18)
sns.countplot(data=car, x='owner', palette='Blues_r')
plt.xlabel('')
plt.subplot(2,2,4)
plt.title('Seller Type Summary', fontsize=18)
sns.countplot(data=car, x='seller_type', palette='Blues_r')
plt.xlabel('')

plt.tight_layout()
plt.show()

"""Based on the plot above, if we look at the Fuel from cars with the Diesel type, it has the same amount as the Transmission Manual, First Owner Car, and Individual Seller.

***Correlation Matrix***
"""

plt.figure(figsize=(10,10))
plt.title('Correlation Matrix', fontsize=18)
sns.heatmap(car.corr(), cbar=True, annot=True, cmap='Blues')

"""Based on the Correlation Matrix above, it provides information that if there is a new car, the selling price will be high, and if the car is the latest, the KM Driven will be low.

Correlation Between selling_price and km_driven
"""

plt.figure(figsize=(18,8))
plt.title('km_driven by selling_price Distribution', fontsize=18)
sns.scatterplot(data=car, x='km_driven', y='selling_price')

plt.ticklabel_format(style='plain', axis='y')

"""The plot above provides information that on Car Dekho, Cars have a Selling Price below 2,000,000 with KM Driven conditions below 100,000 KM.

Correlation Between selling_price and year
"""

plt.figure(figsize=(18,8))
plt.title('year by selling_price Distribution', fontsize=18)
sns.scatterplot(data=car, x='year', y='selling_price')

plt.ticklabel_format(style='plain', axis='y')

"""The plot above provides information if the distribution of selling prices for cars in Car Dekho is the highest between 2016-2019.

How does year affects km_driven?
"""

plt.figure(figsize=(12,10))
plt.title('year by km_driven Distribution', fontsize=18)
sns.histplot(data=car, x='year', y='km_driven', bins=100)
#plt.ticklabel_format(style='plain', axis='x')

"""The plot above provides information that on Car Dekho, most cars are still under 100,000 KM and the best car choices are in cars with years between 2017-2019 because the number of KM tends to be small and the number of units is large.

Detailed Analysis in selling_price, km_driven, year
"""

pd.pivot_table(data=car, index=['name'], values=['selling_price','km_driven','year']).sort_values(by='selling_price', ascending=False)

pd.pivot_table(data=car, index=['name'], values=['selling_price','km_driven','year']).sort_values(by='km_driven', ascending=False)

pd.pivot_table(data=car, index=['name'], values=['selling_price','km_driven','year']).sort_values(by='year', ascending=False)

"""The Audi RS7 2015-2019 Sportback Performance is the car model with the highest selling price, reaching 8,900,000 with a relatively small number of KM. In contrast, the Ford Icon 1.6 ZXI NXt is a car model with the lowest selling price of 20,000 but has a fairly high KM Driven, reaching 25,000 KM because it was purchased in 2005.

Chevrolet Tavera Neo LS B3 - 7(C) seats BSIII is the car model with the highest KM Driven, reaching 350,000 KM with a selling price of 280,000 purchased in 2010. On the other hand, the Ford Figo Titanium is the car model with the lowest KM Driven with 606 KM with a selling price of 690,500 purchased in 2020.

***How does Categorical Feature affects selling_price***
"""

plt.figure(figsize=(24,16))

plt.subplot(2,2,1)
plt.title('Fuel by selling_price Distribution', fontsize=18)
sns.boxplot(data=car, x='selling_price', y='fuel', palette='Set2')
plt.ticklabel_format(style='plain', axis='x')
plt.subplot(2,2,2)
plt.title('Transmission by selling_price Distribution', fontsize=18)
sns.boxplot(data=car, x='selling_price', y='transmission', palette='Set2')
plt.ticklabel_format(style='plain', axis='x')
plt.subplot(2,2,3)
plt.title('Owner by selling_price Distribution', fontsize=18)
sns.boxplot(data=car, x='selling_price', y='owner', palette='Set2')
plt.ticklabel_format(style='plain', axis='x')
plt.subplot(2,2,4)
plt.title('Seller_type by selling_price Distribution', fontsize=18)
sns.boxplot(data=car, x='selling_price', y='seller_type', palette='Set2')
plt.ticklabel_format(style='plain', axis='x')

"""In the Car Dekho dataset, Cars with the Diesel Fuel type have more influence on Selling Prices, just like the Transmission Automatic type which has more influence on Selling prices than Manual, First Owner also has a high influence on Selling Prices, and Seller Type Dealer also has a high influence on Selling Price.

Conclusion


1. The Maruti model car has higher units in the Car Dekho dataset after Hyundai and Mahindra.
2. Fuel from cars with the Diesel type has a higher amount, the same as Manual Transmissions, First Owner Cars, and Individual Sellers.
3. IF there is a new car, the selling price will be high, and if the car is the latest, the KM Driven will be low.
4. Look for a quality car by looking at the number of KM Driven cars and the year the car was purchased. You also need to know the Owner Type and Seller Type because both of them can affect the Selling Price apart from KM Driven and Year.
"""

import os

import statsmodels.api as sm

pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)

pd.reset_option('display.float_format')
pd.options.display.float_format = '{:.5f}'.format

f, ax = plt.subplots(figsize=(10, 5))

ax.ticklabel_format(style='plain', axis='both')

sns.boxenplot(car.km_driven, ax=ax).set_title('KM Driven')

plt.show()

car=car[car.km_driven<400000]

f, ax = plt.subplots(figsize=(10, 8))

ax.ticklabel_format(style='plain', axis='both')

sns.boxenplot(data= car, x='selling_price', y='model', ax=ax).set_title('Sales Price by model')

plt.show()

car.model.value_counts()

"""**if number of records per manufacturer is 1 then 'Rest'**"""

cars_rest_filter=car.model.value_counts()[car.model.value_counts()==1].index.to_list()

car.loc[(car.model.isin(cars_rest_filter)), 'model']='Rest'
car.loc[~(car.model.isin(cars_rest_filter)), 'model']=car['model']

pd.concat([car.model.value_counts(),
               pd.Series(car.model.value_counts(), index=['Rest'])]).plot.bar(rot=90)
plt.title('Number of Cars per Model')
plt.show()

for i in car.model.unique():
    sns.lmplot(x='km_driven', y='selling_price',data=car[(car.model==i)], hue='model' )
    plt.ticklabel_format(style='plain', axis='y')

"""***Resgression***"""

car=car.join(pd.get_dummies(car.fuel))

car=car.join(pd.get_dummies(car.seller_type))

car=car.join(pd.get_dummies(car.transmission))

car=car.join(pd.get_dummies(car.owner))

car=car.join(pd.get_dummies(car.model))

y=car.selling_price

car.head().T

X=car.drop(['name','selling_price', 'fuel', 'seller_type', 'transmission', 'owner', 'model','model' ],  axis=1)

X = sm.add_constant(X)

model = sm.OLS(y, X)
results = model.fit()
print(results.summary())

"""***Conclusion***

[1] Standard Errors assume that the covariance matrix of the errors is correctly specified.

[2] The smallest eigenvalue is 1.87e-19. This might indicate that there are

strong multicollinearity problems or that the design matrix is singular.
"""



"""**SAVING THE TRAINED MODEL**"""

import pickle

filename = 'trained_model.sav'
pickle.dump(model,open(filename,'wb'))

#loading the save model
loaded_model=pickle.load(open('trained_model.sav','rb'))

!pip install streamlit

!pip install joblib

! pip install streamlit

!pip install ngrok

# Load dataset
df = pd.read_csv('CAR DETAILS.csv')

import streamlit as st
import pandas as pd
!pip install joblib

import joblib
import pickle


# Load dataset
df = pd.read_csv('CAR DETAILS.csv')
# Load the trained model
loaded_model=pickle.load(open('trained_model.sav','rb'))

def filter_cars_by_company(selected_model, df):
    sorted_df = df.sort_values(['car.model', 'name'], ascending=True)
    filtered_cars = sorted_df[sorted_df['car.model'] == selected_company]['name'].unique()
    return filtered_cars


# Create the web app
def main():
    # Set the title and description
    st.title('Car details')
    st.write('Enter the details of the car to predict its price.')

    # Get user inputs


    year = st.number_input('Year', min_value=1900, step=1)
    km_driven = st.number_input('Kilometers Driven',step=1000)
    fuel = st.selectbox('Fuel Type', ['Petrol', 'Diesel', 'CNG', 'LPG', 'Electric'])
    seller_type = st.selectbox('Seller Type',['Individual', 'Dealer', 'Trustmark Dealer'])
    transmission = st.selectbox('Transmission', ['Manual', 'Automatic'])
    owner = st.selectbox('Owner',['First Owner', 'Second Owner','Third Owner','Fourth & Above Owner','Test Drive Car'])


    data = pd.DataFrame({
                            'year': year,
                            'km_driven': km_driven,
                            'fuel': fuel,
                            'seller_type': seller_type,
                            'transmission': transmission,
                            'owner': owner}, index=[0])

    if st.button('Predict Price'):
        # Make predictions
        predictions = model.predict(data)
        predicted_price = "{:.2f}".format(predictions[0])
        st.success(f'Price of the car is {predicted_price} INR')


# Run the web app
if __name__ == '__main__':
    main()