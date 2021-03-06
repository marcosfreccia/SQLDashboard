import sys
import pyodbc
from django.db import connections
from request.utils import retrieve_server_name_tcp_port


def validate_database_name(server_name,database_name):
    try:
        server_name = retrieve_server_name_tcp_port(server_name)
        print(server_name)
        cnxn = pyodbc.connect(r"Driver={ODBC Driver 17 for SQL Server};Server="+str(server_name)+";Database=master;Trusted_Connection=yes;APP='sql-dashboard check database existance '")
        custom_cursor = cnxn.cursor()
        custom_cursor.execute("SELECT name AS database_name FROM sys.databases WHERE name = '{0}'".format(database_name))
        database_name_exists = custom_cursor.fetchall()
        if(database_name_exists):
            data = {
            'is_taken':True
                }
            if data['is_taken']:
                data['error_message'] = "Database " + database_name + " already exists on " + server_name
            cnxn.close()
            return data
        else:
            data = {
            'is_taken':False
                }
            return data
    except:
        error = sys.exc_info()
        print(error)
