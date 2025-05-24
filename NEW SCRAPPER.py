import openpyxl
import csv

# Load the workbook
workbook = openpyxl.load_workbook('C:/Users/user/Desktop/FRONTDESK MONTHLY REPORTS/CUSTOMER OPENPYXL DATA.xlsx')

# Select the worksheet
worksheet = workbook.active

# Create a list to store the numbers
numbers = []

# Loop through all cells in the column and add their values to the list
for cell in worksheet['B']:
    if cell.value:
        numbers.append(str(cell.value))

# Write the numbers to a CSV file
with open('openpyxldata.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(numbers)
