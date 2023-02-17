

from prettytable import PrettyTable
table=PrettyTable()
#adding one row at a time
tablefield_names=["city name","area","population","jobs available"]
table.add_row(["Nairobi","CBD","5 million","2.5million"])
print(table)
