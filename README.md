
#  RevInsight: Sales and Profit Intelligence

This is a personal data project where I analyze vendor sales, purchases, and freight data using Python, SQL, and Power BI.  It covers end-to-end data handling — from ingestion of raw CSV files to generation of key business metrics and insightful visual dashboards.
The final output is a clean summary table and a Power BI dashboard that shows profit margins, stock turnover, and top-performing brands.
I built this to strengthen my data analytics skills and learn how to move from raw files to business insights.

## 🧠 Why I Built This
I wanted to understand how vendors contribute to overall business performance. This project gave me hands-on practice with SQL joins, data cleaning, and visualizing business KPIs in Power BI.

---

##  Features

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

## Project Structure

| File/Folder                         | Description                                                |
|------------------------------------|------------------------------------------------------------|
| `data/`                             | Folder with all input CSVs (sales, purchases, etc.)        |
| `logs/`                             | Log files from data ingestion and summary steps            |
| `ingestion_db.py`                   | Script to load CSVs into a SQLite database                 |
| `sales_summary.py`                  | SQL joins + KPI calculations + data cleaning               |
| `EDA for sales analysis.ipynb`      | Jupyter notebook for visual and statistical analysis       |
| `SQL for sales analysis.ipynb`      | SQL queries to explore vendor sales                        |
| `Vendor Sales Project Dashboard.pbix` | Power BI dashboard built using cleaned data              |
| `inventory.db`                      | SQLite database created automatically                      |


---

## Tech Stack

- **Python 3.x**
  - `pandas`, `sqlite3`, `sqlalchemy`, `logging`
- **SQLite** – lightweight local database
- **Jupyter Notebook** – for EDA and SQL prototyping
- **Power BI** – for interactive dashboards

---

##  Workflow

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

####  Jupyter EDA

* Open `EDA for sales analysis.ipynb` to analyze trends, top vendors, sales patterns, etc.

---

#### Power BI Dashboard Insights

The Power BI dashboard (`Vendor Sales Project Dashboard.pbix`) summarizes the performance of vendors and brands using visual KPIs and charts. It was built on top of the cleaned `final_table` generated through SQL and Python scripts.

Here are some of the key insights:

*  **Total Sales**: \$441.41 million
*  **Total Purchase**: \$307.34 million
*  **Gross Profit**: \$134.07 million
*  **Profit Margin**: 38.7%
*  **Unsold Capital**: \$2.71 million tied up in unsold inventory
*  **Total Vendors**: 119


 **Top Performers**

* **Top Vendor by Sales**: Diageo North America Inc. (\$68M)
* **Top Brand**: Jack Daniel's (\$8M)
* Other strong vendors include Martignetti, Pernod Ricard, Jim Beam Brands, and Bacardi USA.

 **Low Performers**

* Vendors like Alisa Carr Beverages and Highland Wine Merchants showed the lowest contributions or margins.
* Scatter plot analysis highlights brands with **low profit margins** despite high total sales — potential candidates for review or pricing optimization.

**Strategic Highlights**

* A small group of vendors account for a large share of purchases — useful for renegotiating contracts or planning bulk orders.
* Several brands show strong sales but low profitability — can be addressed by reviewing discounting, freight, or tax factors.
* The dashboard makes it easier to **spot inefficiencies and improve vendor strategies**.

>  The `.pbix` file can be opened in Power BI Desktop for full interactivity.

---

##  Metrics Calculated

| Metric                | Formula                                      |
| --------------------- | -------------------------------------------- |
| **Gross Profit**      | `TotalSalesDollars - TotalPurchaseDollars`   |
| **Profit Margin (%)** | `(GrossProfit / TotalSalesDollars) * 100`    |
| **Stock Turnover**    | `TotalSalesQuantity / TotalPurchaseQuantity` |
| **Sales-to-Purchase** | `TotalSalesDollars / TotalPurchaseDollars`   |

---

##  What Could Be Better
Right now, the ingestion script replaces tables each time. Eventually, I want to switch to incremental loading and maybe move from SQLite to PostgreSQL.

---

## 📌 Author

👤 **[Nitya-34](https://github.com/Nitya-34)**

---



