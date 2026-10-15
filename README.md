# 👟 The Souled Store — Data Engineering Project

An end-to-end data engineering project that extracts product data from an API and processes it using Python, Databricks, PySpark, SQL, and Delta Lake.

## 📌 Project Overview

This project demonstrates a data pipeline built using the Medallion Architecture to transform raw product data into useful business insights.

The pipeline processes a sample of 24 men's footwear product records.

## 🛠️ Technologies Used

- **Python** — API data extraction
- **Requests** — HTTP API requests
- **CSV** — Data exchange and storage
- **Databricks** — Cloud data processing environment
- **PySpark** — Data transformation and cleaning
- **Delta Lake** — Structured data storage
- **SQL** — Data analysis

## 🏗️ Data Pipeline Architecture

```text
Souled Store Product API
          |
          v
   Python Extraction
          |
          v
      CSV Output
          |
          v
   Databricks Volume
          |
          v
   Bronze Layer
   Raw Product Data
          |
          v
   Silver Layer
   Cleaned and Validated Data
          |
          v
    Gold Layer
  Category-Level Summary
          |
          v
      SQL Analysis
```

## 🥉 Bronze Layer

- Loads the extracted CSV data into a Delta table.
- Preserves the raw product records for further processing.
- Records processed: **24**

## 🥈 Silver Layer

- Cleans and validates product records.
- Checks for duplicate product IDs.
- Prepares the data for analysis.
- Records processed: **24**

## 🥇 Gold Layer

Creates category-level business summaries containing:

- Total number of products
- Average product price
- Highest product price
- Total available stock

The sample data produced **5 category-level summary rows**.

## 📊 SQL Analysis

SQL is used to identify the five most expensive products in the sample dataset.

Example query:

```sql
SELECT
    id,
    title,
    category,
    price,
    stock
FROM workspace.default.soulstore_silver
ORDER BY price DESC
LIMIT 5;
```

## 📈 Project Results

| Metric | Result |
|---|---:|
| Products extracted | 24 |
| Bronze records | 24 |
| Silver records | 24 |
| Gold category summary rows | 5 |
| Duplicate product IDs found | 0 |

## 📁 Repository Structure

```text
souled-store-data-engineering/
├── README.md
└── soul_store_api.py
```

## 🚀 Future Improvements

- Automate scheduled API extraction.
- Add incremental data ingestion.
- Implement data quality checks.
- Build an interactive dashboard.
- Expand the pipeline to process additional product categories.

## 👨‍💻 Author

**Palanivel**

GitHub: [Palanivel2005](https://github.com/Palanivel2005)

---

*This is an educational data engineering project using a sample of product listing data. Product availability and prices may change.*
