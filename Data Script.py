import redshift_connector
import pandas as pd
from redshift_connector import cursor
import pandas_profiling as pp

host = input('Please enter the local host: ')
database = input('Please enter the database name: ')
user = input('Enter user name: ')
password = input('Enter the password: ')
conn = redshift_connector.connect(
    host=host,
    database=database,
    user=user,
    password=password)

table_name = input('Please enter the table name ')
mycursor: redshift_connector.cursor=conn.cursor()
statement = "Select * from " + table_name
mycursor.execute(statement)
myresult : pd.DataFrame = mycursor.fetch_dataframe()
myresult.head()
profile = pp.ProfileReport(myresult)
profile.to_file("output.html")
