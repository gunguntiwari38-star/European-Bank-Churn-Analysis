import pandas as pd
df = pd.read_csv("European_Bank.csv")
print(df.head())
print(df.info())
print(df.isnull().sum())
df.drop_duplicates(inplace=True)
df.drop(['CustomerId', 'Surname'],axis=1,inplace=True, errors='ignore')
print(df.info())
df.to_csv("C:/Users/tiwari/Downloads/Processed_Bank_Data.csv",index=False)
print("Processed dataset exported successfully")
import streamlit as st
st.title("My First Streamlit App")
st.write("Hello World!")

