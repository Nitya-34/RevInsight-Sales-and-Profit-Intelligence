import sqlite3
import pandas as pd
import logging
from ingestion_db import ingest_db

logging.basicConfig(
    filename='logs/sales_summary.log',
    level=logging.DEBUG,
    format='%(asctime)s - %(levelname)s - %(message)s',
    filemode='a'
)

def create_vendor_summary(conn):
    final_table = pd.read_sql_query(""" WITH FreightSummary as(
    SELECT VendorNumber, SUM(Freight) as Freight_cost 
    FROM vendor_invoice 
    GROUP BY VendorNumber
    ),
                                    
    PurchaseSummary as(
        SELECT p.VendorNumber, p.VendorName, p.Brand, p.Description, pp.Price as ActualPrice, pp.Volume , p.PurchasePrice, SUM(p.Quantity) as TotalPurchaseQuantity, SUM(p.Dollars) as TotalPurchaseDollars
                  FROM purchases p JOIN 
                  purchase_prices pp ON p.Brand=pp.Brand
                  WHERE p.PurchasePrice>0
                  GROUP BY p.VendorNumber, p.VendorName, p.Brand
                  ORDER BY TotalPurchaseDollars
    ),
    
    SalesSummary as(
       SELECT VendorNo, Brand, SUM(SalesDollars) as TotalSalesDollars, SUM(SalesQuantity) as TotalSalesQuantity, SUM(ExciseTax) as TotalExciseTax,      SUM(SalesPrice) as TotalSalesPrice
        FROM Sales
        GROUP BY VendorNo, Brand
    )           
        
    SELECT
        ps.VendorNumber,
        ps.VendorName,
        ps.Brand,
        ps.Description,
         ps.Volume,
        ps.ActualPrice,
        ps.PurchasePrice,
        ps.TotalPurchaseQuantity,
        ps.TotalPurchaseDollars,
        ss.TotalSalesQuantity,
        ss.TotalSalesDollars,
        ss.TotalSalesPrice,
        ss.TotalExciseTax,
        fs.Freight_cost    
        FROM PurchaseSummary ps
        LEFT JOIN SalesSummary ss ON ps.VendorNumber = ss.VendorNo AND ps.Brand = ss.Brand
        LEFT JOIN FreightSummary fs ON ps.VendorNumber = fs.VendorNumber
        ORDER BY ps.TotalPurchaseDollars DESC""", conn)
    
    return final_table


def clean_data(df):
    df['Volume']=df['Volume'].astype('float64')
    df.fillna(0, inplace=True)
    df['VendorName']=df['VendorName'].str.strip()
    
    final_table['GrossProfit']=final_table['TotalSalesDollars']-final_table['TotalPurchaseDollars']
    final_table['ProfitMargin']=final_table['GrossProfit']/final_table['TotalSalesDollars']*100
    final_table['StockTurnover']= final_table['TotalSalesQuantity']/final_table['TotalPurchaseQuantity']
    final_table['SalestoPurchaseRatio']= final_table['TotalSalesDollars']/final_table['TotalPurchaseDollars']

    return df


if __name__ == "__main__":
    conn = sqlite3.connect("inventory.db")

    logging.info("Creating the final sales table")
    final_table = create_vendor_summary(conn)
    logging.info(final_table.head().to_string())

    logging.info("Cleaning data")
    cleaned_df = clean_data(final_table)
    logging.info(cleaned_df.head().to_string())

    logging.info("Ingesting into DB")
    ingest_db(cleaned_df, 'final_table', conn)
    logging.info("Ingestion completed")


