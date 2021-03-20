# how to connect Python to SQL Server
# pip install pyodbc

import pyodbc
conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=server_name;'
                      'Database=database_name:'
                      'Trusted_Connection=yes;')

cursor = conn.curor()
cursor.execute('SELECT * FROM database_name.table')

for row in  cursor:
    print(row)

#
