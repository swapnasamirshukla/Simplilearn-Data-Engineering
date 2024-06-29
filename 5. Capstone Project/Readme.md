# E-commerce Sales Data Analysis

## Description

You work for an e-commerce company as a big data consultant. Your job entails analyzing sales data. The company operates at a number of locations around the world. They want you to analyze the data from their sales transactions on a daily and weekly basis and derive significant insights to understand their sales in various cities and states. You've also been asked to include a variety of other details about the product evaluation.

## Objective

- Use Spark features for data analysis to derive valuable insights.
- Perform exploratory analysis to determine actionable insights.

## Domain

E-commerce

## Dataset

**File:** `olist_public_dataset.csv`

### Dataset Description

- `Id`
- `order_status`
- `order_products_value`
- `order_freight_value`
- `order_items_qty`
- `order_purchase_timestamp`
- `order_aproved_at`
- `order_delivered_customer_date`
- `customer_city`
- `customer_state`
- `customer_zip_code_prefix`
- `product_name_lenght`
- `product_description_lenght`
- `product_photos_qty`
- `review_score`

## Analysis

### Insights on Historical Data

#### 1. Daily Insights

**a. Sales**

- Total sales
- Total sales in each city
- Total sales in each state

**b. Orders**

- Total number of orders
- City-wise order distribution
- State-wise order distribution
- Average review score per order
- Average freight charges per order
- Average time taken to approve the orders (order approved – order purchased)
- Average order delivery time

#### 2. Weekly Insights

**a. Sales**

- Total sales
- Total sales in each city
- Total sales in each state

**b. Orders**

- Total number of orders
- City-wise order distribution
- State-wise order distribution
- Average review score per order
- Average freight charges per order
- Average time taken to approve the orders (order approved – order purchased)
- Average order delivery time

**c. Total Freight Charges**

**d. Distribution of Freight Charges in Each City**

### Week 1: Overview and Basic Configurations

#### Step 1: Choose a Suitable Cloud Provider and Set Up a Spark Shell Environment
- Select a cloud provider (e.g., AWS, Azure, GCP).
- Set up a Spark shell environment using the chosen cloud provider.

#### Step 2: Configure the Necessary Dependencies
- Install and configure all required dependencies for Spark, including Hadoop and Hive.

#### Step 3: Execute Basic Spark Commands to Ensure Spark is Ready
- Execute basic Spark commands to verify that the Spark environment is properly set up and functioning.

#### Step 4: Use `README.md` for Details, Instructions, and Commands
- Create and maintain a `README.md` file with all the necessary details, instructions, and commands for setting up and using the Spark environment.

### Week 2: Data Ingestion

#### Step 1: Upload Data into Hive from CSV Using Cloud Provider Cluster Setup
- Log in to the cluster using a tool like PuTTY with the username “hadoop”.
- Enter the following command to access Hive:
  ```bash
  hive
  ```
- Create a database and a table in Hive with all the relevant details to store the data from the CSV file.

#### Step 2: Create a Bucket and Upload the CSV File
- Create a bucket in a cloud storage service (e.g., S3 for AWS, Blob Storage for Azure).
- Upload the `olist_public_dataset.csv` file to the created bucket.

#### Step 3: Load Data from the Bucket into the Hive Table
- Load the data from the cloud storage bucket into the Hive table.

#### Step 4: Create a New Directory in HDFS and Copy Data from Hive to HDFS
- Create a new directory in HDFS.
- Copy the data from the Hive table to the HDFS directory.

#### Step 5: Verify Data Loading in HDFS
- Check if the data has been successfully loaded into the specified HDFS path.

### Week 3: Data Streaming

#### Step 1: Connect to Spark Shell with All Dependencies
- Connect to the Spark shell and ensure all dependencies (Hive, Hadoop, HDFS) are included.
- Create the schema for the CSV files.
- Create a Spark session.
- Add Object Storage Service details as per the chosen cloud provider.
- Set up environment variables to handle sensitive data.

#### Step 2: Read the CSV File and Convert to a DataFrame
- Read the `olist_public_dataset.csv` file and convert it to a Spark DataFrame.

#### Step 3: Convert `order_purchase_timestamp` to Week and Day Using UDF
- Use User Defined Functions (UDFs) to convert the `order_purchase_timestamp` field into week and day formats.

#### Step 4: Calculate Required Data
- Calculate the following metrics:
  - Total sales and order distribution per day and week for each city.
  - Total sales and order distribution per day and week for each state.
  - Average review score, average freight value, average order approval time, and delivery time.
  - Freight charges per city and total freight charges.

### Week 4: Data Analysis and Visualization

#### Step 1: Write Results into HDFS
- Write the calculated results and insights into HDFS.

#### Step 2: Save the Final Dataset into Object Storage Service
- Save the final processed dataset into the object storage service (e.g., S3, Azure Blob Storage).

#### Step 3: Create a NoSQL DB Cluster Using Relevant Cloud Service
- Create a NoSQL database cluster using the relevant service on the chosen cloud platform (e.g., DynamoDB for AWS, Cosmos DB for Azure).

#### Step 4: Save Insights in the NoSQL DB
- Save the derived insights into the NoSQL database created in the previous step.
