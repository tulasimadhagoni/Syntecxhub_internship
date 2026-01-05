import csv
import openpyxl

workbook = openpyxl.Workbook()
sheet = workbook.active

with open("sample.csv", "r") as file:
    reader = csv.reader(file)
    for row in reader:
        sheet.append(row)

workbook.save("output.xlsx")

print("CSV successfully converted to Excel")