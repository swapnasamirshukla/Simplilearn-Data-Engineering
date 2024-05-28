# Lenodo E-commerce Data Analysis

## Description

Lenodo is a multinational e-commerce organization that sells products directly to consumers. The database administrator exports the data every night in a CSV file, but this export functionality is unused. Lenodo wants to use this data to uncover insights about the most-sold item and the countries where customers have bought this item.

You are a data analytics consultant, and you're asked to provide valuable insights and statistics across products, brands, categories, and segments to the marketing, product, sales, and procurement teams. Your goal is to inform them about which product has the highest amount of sales and which product and its marketing needs the most improvement. These statistics will help to run effective digital marketing campaigns. The scope of this project is limited to data engineering and analysis.

## Objective

To use AWS Big Data stack for data engineering to analyze transactions, uncover patterns, and share actionable insights.

## Steps to Perform

1. **Create an S3 bucket with a unique name and upload the CSV file to the S3 bucket (ensure that the file is in UTF-8 format only).**

2. **Create a crawler to crawl the CSV data and generate a metadata catalog.**

3. **Create a Glue job to transform the data into the Parquet format as CSV is not optimal for data warehouse queries.**

4. **Add another crawler to crawl the Parquet data files to generate the metadata catalog of the Parquet file in order to query it with Athena.**

5. **Query the data to identify the best-selling item and countries where customers have bought the most-sold item using Athena.**
