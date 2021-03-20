from prettytable import PrettyTable
# Specify the Column Names while initializing the Table
myTable = PrettyTable(["Student Name", "Last Name", "Course", "Percentage of grades"])
# add rows
myTable.add_row(["Lucas", "Santos", "Computação", "85.55 %"])
myTable.add_row(["Michael", "Polidoro", "Sistemas", "85.66 %"])
myTable.add_row(["Murilo", "Doido", "Banco de dados", "75.80 %"])
myTable.add_row(["Henrique", "Neves", "Analytics", "80.75"])
print(myTable)


