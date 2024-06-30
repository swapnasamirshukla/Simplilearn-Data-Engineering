# Sales Data Visualization Using Azure Synapse Analytics
## Course-end Project 2

### Description

A leading retailer has many branches across various locations in India. Each branch operator is recording the sales data in CSV format and uploading it to the cloud. Upper management wants to visualize the sales data using a dashboard to estimate the demand for all locations, which they will use to make decisions on where to open a new branch.

### Steps to Perform

1. **Create a Landing Storage Account in Azure**
    - Set up a storage account in Azure.
    - Upload a CSV file with sales data to the storage account.

2. **Create a Staging Storage Account in Azure**
    - Set up another storage account in Azure for staging purposes.

3. **Create an Azure Data Factory Resource**
    - Set up an Azure Data Factory (ADF) resource.
    - Create linked services for the storage accounts.

4. **Create an Azure Databricks Workspace**
    - Set up an Azure Databricks workspace as part of the ADF pipeline.

5. **Create Linked Services in ADF for Databricks**
    - Configure linked services in ADF for the Databricks workspace.

6. **Convert CSV Files to Parquet Files**
    - Use the ADF pipeline to convert the CSV files in the landing storage account to Parquet files in the staging storage account.

7. **Convert Parquet Files to Azure Databricks Delta Tables**
    - Use Databricks to convert the Parquet files into Delta tables.

8. **Create an Azure Synapse Analytics Instance**
    - Set up an Azure Synapse Analytics instance.

9. **Create SQL Tables in Azure Synapse Analytics**
    - Define SQL tables in the Synapse Analytics instance to store the incoming data.

10. **Store Incoming Data in Azure Synapse Analytics Using Databricks**
    - Utilize Databricks to store the processed data into the SQL tables in Azure Synapse Analytics.
