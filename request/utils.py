import sys
from django.db import connections

# Still running into errors here. SQL Lite seems to be working as I expect.
def retrieve_server_name_tcp_port(server_name):
    cursor = connections['default'].cursor()
    try:
        cursor.execute("select server_name ||  ',' || tcp_port as server_name from server_servers where is_active = 1 AND server_name = '{0}'".format(server_name))
        for row in cursor.fetchall():
            return row.server_name
    except:
        error = sys.exc_info()
        print(error)