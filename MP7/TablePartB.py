import happybase as hb
connection = hb.Connection('localhost', autoconnect=False)
connection.open()
print(connection.tables())

