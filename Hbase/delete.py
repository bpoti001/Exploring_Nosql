import happybase
connection = happybase.Connection(host='localhost', port = 9999)
connection.delete_table('bpotinen', disable=True)
print connection.tables()
