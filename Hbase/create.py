import happybase
connection = happybase.Connection(host = 'localhost', port = 9999)
connection.create_table('bpotinen',{'cc':dict(),'d':dict()})
print connection.tables()
connection.close()