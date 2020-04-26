import happybase as hb

# DON'T CHANGE THE PRINT FORMAT, WHICH IS THE OUTPUT
# OR YOU WON'T RECEIVE POINTS FROM THE GRADER
connection = hb.Connection('localhost', autoconnect=False)
connection.open()
table = connection.table('powers')

for key, data in table.scan(row_start=b'row1',include_timestamp=True):
    print('Found: {}, {}'.format(key, data))
