Week 1 – Batch-Based Data Ingestion Pipeline
Objective

Build a simple data ingestion pipeline using Python and MySQL.

Dataset

Iris Flower Dataset – Kaggle

https://www.kaggle.com/datasets/uciml/iris

Technologies
Python
MySQL
MySQL Workbench
MySQL Connector/Python
Project Workflow
Download the Iris dataset from Kaggle.
Read CSV records using Python.
Load the data into the source MySQL database.
Fetch records in batches of 25.
Insert batches into the target MySQL database.
Validate source and target record counts.
Database Design
Source database: source_db
Target database: target_db
Table: iris

Both databases are hosted on the same MySQL server.

Batch Processing
Total records: 150
Batch size: 25 records
Total batches: 6
Execution
bash
pip install -r requirements.txt
python main.py


Configure your MySQL credentials in config.py before running.

Expected Result
text
Source records: 150
Target records: 150
SUCCESS: Data ingestion completed!

Learning Outcomes
Python CSV handling
MySQL connectivity
Source-to-target data transfer
Batch processing
Data validation

Status: Completed