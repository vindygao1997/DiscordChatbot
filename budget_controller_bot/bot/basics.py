import csv

categories = ['grocery', 'clothes', 'makeup', 'travel', 'dining out', 'tuition', 'rent and fees', 'jewlery']
#create the csv file to store where my money goes
fields = categories
filename = "money_tracking.csv"
with open(filename, 'w') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames = fields)
    writer.writeheader()