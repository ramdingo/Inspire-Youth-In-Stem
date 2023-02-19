#!/usr/bin/env python3
#tabulation in python
#Name:Ramsey Kobia
#Email:ramseykobia@gmail.com
#date: 18th Feb 2023
#file:tabulate.py

from prettytable import PrettyTable
table=PrettyTable()
#adding one row at a time
tablefield_names=["city name","area","population","jobs available"]
table.add_row(["Nairobi","CBD","5 million","2.5million"])
table.add_row(["Machakos","Maembeni","1.5 million","300K"])
table.add_row(["Meru","Maua","2.7 millon","1 million"])
table.add_row(["Mombasa","Bombolulu","3.01 million","700K"])
print(table)