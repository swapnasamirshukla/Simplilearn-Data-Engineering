import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job

args = getResolvedOptions(sys.argv, ["JOB_NAME"])
sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args["JOB_NAME"], args)

# Script generated for node AWS Glue Data Catalog
AWSGlueDataCatalog_node1710716550592 = glueContext.create_dynamic_frame.from_catalog(
    database="crawl-output",
    table_name="csvoutput-data_utf8_csv",
    transformation_ctx="AWSGlueDataCatalog_node1710716550592",
)

# Script generated for node Change Schema
ChangeSchema_node1710716557710 = ApplyMapping.apply(
    frame=AWSGlueDataCatalog_node1710716550592,
    mappings=[
        ("invoiceno", "string", "invoiceno", "string"),
        ("stockcode", "string", "stockcode", "string"),
        ("description", "string", "description", "string"),
        ("quantity", "long", "quantity", "long"),
        ("invoicedate", "string", "invoicedate", "string"),
        ("unitprice", "double", "unitprice", "double"),
        ("customerid", "long", "customerid", "long"),
        ("country", "string", "country", "string"),
    ],
    transformation_ctx="ChangeSchema_node1710716557710",
)

# Script generated for node Amazon S3
AmazonS3_node1710716564846 = glueContext.write_dynamic_frame.from_options(
    frame=ChangeSchema_node1710716557710,
    connection_type="s3",
    format="glueparquet",
    connection_options={
        "path": "s3://project1bysamir/parquetfolder/",
        "partitionKeys": [],
    },
    format_options={"compression": "snappy"},
    transformation_ctx="AmazonS3_node1710716564846",
)

job.commit()
