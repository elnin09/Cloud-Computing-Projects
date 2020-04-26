import happybase as hb

# DON'T CHANGE THE PRINT FORMAT, WHICH IS THE OUTPUT
# OR YOU WON'T RECEIVE POINTS FROM THE GRADER
connection = hb.Connection('localhost', autoconnect=False)
connection.open()
table = connection.table('powers')
count=0
for key, data in table.scan(row_start=b'row1',include_timestamp=False):
    for key1, data1 in table.scan(row_start=b'row1',include_timestamp=False):
        if(data["custom:color"]==data1["custom:color"] and data["professional:name"]!=data1["professional:name"] ):
            color =   data["custom:color"]
            name =    data["professional:name"]
            power =   data["personal:power"]
            color1 =  data1["custom:color"]
            name1 =   data1["professional:name"]
            power1 =  data1["personal:power"]
            print('{}, {}, {}, {}, {}'.format(name, power, name1, power1, color))
            #print('{}, {}, {}, {}, {}'.format(name, power, name1, power1, color1))
            count += 1


#print (count)
