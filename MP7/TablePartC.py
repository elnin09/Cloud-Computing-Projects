import happybase as hb
import csv


file=open("input.csv", "r")
reader = csv.reader(file)
connection = hb.Connection('localhost', autoconnect=False)
connection.open()
table = connection.table('powers')
for line in reader:
    data = {
        b'personal:hero': line[1],
        b'personal:power': line[2],
        b'professional:name': line[3],
        b'professional:xp': line[4],
        b'custom:color' : line[5]
    }
    table.put(line[0], data)
