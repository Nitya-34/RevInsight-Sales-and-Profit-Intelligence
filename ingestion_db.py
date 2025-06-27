import pandas as pd
import os
from sqlalchemy import create_engine
import logging 
import time

logging.basicConfig(
    filename='logs/ingestion_db.log',
    level=logging.DEBUG,
    format='%(asctime)s - %(levelname)s - %(message)s',
    filemode='a'
)

engine = create_engine('sqlite:///inventory.db')

def ingest_db(df,table_name,engine):
    df.to_sql(table_name, con=engine, if_exists='replace', index=False)  # use if_exists='append' for continous data
    
def load_raw_data():
    start=time.time()
    for file in os.listdir('data'):
        if '.csv' in file:
            df=pd.read_csv('data/'+file)
            logging.info(f'Ingesting {file} in db')
            ingest_db(df, file[:-4], engine)   
    end=time.time()
    total_time= (end-start)/60
    logging.info("-------------------Ingestion complete------------------")
    logging.info(f'\nTotal time taken {total_time} minutes')

if __name__ == '__main__':
    load_raw_data()


"""✅ How to Use This Script When You Have New Data
    📝 Steps:
    Place your new CSV file in the data/ folder.Example: data/sales_2025.csv
    
    Run the script from the terminal:    
    >>>  python your_script_name.py
    
    Replace your_script_name.py with the actual file name, e.g. ingest.py.
    
    It will:    
    Read the new file    
    Create/replace the corresponding table in inventory.db    
    Log everything in logs/ingestion_db.log


    🔄 To Support Weekly Additions Without Deleting Old Data
    Change this line:   
    >>> df.to_sql(table_name, con=engine, if_exists='replace', index=False)
    To this:    
    >>> df.to_sql(table_name, con=engine, if_exists='append', index=False)
    This will append the new rows to the existing table each week.
"""