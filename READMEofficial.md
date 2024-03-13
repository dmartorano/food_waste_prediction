# Predicting Greenhouse Gas Emissions From The Food Supply Chain

## Data Files

ReFED_US_Food_Surplus_Detail.csv - This is a robust dataset providing national-level data about food supply, waste, and waste diversion in the US from 2010 to 2022.
clean_us_food_waste.csv - This is a dataset derived from the original dataset after cleaning and feature engineering.

## Problem Statement

In 2022, the U.S. food supply chain generated 88.7 million tons of surplus food. Of that 88.7 million tons, 16.2 million tons were converted into composting material, 8.2 million tons were converted into animal feed, 3.8 million tons were used directly in revitalizing farm land, 1.1 million tons were used in the anaerobic digestion process, and only 1.8 million tons were donated to those in need. The other 57.6 million tons were either dumped in landfills or sewers, incinerated, or simply not harvested. 

All of these methods contribute to the greenhouse gas emissions produced by the food supply chain, but some methods are more helpful to society than others. The goal of this project is to help predict how much greenhouse gas is produced by our food throughout its lifecycle and to figure out what methods might be the least detrimental.

## Data Dictionary

|Feature|Type|Description|
|---|---|---|
|year|integer|Year of data collection|
|tons_surplus|float|Amount of excess food supplied in tons|
|tons_supply|float|Amount of total food supplied in tons|
|us_dollars_surplus|float|Price of surplus food in US dollars|
|tons_waste|float|Amount of food wasted in tons|
|tons_uneaten|float|Amount of food that is not eaten in tons|
|tons_inedible_parts|float|Amount of 'food' that includes bones, egg shells, stems, etc. in tons|
|tons_not_fit_for_human_consumption|float|Amount of food deemed not fit for consumption in tons|
|tons_donated|float|Amount of food donated to food pantries and similar entities in tons|
|tons_biomaterial_processing|float|Amount of food diverted to industrial purposes such as fuel and energy conversion in tons|
|tons_animal_feed|float|Amount of food converted into animal feed in tons|
|tons_anaerobically_digested|float|Amount of food used in anaerobic digestion in tons|
|tons_composted|float|Amount of food composted in tons|
|tons_not_harvested|float|Amount of food not harvested in tons|
|tons_incinerated|float|Amount of food incinerated in tons|
|tons_land_application|float|Amount of food waste applied directly to land to impart nutrients in tons|
|tons_landfilled|float|Amount of food disposed of in landfills in tons|
|tons_sewer|float|Amount of food disposed of in sewers in tons|
|tons_refuse_discards|float|Amount of food discarded at the packhouse due to failure to meet expectations in tons|
|upstream_mtco2e_footprint|float|Metric tons of greenhouse gases produced prior to waste processing (production, transportation, storage)|
|downstream_mtco2e_footprint|float|Metric tons of greenhouse gases produced as a result of waste processing (transportation to processing facility and act of processing)|
|total_mtco2e_footprint|float|Metric tons of greenhouse gases produced, aggregate of upstream and downstream|
|gallons_water_footprint|float|Gallons of water used in process in millions|
|meals_wasted|float|Standardized 1.2 pound units of food wasted|
|sector_farm|integer|Determines whether or not data is from the farm sector|
|sector_foodservice|integer|Determines whether or not data is from the foodservice sector|
|sector_manufacturing|integer|Determines whether or not data is from the manufacturing sector|
|sector_residential|integer|Determines whether or not data is from the residential sector|
|sector_retail|integer|Determines whether or not data is from the retail sector|
|food_type_breads_&_bakery|integer|Determines if food is a bakery item|
|food_type_dairy_&_eggs|integer|Determines if food is a dairy item|
|food_type_dry_goods|integer|Determines if food is a dry good|
|food_type_fresh_meat_&_seafood|integer|Determines if food is fresh meat or seafood|
|food_type_frozen|integer|Determines if food is frozen|
|food_type_prepared_foods|integer|Determines if food is a prepared food|
|food_type_produce|integer|Determines if food is produce|
|food_type_ready-to-drink_beverages|integer|Determines if food is a ready-to-drink beverage|
|tons_productive_surplus|float|Amount of food disposed of in environmentally "responsible" ways|
|tons_unproductive_surplus|float|Amount of food disposed of in environmentally "irresponsible" ways|
|tons_consumed|float|Amount of food supplied and not surplus|

## Summary

After performing EDA on the correlations in the data, the distribution of the data, and the over-time trends in the food surplus, several regression models were tested in order to best predict the greenhouse gas emissions from the food supply chain. While the various forms of linear regression offered fairly high R-scores, their other metrics were quite high, indicating poor predictability. The decision tree and random forest models yielded significantly smaller metrics, indicating that they are better at predicting the greenhouse gas emissions based on the data used, although the lowest RMSE was still 86,121. However, based on the scale of the data, this RMSE is still fairly good.

## Streamlit App


