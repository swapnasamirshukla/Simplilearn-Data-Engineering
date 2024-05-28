# Exploratory Data Analysis on NYSE Data (2010-2016)

## Description

### Objective
To use Hive features for data engineering or analysis and share actionable insights.

### Problem Statement
New York Stock Exchange data for seven years, from 2010 to 2016, has been captured for 500+ listed companies. The dataset comprises intra-day prices and volume traded for each listed company. The data serves both machine learning and exploratory analysis projects, aiming to automate the trading process and predict the next trading-day winners or losers. This project's scope is limited to exploratory data analysis.

### Domain
Banking, Financial Services, and Insurance (BFSI)

### Analysis to be Done
Perform exploratory analysis to understand how month-over-month (MoM) or year-over-year (YoY) companies from different sectors, industries, and states have progressed over a period of 7 years.

### Content
The dataset contains two files: `prices.csv` and `securities.csv`.

#### `prices.csv`
- **Date:** Trading date
- **Symbol:** Ticker code or listed company code on NY stock exchange
- **Open:** Intra-day opening price for each listed company
- **Close:** Intra-day closing price for each listed company
- **Low:** Intra-day lowest price for each listed company
- **High:** Intra-day highest price for each listed company
- **Volume:** Number of shares traded per day per company

#### `securities.csv`
- **Ticker_Symbol:** Ticker code
- **Security:** Legal name of the listed company
- **Sector:** Business vertical of the listed company
- **Sub_Industry:** Business domain of the listed company within a sector
- **Headquarter:** Headquarters address

## Steps to Perform

### 1. Create a Data Pipeline Using Sqoop

Pull the data from the tables below from the MySQL server into Hive.

#### MySQL Database Name
BDHS_PROJECT

#### Tables
- **Stock_prices**
- **Stock_companies**

#### Table Descriptions

**`STOCK_PRICES`**
| Column Name   | Datatype |
|---------------|----------|
| Trading_date  | Date     |
| Symbol        | String   |
| Open          | Double   |
| Close         | Double   |
| Low           | Double   |
| High          | Double   |
| Volume        | Int      |

**`STOCK_COMPANIES`**
| Column Name   | Datatype |
|---------------|----------|
| Symbol        | String   |
| Company_name  | String   |
| Sector        | String   |
| Sub_industry  | String   |
| Headquarter   | String   |

### 2. Create a New Hive Table

Create a new Hive table by joining the above two Hive tables. Use appropriate Hive built-in functions for the columns listed below.

- **Trading_year:** Should contain YYYY for each record
- **Trading_month:** Should contain MM or MMM for each record
- **Symbol:** Ticker code
- **CompanyName:** Legal name of the listed company
- **State:** State to be extracted from headquarters value
- **Sector:** Business vertical of the listed company
- **Sub_Industry:** Business domain of the listed company within a sector
- **Open:** Average of intra-day opening price by month and year for each listed company
- **Close:** Average of intra-day closing price by month and year for each listed company
- **Low:** Average of intra-day lowest price by month and year for each listed company
- **High:** Average of intra-day highest price by month and year for each listed company
- **Volume:** Average of the number of shares traded by month and year for each listed company

### 3. Data Analysis Using Hive

- Find the top five companies that are good for investment
- Show the best-growing industry by each state, having at least two or more industries mapped
- For each sector, find the following:
  - Worst year
  - Best year
  - Stable year
