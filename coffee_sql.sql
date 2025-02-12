#Queries for consumption data
USE consumption;

#1. Total coffee consumption per continent:
SELECT COUNT(consumption_kg), continent AS consumption_continent
FROM df_consumption_finall
GROUP BY continent;

#2. Top 5 countries with the highest yearly coffee consumption per capita:
SELECT MAX(yearly_coffee_consumption_pcapita_kg), country AS yearly_country
FROM df_consumption_finall
GROUP BY country
ORDER BY yearly_country DESC
LIMIT 5;

#3. Average price per cup of coffee per continent:
SELECT continent, AVG(price_per_cup) AS avg_price_per_cup
FROM df_consumption_finall
GROUP BY continent;

#4. Find countries where daily coffee consumption per capita is above 3 cups:
SELECT country, AVG(daily_cofee_consumption_pcapita_cup) AS avg_daily_cups
FROM df_consumption_finall
GROUP BY country
HAVING avg_daily_cups > 3;

#5. Calculate the total lifetime spending on coffee per continent:
SELECT continent, SUM(total_lifetime_coffee_spending) AS lifetime_spending
FROM df_consumption_finall
GROUP BY continent;

#6. Find the 3 countries with the lowest price per cup of coffee:
SELECT country, price_per_cup AS lowest_price
FROM df_consumption_finall
ORDER BY lowest_price ASC
LIMIT 3;

#7. Top 5 countries with the highest coffee price per cup:
SELECT country, price_per_cup AS highest_price
FROM df_consumption_finall
ORDER BY highest_price DESC
LIMIT 5;

#8. Countries where price per cup higher than 2.5 dollars:
SELECT country, AVG(price_per_cup) AS prices
FROM df_consumption_finall
GROUP BY country
HAVING prices > 2.5
ORDER BY prices ASC;

#9. Countries where lifetime coffee spending is above $50,000:
SELECT country, AVG(total_lifetime_coffee_spending) AS spending
FROM df_consumption_finall
GROUP BY country
HAVING spending > 50.000
ORDER BY spending DESC;

#10 Countries where lifetime coffee spending is less than $50,000:
SELECT country, AVG(total_lifetime_coffee_spending) AS spending
FROM df_consumption_finall
GROUP BY country
HAVING spending < 50.000
ORDER BY spending ASC;

#11. Find the top 3 countries with the highest lifetime cup consumption:
SELECT country, continent, MAX(lifetime_cup_consumption_cup) max_consumption
FROM df_consumption_finall
GROUP BY country, continent
ORDER BY max_consumption DESC
LIMIT 3;

#Queries for production data
USE producers;

#12. Producers of Arabica Coffee Beans
SELECT "Arabica Production", Countries
FROM coffee_dataset
GROUP BY Countries;

#13. Producers of Robusta Coffee Beans
SELECT "Robusta Production", Countries
FROM coffee_dataset
GROUP BY Countries;

#14. Biggest Importers
SELECT "Imports", Countries
FROM coffee_dataset
GROUP BY Countries;

#15. Biggest Exporters
SELECT "Exporters", Countries
FROM coffee_dataset
GROUP BY Countries;

#16. Top 5 coffee-producing countries in 2025:
SELECT Countries, `2025` AS production_volume
FROM coffee_dataset
WHERE Countries <> 'Total'
ORDER BY `2025` DESC
LIMIT 5;

#17. Compare production between 2020 and 2025:
SELECT Countries, `2020` AS production_2020, `2025` AS production_2025, (`2025` - `2020`) AS production_change
FROM coffee_dataset
WHERE Countries <> 'Total'
ORDER BY production_change DESC;

#18. Total coffee production by category:
SELECT Categories, SUM(`2025`) AS total_production_2025
FROM coffee_dataset
WHERE Categories IS NOT NULL
GROUP BY Categories
ORDER BY total_production_2025 DESC;

#19. Find the country with the lowest coffee production in 2025:
SELECT Countries, `2025` AS production_2025
FROM coffee_dataset
WHERE Countries <> 'Total'
ORDER BY `2025` ASC
LIMIT 1;

#20. Get the top 3 countries with the highest increase in production from 2020 to 2025:
SELECT Countries, `2020` AS production_2020, `2025` AS production_2025, (`2025` - `2020`) AS production_change
FROM coffee_dataset
WHERE Countries <> 'Total'
ORDER BY production_change DESC
LIMIT 3;

