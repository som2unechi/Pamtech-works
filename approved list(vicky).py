
# import openpyxl
#
# def remove_repeated_phone_numbers(file_path):
#     # Load the Excel workbook
#     workbook = openpyxl.load_workbook(file_path)
#
#     # Select the active sheet
#     sheet = workbook.active
#
#     # Create a set to store unique phone numbers
#     unique_phone_numbers = set()
#
#     # Iterate through the rows in the sheet
#     rows_to_delete = []
#     for row in sheet.iter_rows(min_row=1, values_only=True):
#         if len(row) >= 2:  # Check if the row has at least 2 columns
#             phone_number = row[1]  # Assuming phone numbers are in the second column (column B)
#             if phone_number not in unique_phone_numbers:
#                 unique_phone_numbers.add(phone_number)
#             else:
#                 rows_to_delete.append(row)
#
#     # Delete the repeated rows from the sheet
#     for row in rows_to_delete:
#         sheet.delete_rows(row[0])
#
#     # Save the modified workbook
#     workbook.save(file_path)
#
#
#
#
# # Specify the file path of the Excel spreadsheet
# file_path = r"C:\Users\user\OneDrive\Documents\VICKY AND ESTHER'S APPROVED CONTACT NOS..xlsx"
#
# # Call the function to remove repeated phone numbers
# remove_repeated_phone_numbers(file_path)


import openpyxl
import csv
def remove_repeated_phone_numbers(phone_numbers):
    unique_phone_numbers = set()
    filtered_phone_numbers = []

    for phone_number in phone_numbers:
        if phone_number not in unique_phone_numbers:
            unique_phone_numbers.add(phone_number)
            filtered_phone_numbers.append(phone_number)
            print("Filtered Phone Number:", phone_number)
            print(len(unique_phone_numbers))

    return filtered_phone_numbers

phone_numbers = [
    "0818 4277905",
    "+234 803 773 5681",
    "0704 1213276",
    "0803 3917883",
    "+370 67549702",
    "+370 67549702",
    "0704 1947583",
    "0803 4353565",
    "0907 4472858",
    "0907 4472858",
    "0814 1783982",
    "0706 7413241",
    "0814 7011698",
    "0907 9309753, +971 58 898 1731",
    "0906 4736948",
    "0902 9298651",
    "0906 0327282",
    "0814 7823681",
    "0906 5957781",
    "0803 7972418",
    "0902 4031538",
    "0803 9743340",
    "0803 3263354",
    "0816 8798112",
    "0810 4671525",
    "0810 4671525",
    "0803 5003550",
    "0803 5003550",
    "0806 2866077",
    "0806 2866077",
    "0907 4472858",
    "0809 5461950",
    "0706 1927651",
    "0810 5601224",
    "0902 3510526",
    "0812 3942213",
    "0812 3942213",
    "0703 9338791",
    "0813 6245878",
    "0803 3279005",
    "0703 3087715",
    "0806 1325457",
    "0806 1325457",
    "0906 4548812",
    "0906 4548812",
    "0810 1260693",
    "0816 5160706",
    "0803 4078107",
    "0903 8144189",
    "0703 4871388",
    "0814 3589784",
    "0814 3589784",
    "+2348 146624121",
    "+2348 146624121",
    "0703 4994266",
    "0703 4994266",
    "0810 57356565",
    "0813 1991112",
    "0803 6775850",
    "0906 6628687",
    "+7909 6632439",
    "0706 3677280",
    "0902 2549598",
    "0902 2549598",
    "0812 7940262",
    "0812 7940262",
    "0810 4165898",
    "0905 5184840",
    "0803 9354924",
    "0806 4996808",
    "0810 4361719",
    "0810 4361719"]




filtered_numbers = remove_repeated_phone_numbers(phone_numbers)
# Write filtered phone numbers to a CSV file
output_file = "filtered_phone_numbers.csv"
with open(output_file, "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Filtered Phone Numbers"])
    writer.writerows([[number] for number in filtered_numbers])

print("\nFiltered Phone Numbers:")
for number in filtered_numbers:
    print(number)

print("Filtered phone numbers written to", output_file)
print("\nFiltered Phone Numbers:")
for number in filtered_numbers:
    print(number)
print(len(filtered_numbers))


