
![Black-Coffee-easy-Recipe](https://github.com/user-attachments/assets/809c9dc0-3591-437a-b6a7-7fa1730b5d56)

# ☕ The Price of a Cup: Does Coffee Production Influence Affordability?


## Project Overview 🎯

Welcome to my final project, a comprehensive analysis of coffee consumption, pricing, and production levels across different countries! This project marks the culmination of my journey in Ironhack's Data Analytics Bootcamp, where I apply the skills and knowledge I've gained to showcase my progress in data analysis, visualization, and storytelling. 

This analysis explores the relationship between coffee producer prices and consumer prices, assessing whether coffee-producing countries (Brazil, Colombia, Ethiopia) have lower retail coffee costs compared to non-producing nations (Luxembourg, Finland). Additionally, it investigates how production levels influence affordability and incorporates sentiment analysis to gain insights into consumer perceptions.


## Exploring the Price Trends among Consumer and Producer Countries 🌎

Coffee is more than just a drink, it’s a global industry shaped by history, culture, and trade. This project delves into coffee production data to uncover trends, insights, and patterns that define the coffee landscape worldwide.

Imagine stepping into a bustling coffee shop, the aroma of freshly brewed espresso filling the air. Beans from Colombia, Ethiopia, and Brazil promise distinct flavors. But how does coffee production vary across regions? This analysis leverages data science to explore these variations and their implications for coffee producers, traders, and consumers alike.


## The Dataset 📊

This analysis is based on two key datasets that provide a comprehensive view of global coffee production and consumption:

**Coffee Production Dataset**: This dataset contains coffee production data (in kilograms) by country from 2020 to 2025. It was sourced from an official PDF report and converted into a structured CSV file for analysis.

Here is breakdown of the contents of the coffee consumption dataset:

*Categories*: Classification of coffee types or production sectors.

*Country*: The name of the country producing coffee.

*2020-2025*: Yearly coffee production figures (in kilograms) for each respective year.

*Avg Price Per Cup (USD)*: The average price of a cup of coffee in each country based on production and market trends.



**Coffee Consumption Dataset**: This dataset was obtained through web scraping and details coffee consumption trends across different countries.

Here is breakdown of the contents of the coffee consumption dataset:

*Country*: The name of the country consuming coffee.

*Continent*: The continent where the country is located.

*Consumption (kg)*: The total amount of coffee consumed in kilograms.

*Yearly Coffee* Consumption Per Capita (kg): The average coffee consumption per person per year in the country.

*Daily Coffee Consumption Per Capita (cups)*: The estimated daily coffee consumption per person in cups.

*Coffee Drinking Years*: The estimated number of years an individual drinks coffee in their lifetime.

*Lifetime Coffee Consumption (cups)*: The estimated total number of coffee cups consumed in a lifetime.

*Price Per Cup (USD)*: The average price of a cup of coffee in the country.

*Total Lifetime Coffee Spending (USD)*: The estimated total amount spent on coffee in a lifetime.

Together, these datasets allow for an in-depth exploration of coffee production, trade, and consumption patterns worldwide.


## Workflow ⚙️

A structured approach was taken to analyze the data effectively:

-- Data Collection: Scraped coffee consumption data and converted production data from a PDF to CSV.

-- Data Cleaning: Standardized columns, handled missing values, and stored the process in a Python script.

Before diving into the analysis, I had to ensure my datasets were clean, consistent, and ready for insights. Just like making a great cup of coffee, data cleaning is all about removing the impurities and refining the details.

Production Dataset – Standardizing for Accuracy 

✔ Dropped missing values to eliminate incomplete records.
✔ Removed unnecessary columns to keep only relevant information.
✔ Checked for duplicates and empty spaces to prevent distortions in analysis.
✔ Standardized country names – For example, some entries listed USA while others had United States of America. To maintain uniformity, I merged them into a single, consistent format.

Consumption Dataset – Making the Data Usable 

This dataset contained symbols and formatting issues that prevented smooth numerical analysis. To clean it, I:
✔ Removed unwanted symbols to convert all relevant variables into numeric format.
✔ Ensured uniformity across all data points for accurate comparison and calculations.

With both datasets properly cleaned and structured, I was ready to move forward with analysis and uncover meaningful insights! 🚀

-- Exploratory Data Analysis (EDA):

    Univariate analysis on df_production: Examining production statistics.

    Univariate analysis on df_consumers: Understanding consumption trends.

-- Bivariate Analysis & Hypothesis Testing:

    Correlation Analysis: Examining relationships between production, consumption, and trade variables.

    Hypothesis Testing: Conducting statistical tests to determine significant associations.

-- Visualization: Creating compelling graphics to highlight trends using Matplotlib, Seaborn and Plotly.

-- Insights & Conclusions: Identifying key takeaways from production patterns and trade dynamics.


## Visualizations 📈

The notebook includes a variety of visualizations to enhance understanding:

  Top 10 Coffee-Producing Countries: A bar chart ranking the leading coffee producers globally.

  Top 10 Coffee-Consuming Countries: A visualization showing which nations consume the most coffee.

  Evolution of Coffee Production (2020-2025): A time-series analysis depicting trends in coffee production over recent years.

  Top 5 Regions of Consumption: A geographical breakdown of the most coffee-thirsty regions worldwide.

  Scatter Plot: showcasing the relationship between price_per_cup and consumption (kg).

  Barplots: Results of sentiment analysis


## Sentiment Analysis 📝

Objective: 

-- Analyze consumer sentiment regarding coffee prices, production, and trends using textual data.

Methodology:

-- Created a google form to gather insights from the public.

-- Processed text using Natural Language Processing (NLP) techniques.

-- Used sentiment analysis models to classify opinions as positive, neutral, or negative.

Findings:

-- Price Sensitivity: Many consumers desire lower prices, suggesting demand for promotions or value-based offerings.

-- Quality Matters: While some are indifferent, a portion of respondents value stronger and more flavorful coffee.

-- Consumer Awareness: Since price and production influence are weakly linked, businesses could educate customers on how sourcing impacts pricing to build a stronger connection.


## SQL Queries 📊

As part of the data analysis process, SQL was used to explore and manipulate the dataset. The SQL file includes:

Data Extraction Techniques: Querying specific subsets of the dataset.

Basic Aggregations & Filtering: Summarizing production and consumption data.

These queries provide a structured approach to extracting meaningful insights and can be used as a reference for further database analysis.


## Streamlite and Tableau

To further enhance the interactivity of the project, I created a Streamlit app that displays the visualizations and allows users to dive deeper into the data. The app integrates real-time SQL queries with the visual insights, offering a seamless exploration experience.

I also created a Tableau dashboard to effectively showcase the key findings in a visually compelling way.


## Final Thoughts ☕

Every cup of coffee carries a story—from the farms where beans are cultivated to the markets where they are traded. This analysis highlights how geography, production capacity, and trade dynamics shape the coffee industry.

Whether you're a coffee enthusiast or a data analyst, these insights provide a deeper appreciation of the complexities behind your daily brew.

This project represents the culmination of my learning journey, where I have applied advanced data analytics techniques to uncover meaningful insights. Through this analysis, I aim to demonstrate not only my technical capabilities but also my ability to tell a compelling data-driven story.

A special thanks to my teachers for their invaluable guidance and support throughout this project and this path. Their insights and encouragement have been instrumental in shaping this analysis.


## Author ✍️

Inês Bettencourt  Data Analyst Bootcamp Student - 2024/2025

Aspiring Data Analyst and coffee enthusiast, blending data storytelling with the rich heritage of coffee cultivation. Special thanks to the data science community for fueling this journey. Cheers to insights and innovation! ☕📊
