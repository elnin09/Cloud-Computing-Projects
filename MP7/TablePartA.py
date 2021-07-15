import happybase as hb

connection = hb.Connection('localhost', autoconnect=False)
connection.open()
#print(connection.tables())

connection.create_table(
 'powers',
 {  'personal': dict(), # it uses defaults, if you want you can define column definitions
    'professional': dict(),
    'custom': dict()
 }
)
connection.create_table(
     'food',
     {  'nutrition': dict(), # it uses defaults, if you want you can define column definitions
        'taste': dict()
    }
)