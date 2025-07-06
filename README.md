
# 📊 Vendor Sales Analysis

This project performs a detailed **sales and purchase analysis** for vendors using Python, SQL, SQLite, and Power BI. It covers end-to-end data handling — from ingestion of raw CSV files to generation of key business metrics and insightful visual dashboards.

---

## 🚀 Features

- **Automated data ingestion** from CSV files into SQLite
- **SQL-powered aggregation** of purchases, sales, and freight data
- **Computation of vendor-wise KPIs**, including:
  - Gross Profit
  - Profit Margin
  - Sales-to-Purchase Ratio
  - Stock Turnover
- **Power BI Dashboard** with interactive visuals
- **Logged execution** for traceability
- **Jupyter Notebooks** for EDA and SQL testing

---

## 🧱 Project Structure


Vendor-Sales-Analysis/
│
├── data/                         # Raw CSV files (Sales, Purchases, etc.)
├── logs/                         # Log files for data pipeline steps
│
├── ingestion\_db.py              # Script to ingest CSVs into SQLite
├── sales\_summary.py             # SQL + Python script to generate clean summary
├── EDA for sales analysis.ipynb # Exploratory Data Analysis using pandas/plots
├── SQL for sales analysis.ipynb # SQL queries and testing on inventory.db
├── inventory.db                 # SQLite database (auto-generated)
├── PowerBI Dashboard.pbix       # Power BI file (based on final\_table)
└── README.md                    # You're here!

---

## 🛠️ Tech Stack

- **Python 3.x**
  - `pandas`, `sqlite3`, `sqlalchemy`, `logging`
- **SQLite** – lightweight local database
- **Jupyter Notebook** – for EDA and SQL prototyping
- **Power BI** – for interactive dashboards

---

## 🔄 Workflow

### Step 1: Ingest Data

Place `.csv` files in `data/`. Run:

```bash
python ingestion_db.py
````

* Loads each CSV into SQLite as a table.
* Logs stored in `logs/ingestion_db.log`.

👉 Tip: To support weekly incremental updates, switch `if_exists='replace'` to `'append'` in the script.

---

### Step 2: Generate Clean Summary

```bash
python sales_summary.py
```

* Creates a comprehensive vendor-wise summary using SQL joins and aggregations.
* Computes key metrics (profit, ratios, turnover).
* Cleans the data and stores the result in `final_table` inside `inventory.db`.
* Logs execution to `logs/sales_summary.log`.

---

### Step 3: Explore & Visualize

#### 🔍 Jupyter EDA

* Open `EDA for sales analysis.ipynb` to analyze trends, top vendors, sales patterns, etc.

#### 📊 Power BI Dashboard

* File: `Vendor Sales Project Dashboard.pbix`
* Built using the output from `final_table`
* Includes charts like:

  * Top Performing Vendors
  * Brand-wise Profit Margins
  * Sales vs Purchase Comparison
  * Freight Cost Analysis

---

## 📈 Metrics Calculated

| Metric                | Formula                                      |
| --------------------- | -------------------------------------------- |
| **Gross Profit**      | `TotalSalesDollars - TotalPurchaseDollars`   |
| **Profit Margin (%)** | `(GrossProfit / TotalSalesDollars) * 100`    |
| **Stock Turnover**    | `TotalSalesQuantity / TotalPurchaseQuantity` |
| **Sales-to-Purchase** | `TotalSalesDollars / TotalPurchaseDollars`   |

---

## 📌 Author

👤 **[Nitya-34](https://github.com/Nitya-34)**

---



