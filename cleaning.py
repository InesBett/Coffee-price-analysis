from bs4 import BeautifulSoup
import pandas as pd
import requests
import warnings
warnings.filterwarnings('ignore') 

url= "https://cafely.com/blogs/research/which-country-consumes-the-most-coffee?srsltid=AfmBOooy1znaM-b_BvIsZhMLRjZFvsDTyNMtxBeU8Hzi6Y08RJHfbDP5"

response= requests.get(url)

soup= BeautifulSoup(response.text, "html.parser")

html_table = soup.find_all("table", {"id":"full-data-table"})[0]

df= pd.read_html(html_table.prettify())[0]
df

df.columns= ["Drop", "country", "continent", "consumption_kg", "yearly_coffee_consumption_pcapita_kg", "daily_cofee_consumption_pcapita_cup", "coffe_drinking_year", "lifetime_cup_consumption_cup", "price_per_cup", "total_lifetime_coffee_spending"]

df["price_per_cup"]= df["price_per_cup"].str.replace("$", " ")
df["total_lifetime_coffee_spending"]= df["total_lifetime_coffee_spending"].str.replace("$", " ")
df["total_lifetime_coffee_spending"]= df["total_lifetime_coffee_spending"].str.replace(",", ".")

df["price_per_cup"]= df["price_per_cup"].astype(float)
df["total_lifetime_coffee_spending"]= df["total_lifetime_coffee_spending"].astype(float)

df= df.drop(columns="Drop")

df_2= pd.read_csv("coffee_dataset.csv", delimiter= ";")
df_2.columns= ["Categories", "Country", "2020", "2021", "2022", "2023", "2024", "2025","Avg_price_per_cup"]

df_2= df_2.dropna()

df_2.columns= [col.lower().replace(" ", "") for col in df_2.columns]

df_2["avg_price_per_cup"]= df_2["avg_price_per_cup"].str.replace("$", " ")

df_2["country"] = df_2["country"].str.strip().replace("Algeria                                         2,240                 2,090                 2,050                 1,950                 1,950             2,050", "Algeria")

df_2["country"]= df_2["country"].str.strip().replace("Siuth Korea", "South Korea")

df_2["country"]= df_2["country"].str.strip().replace("UK","United Kingdom")

df_2["country"]= df_2["country"].str.strip().replace("USA","United States")

df_2["country"]= df_2["country"].str.strip().replace("Philipines", "Philippines")

df_2["country"]= df_2["country"].str.strip().replace("EU", "European Union")

df_2["country"]= df_2["country"].str.strip().replace("Vietnma", "Vietnam")

df.to_csv("df_consumption_finall.csv", index=False)
df_2.to_csv("producers.csv", index= False)
