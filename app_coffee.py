import streamlit as st
import matplotlib as plt
import pandas as pd
import seaborn as sns

# Title Design
st.markdown("""
    <style>
    .title {
        font-size: 52px;
        font-family: 'Verdana', sans-serif;
        font-weight: bold;
        color: #FAE3C6; /* Creamy coffee tone */
        text-align: center;
        background: linear-gradient(90deg, #3D2B1F, #B07B53); /* Espresso & caramel blend */
        padding: 20px;
        border-radius: 15px;
        box-shadow: 5px 5px 20px rgba(0, 0, 0, 0.5);
        letter-spacing: 2px;
        text-transform: uppercase;
    }
    </style>
    <div class="title">☕ Coffee Across the Globe: A Data-Driven Brew 🌍</div>
""", unsafe_allow_html=True)



tab1, tab2, tab3, tab4, tab5 = st.tabs(["Overview","Producers", "Consumers", "Hypothesis & Correlation","Sentiment Analysis"])

# Content for Overview tab
with tab1:
    st.header("☕ The Story of Coffee: From Bean to Cup")
    st.write("Coffee is more than just a beverage—it’s a global phenomenon that has shaped cultures, fueled economies, and connected people across centuries." 
             "From the first discovery of coffee beans in Ethiopia to the bustling cafés of Europe and the rise of specialty coffee worldwide, this drink has become an essential part of daily life for millions.But coffee is also a business, one that spans continents, from the tropical farms of Latin America, Africa, and Asia to the bustling cities where it is brewed and consumed. Behind every cup, there is a complex system of production, trade, and consumption—each with its own economic, social, and environmental implications.")
    st.header("📊 About This Project")

    st.write("This analysis aims to uncover key insights about the coffee industry, focusing on two major questions:")

    st.write("")  # Adds an empty line

    st.write(
    "1️⃣ Who produces the most coffee, and does high production affect local prices?\n\n"
    "2️⃣ Which countries are the biggest consumers, and what influences their coffee prices?\n\n"
    "By examining data on production, consumption, and pricing, this project seeks to reveal the hidden dynamics of the coffee market. "
    "Are coffee-producing countries benefiting from their own production, or do international markets dictate the price? "
    "And what makes some countries pay significantly more for their daily cup?\n\n"
    "Through interactive visualizations and in-depth analysis, this project provides a comprehensive look at the fascinating world of coffee. "
    "Grab a cup, and let’s explore! 🚀"
    )

# Content for Producers tab
with tab2:
    st.header("🌍 Coffee Production: Who Grows the World's Coffee?")

    st.write(
    "Coffee is one of the most traded commodities in the world, with millions of farmers depending on it for their livelihoods. "
    "But where does most of our coffee come from? Let's explore the leading coffee-producing nations and the factors that influence production."
    )
    st.write("")
    st.subheader("☕ Top Coffee Producers")

# Description
    st.write(
    "The global coffee industry is dominated by a few key players. The **top coffee-producing countries** are responsible for the majority of the world's supply. "
    "Brazil, Vietnam, and Colombia lead the market, producing vast quantities of coffee beans that fuel global demand."
    )

# Load the dataset
    df_production = pd.read_csv("producers.csv")

# Select categorical and numerical columns
    categorical = df_production.select_dtypes(exclude="number")
    numerical= df_production.select_dtypes(include="number")

# Create frequency table
    frequency_table_country = categorical.country.value_counts().reset_index()
    frequency_table_country.columns = ['country', 'absolute_frequency']

# Filter out unnecessary values
    frequency_table_country = frequency_table_country[
    ~frequency_table_country['country'].isin(["Other", "Total"])
    ]

# Create proportion table
    proportion_table_country = categorical.country.value_counts(normalize=True).round(2).reset_index()
    proportion_table_country.columns = ['country', 'proportion']

# Remove "Other" and "Total"
    proportion_table_country = proportion_table_country[
    ~proportion_table_country['country'].isin(["Other", "Total"])
    ]

# Merge both tables
    country_table = pd.concat([frequency_table_country, proportion_table_country], axis=1)
    country_table.columns = ['country', 'absolute_frequency', 'country_2', 'relative_frequency']
    country_table.drop(columns="country_2", inplace=True)

# Select top 10 producers
    top_10_country = country_table.sort_values(by="absolute_frequency", ascending=False).head(10)

# Display the DataFrame
    st.dataframe(top_10_country)

# Create a Seaborn barplot
    fig, ax = plt.subplots(figsize=(10, 5))
    sns.barplot(x="country", y="absolute_frequency", data=top_10_country, palette="copper", ax=ax)
    ax.set_title("Top 10 Coffee-Producing Countries")
    ax.set_xticklabels(ax.get_xticklabels(), rotation=45, ha="right")

# Display the plot in Streamlit
    st.pyplot(fig)

    st.write("China, Indonesia, and Vietnam top the list, each representing 5% of the data, highlighting their significant roles in the coffee industry.Brazil and Colombia, two of the largest coffee producers, have slightly lower frequencies but still remain prominent in the dataset.A variety of countries are involved in coffee, with significant representation from Mexico, India, European Union, Ethiopia, and United States.Smaller countries such as Australia, Cote d'Ivoire, Saudi Arabia, and others have minimal representation, suggesting a smaller, role in the global coffee market.The dataset also includes countries with emerging or smaller roles in coffee like Kazakhstan, Turkey, and Venezuela.")

#Evolution

    st.write("")
    st.subheader(" 📉 Coffee Production: Evolution (2020-2025)")
    st.write("In this section, we’ll explore how coffee production has evolved over the years. From the early days of cultivation to the present, the global coffee market has witnessed significant shifts. We'll dive into the trends that have shaped production volumes, highlighting the key factors driving changes in the coffee industry. Let’s look at how global dynamics and regional changes have influenced coffee supply over time.")

    year_means = numerical[["2020", "2021", "2022", "2023", "2024", "2025"]].mean()

# Create the figure
    fig_2, ax = plt.subplots(figsize=(10, 5))  # Define fig_2 properly
    sns.lineplot(x=year_means.index, y=year_means.values, marker='o', color='#6F4F37', linewidth=2, ax=ax)

# Set plot title and labels
    ax.set_title("Yearly Evolution of Mean Values", fontsize=14)
    ax.set_xlabel("Year", fontsize=12)
    ax.set_ylabel("Value", fontsize=12)
    ax.grid(True)

# Display the plot in Streamlit
    st.pyplot(fig_2)  # Pass the figure object

    st.write(
    """
    The **sharp decline from 2020 to 2022** suggests that coffee production, or related metrics, faced significant challenges during this period.  
    This could be attributed to the **global impact of the COVID-19 pandemic**, which disrupted several key aspects of the coffee supply chain:  

    - **Labor Shortages**: Lockdowns and travel restrictions reduced the availability of farm labor in major coffee-producing countries like **Brazil, Colombia, and Ethiopia**, where harvesting heavily relies on manual work.  
    - **Logistics Disruptions**: Shipping delays, increased storage costs, and reduced market accessibility made it difficult for small-scale producers to export coffee.  
    - **Decline in Consumption**: With cafes and restaurants closed during lockdowns, **out-of-home coffee consumption dropped significantly**.  
    - **Financial Struggles**: Rising production costs and financial challenges further hindered production capacity.  

    From **2022 onward, a strong recovery is observed**, peaking in **2024**, likely due to a return to stability in the coffee industry.  
    However, a **slight decline in 2025** might be due to **limited available data**, as the figures for this year only include early data.  
    """
)


# Content for Consumers tab
with tab3:
    st.header("Top Coffee Consumers")
    st.write("This section covers the countries that consume the most coffee or have the highest coffee prices.")
    
    # Load the dataset
    df_consumption= pd.read_csv("df_consumption_finall.csv")

# Select categorical and numerical columns
    cat = df_consumption.select_dtypes(exclude="number")
    num= df_consumption.select_dtypes(include="number")

# Create frequency table
    freq_table_country= cat.country.value_counts().reset_index()
    freq_table_country.columns= ["country", "absolute_frequency"]


# Create proportion table
    prop_table_country= cat.country.value_counts(normalize=True).reset_index()
    prop_table_country.columns= ["country", "relative_frequency"]

# Merge both tables
    country_consumption_table= pd.concat([freq_table_country, prop_table_country], axis=1)
    country_consumption_table.columns= ["country", "absolute_frequency","country_2","relative_frequency"]
    country_consumption_table.drop(columns="country_2", inplace=True)

# Select top 10 producers
    country_avg_price_consumption = df_consumption.groupby('country')['price_per_cup'].mean().sort_values(ascending=False).head(10)

# Display the DataFrame
    st.dataframe(country_avg_price_consumption)

# Create figure
    fig_3 = plt.figure(figsize=(10, 6))

# Create bar plot
    sns.barplot(x=country_avg_price_consumption.index, y=country_avg_price_consumption.values, palette='copper')

# Set title and labels
    plt.title('Top 10 Highest Coffee Price per Country - Consumers', fontsize=14)
    plt.xlabel('Country', fontsize=12)
    plt.ylabel('Average Price Per Cup of Coffee', fontsize=12)
    plt.xticks(rotation=45)

# Display the plot in Streamlit
    st.pyplot(fig_3)

    st.subheader("☕ The World's Most Expensive Coffee")

    st.write(
    "The bar chart highlights the top 10 countries with the highest average price per cup of coffee."
    )

    st.markdown("#### 🌍 Key Insights")

    st.write("- **Denmark** tops the list, with coffee prices exceeding **$5 per cup**.")
    st.write("- **Switzerland** and the **United States** follow closely, both averaging above **$4.50 per cup**.")

    st.markdown("#### 🌎 Regional Insights")

    st.write(
    "- **European Dominance**: The most expensive coffee markets are in **Europe**, including "
    "**Denmark, Switzerland, Norway, Finland, Sweden, and Luxembourg**."
    )
    st.write(
    "- **Economic & Lifestyle Factors**: High prices in countries like Denmark and Switzerland "
    "may be influenced by **high living costs, taxation, and a premium coffee culture**."
    )
    st.write(
    "- **Beyond Europe**: **Saudi Arabia** and **South Korea** also rank among the top 10, "
    "highlighting strong coffee consumption despite traditionally being tea-drinking cultures."
    )

    st.write(
    "This data provides valuable insights into how **economics, culture, and regional preferences** "
    "shape global coffee pricing. ☕🌎"
    )

# Content for Hypothesis and Correlation
with tab4:
    st.subheader("🔬 Correlation & Hypothesis Testing: Coffee Consumption & Pricing")  
    st.write(  
        "To better understand the global coffee market, we analyze the relationship between **coffee consumption** and **price per cup** using correlation analysis. "
        "Additionally, we test a key economic hypothesis about whether coffee-producing countries benefit from lower coffee prices compared to non-producing nations. ☕📊"  
        "\n\n"
        "### 🔗 Correlation Analysis:\n"
        "We investigate whether higher coffee consumption is associated with lower or higher coffee prices worldwide. "
        "Does greater demand drive prices up, or do economies of scale in high-consumption regions keep costs low?\n\n"
    )

    fig_4= sns.lmplot(data=df_consumption,
            x='consumption_kg',
            y='price_per_cup')
    plt.show()
    st.pyplot(fig_4)

    import streamlit as st

# Pearson Correlation
    st.write("""Pearson Correlation (0.13): 
    The Pearson correlation of 0.13 suggests a **very weak positive linear relationship** between coffee consumption and price per cup.
    - In some cases, higher consumption may be slightly associated with higher prices.
    """)

# Spearman Correlation
    st.write("""Spearman Correlation (-0.01): 
    The Spearman correlation of -0.01 reveals that there is **no monotonic relationship** between the two variables.
    - This indicates that, overall, there isn’t a consistent pattern between coffee consumption and price.
    """)

# Discrepancy Explanation
    st.write("""Discrepancy Between Pearson and Spearman: 
    The difference in results suggests that while both variables may occasionally increase together, the overall trend is weak.
    """)

# Other Influencing Factors
    st.write("""Other Influencing Factors:
    Several other factors could be affecting coffee prices more than consumption levels:
    - Regional price variations
    - Local market conditions
    - Supply chain influences
    """)

# Further Analysis
    st.write(""" Further Analysis:
    To gain deeper insights, consider segmenting the data by:
    - Country
    - Income levels
    - Production costs
    """)


    st.write(
        "### 📊 Hypothesis Testing:\n"
        "We conduct a one-tailed **t-test** to evaluate the following hypothesis:\n"
        "- **H₀ (Null Hypothesis):** The average price per cup of coffee in producing countries is **greater than or equal** to the price in non-producing countries.\n"
        "- **H₁ (Alternative Hypothesis):** The average price per cup of coffee in producing countries is **less than** in non-producing countries.\n\n"

        "By applying statistical techniques, we aim to determine if coffee-producing nations truly enjoy lower prices, "
        "or if international markets and economic factors level the playing field. Let’s explore the results! 🚀"
        )

    st.write("""
    - **Test Statistic (t):** -0.39
    - **P-Value:** 0.3485

    **Conclusion:** Fail to reject the null hypothesis (H₀). There's not enough evidence to claim that coffee is cheaper in producing countries.
""")

# Summary
    st.subheader("Summary of Findings")
    st.write("""
    Since the p-value is greater than 0.05, we fail to reject the null hypothesis (H₀). This suggests that there isn't enough evidence to say that coffee is cheaper in coffee-producing countries compared to non-producing countries.

    The **negative t-statistic** (-0.39) suggests that coffee prices might be slightly lower in producing countries, but the difference is minimal. The **p-value of 0.3485** indicates a high probability that the observed result could have occurred by chance, rather than being a true effect of the coffee production status on prices.

    **Why this happens:**
    - Many coffee-producing countries, especially those with high-quality beans like Brazil and Colombia, export a significant portion of their coffee, which can drive up domestic prices due to export demand.
    - Non-producing countries may have higher import taxes, but their efficient supply chains or subsidies could stabilize or lower prices.
    - Local factors such as transportation costs and varying demand can influence prices in producing countries, especially in remote areas.
    - Non-producing countries like Luxembourg and Finland may have a mix of budget and premium coffee options, balancing out average prices. Additionally, wealthier populations in these countries may be willing to pay more for specialty coffee, affecting overall pricing.
    """)    

# Content for Sentiment Analysis tab
with tab5:
    st.header("People's Thoughts")
    st.write("This section highlights customer opinions on the balance between coffee pricing and quality, offering insights into what consumers think about the value they receive for the price.")
    
    import nltk

    data = pd.read_csv("coffee_form.csv")
    data.drop(columns="Carimbo de data/hora", inplace= True)
    data.columns=["coffee_price_feedback", "coffee_quality_feedback", "price_influenced_by_production", "coffee_preference", "additional_thoughts", "overall_score"]
    data.dropna(inplace= True)
    data.drop(columns= ["price_influenced_by_production", "coffee_preference", "additional_thoughts"], inplace= True)

    nltk.download('vader_lexicon')
    from nltk.sentiment import SentimentIntensityAnalyzer
    vd = SentimentIntensityAnalyzer()

    coffee_price_feedback= data["coffee_price_feedback"]
    text_scores = {}
    vader_df_price = pd.DataFrame()

    for _, row in data.iterrows():
        text = row["coffee_price_feedback"]
        polarity = vd.polarity_scores(text)
        vd_df = pd.DataFrame([polarity])
        vader_df_price = pd.concat([vader_df_price, vd_df], ignore_index=True)

    from wordcloud import WordCloud
    sentiment_counts = {
    "Positive": (vader_df_price["compound"] > 0).sum(),
    "Neutral": (vader_df_price["compound"] == 0).sum(),
    "Negative": (vader_df_price["compound"] < 0).sum(),
}

    fig_6= plt.figure(figsize=(6, 4))
    plt.bar(sentiment_counts.keys(), sentiment_counts.values(), color=["#77DD77", "#FFDD75", "#FF6961"])
    plt.title("Sentiment Distribution of Coffee Pricing Feedback")
    plt.ylabel("Number of Responses")
    plt.show()

    st.pyplot(fig_6)

    text = " ".join(data["coffee_price_feedback"])
    wordcloud = WordCloud(width=800, height=400, background_color="white").generate(text)

    fig_7= plt.figure(figsize=(8, 4))
    plt.imshow(wordcloud, interpolation="bilinear")
    plt.axis("off")
    plt.title("Word Cloud of Coffee Price Feedback")
    plt.show()

    st.pyplot(fig_7)


# Header
    st.title("Word Frequency Analysis of Coffee Sentiment")

# Dominant Concerns
    st.subheader("Dominant Concerns")
    st.write("""
    - The word **"Expensive"** is the largest, indicating that many respondents find coffee costly.
    - **"Cheaper"** also stands out, suggesting a desire for more affordable coffee options.
    - The word **"Buy"** highlights that purchasing decisions are significantly influenced by price.
    """)

# Mixed Perceptions
    st.subheader("Mixed Perceptions")
    st.write("""
    - Some users mention **"affordable"** and **"value"**, implying that while some perceive coffee as expensive, others believe it offers good value for money.
    - Positive words like **"Great"** and **"happy"** indicate that a portion of customers have a favorable view of their coffee experience.
    """)

# Negative Indicators
    st.subheader("Negative Indicators")
    st.write("""
    - Words like **"Dont"** and **"poor"** may point to dissatisfaction, possibly related to pricing or quality concerns.
    - **"Wallet"** suggests that respondents are mindful of how coffee prices impact their budget.
    """)

    text_scores_quality = {}
    vader_df_quality = pd.DataFrame()

    for _, row in data.iterrows():
        text = row["coffee_quality_feedback"]
        polarity = vd.polarity_scores(text)
        vd_df = pd.DataFrame([polarity])
        vader_df_quality= pd.concat([vader_df_quality, vd_df], ignore_index=True)

    sentiment_counts_quality = {
    "Positive": (vader_df_quality["compound"] > 0).sum(),
    "Neutral": (vader_df_quality["compound"] == 0).sum(),
    "Negative": (vader_df_quality["compound"] < 0).sum(),
}

    fig_9= plt.figure(figsize=(6, 4))
    plt.bar(sentiment_counts_quality.keys(), sentiment_counts_quality.values(), color=["#77DD77", "#FFDD75", "#FF6961"])
    plt.title("Sentiment Distribution of Coffee Feedback")
    plt.ylabel("Number of Responses")
    plt.show()

    st.pyplot(fig_9)

    text = " ".join(data["coffee_quality_feedback"])
    wordcloud = WordCloud(width=800, height=400, background_color="white").generate(text)

    fig_10= plt.figure(figsize=(8, 4))
    plt.imshow(wordcloud, interpolation="bilinear")
    plt.axis("off")
    plt.title("Word Cloud of Coffee Quality Feedback")
    plt.show()

    st.pyplot(fig_10)


# Header
    st.title("Coffee Sentiment Analysis - Word Cloud Insights")

# Prominent Words
    st.subheader("Prominent Words")
    st.write("""
    - The most prominent word is **"coffee"**, which is expected given the context.
    - Other large words include **"quality," "expensive," "Netherlands," "flavour," "used,"** and **"great."**
    """)

# Positive Sentiment
    st.subheader("Positive Sentiment")
    st.write("""
    - Words like **"great," "love," "good," "strong," "luxury,"** and **"flavour"** suggest that some consumers appreciate the coffee quality.
    """)

# Negative Sentiment
    st.subheader("Negative Sentiment")
    st.write("""
    - Words such as **"expensive," "lacks," "sad," "bit,"** and **"watery"** indicate concerns about pricing and possible dissatisfaction with taste or quality.
    """)

# Netherlands Focus
    st.subheader("Focus on the Netherlands")
    st.write("""
    - The word **"Netherlands"** is quite prominent, suggesting that many reviews or feedback are related to coffee experiences in the Netherlands.
    """)

# Coffee Characteristics
    st.subheader("Coffee Characteristics")
    st.write("""
    - Words like **"taste," "beans," "drink,"** and **"cappuccino"** highlight a focus on flavor, types of coffee, and consumption preferences.
    """)

# Price Sensitivity
    st.subheader("Price Sensitivity")
    st.write("""
    - The strong presence of **"expensive"** suggests that coffee pricing is a major concern for consumers, particularly in the Netherlands.
    """)

# Quality vs. Cost Trade-off
    st.subheader("Quality vs. Cost Trade-off")
    st.write("""
    - The combination of **"quality"** and **"expensive"** could indicate that while coffee is seen as high-quality, its price may be a potential drawback for some.
    """)

# Consumer Preferences
    st.subheader("Consumer Preferences")
    st.write("""
    - People seem to focus on **flavor**, **strength**, and **type of beans**, which could be valuable for businesses aiming to enhance their product offerings.
    """)

    score_counts = data['overall_score'].value_counts()

    fig_11= plt.figure(figsize=(6, 6))
    plt.pie(score_counts, labels=score_counts.index, autopct='%1.1f%%', startangle=90, colors=["#6F4F37", "#D2691E", "#7B4B3A", "#C49A6C", "#9E7B5A"], wedgeprops={'edgecolor': 'black'})
    plt.title("Distribution of Overall Scores for Coffee Feedback", fontsize=16, fontweight='light', color='brown')
    plt.show()

    st.pyplot(fig_11)

# Header
    st.title("Coffee Rating Summary")

# No 5-Star Ratings
    st.subheader("No One Rated 5 Stars")
    st.write("""
    No respondents rated the coffee 5 stars, suggesting that while the coffee was acceptable or good, there is room for improvement in quality, taste, or overall experience.
    """)

# Majority 4-Star Rating
    st.subheader("Majority Gave a 4-Star Rating (40%)")
    st.write("""
    The most common rating was 4 stars, indicating a strong level of satisfaction but also highlighting small areas for improvement.
    """)

# Significant 2-Star Ratings
    st.subheader("Significant 2-Star Ratings (30%)")
    st.write("""
    A notable portion gave 2 stars, suggesting dissatisfaction with certain aspects such as taste, price, or service. Addressing these concerns could help improve the product or service.
    """)

# 3-Star Ratings (Neutral)
    st.subheader("20% Rated 3 Stars (Neutral)")
    st.write("""
    20% of respondents gave a 3-star rating, indicating neutrality. Minor improvements could sway this group toward higher satisfaction.
    """)

# Lowest Rating (1 Star)
    st.subheader("10% Gave the Lowest Score (1 Star)")
    st.write("""
    A small group of customers gave the lowest rating, indicating very poor experiences. Investigating complaints from this group is important for addressing potential issues.
    """)
