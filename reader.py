import csv
# #
# # # Open the CSV file in read mode
# # with open('example.csv', 'r') as file:
# #     # Create a reader object
# #     reader = csv.reader(file)
# #     # Skip the header row
# #
# #     # Open a new file to write the cleaned phone numbers
# #     with open('new.csv', 'w', newline='') as new_file:
# #         # Create a writer object
# #         writer = csv.writer(new_file)
# #         # Write the header row
# #         writer.writerow(['Phone Numbers'])
# #         # Iterate over each row in the CSV file
# #         for row in reader:
# #             # Replace all spaces in the phone number with an empty string
# #             phone_number = row[0].replace(' ', '')
# #             # Write the cleaned phone number to the new file
# #             writer.writerow([phone_number])
# #
# import csv
#
#
# with open('example.csv', 'r') as file:
#     # Read the entire line as a string
#     phone_numbers_string = file.readline().strip()
#     # Split the string into individual phone numbers
#     phone_numbers_list = phone_numbers_string.split(',')
#     # Clean each phone number by removing spaces
#     cleaned_numbers = [number.replace(' ', '') for number in phone_numbers_list]
#     # Join all the cleaned phone numbers into a single string
#     all_numbers = ','.join(cleaned_numbers)
#     # Open a new file to write the cleaned phone numbers
#     with open('cleaned_phone_numbers.csv', 'w', newline='') as new_file:
#         # Create a writer object
#         writer = csv.writer(new_file)
#         # Write the header row
#         writer.writerow(['Phone Numbers'])
#         # Write the cleaned phone numbers to the new file
#         writer.writerow([all_numbers])
#
# #
# #
# # Open the CSV file in read mode
# with open('output.csv', 'r') as file:
#     # Create an empty list to store the cleaned phone numbers
#     cleaned_numbers = []
#     # Iterate over each row in the CSV file
#     reader = csv.reader(file)
#     for row in reader:
#         # Iterate over each item in the row
#         for item in row:
#             # Check if the item is a phone number that starts with '0'
#             if isinstance(item, str) and item.startswith('0') and item.replace(' ', '').isdigit():
#                 # Remove any spaces from the phone number and add it to the cleaned_numbers list
#                 cleaned_numbers.append(item.replace(' ', ''))
#     # Open a new file to write the cleaned phone numbers
#     with open('cleaned_phone_numbers.csv', 'w', newline='') as new_file:
#         # Create a writer object
#         writer = csv.writer(new_file)
#         # Write the header row
#         writer.writerow(['Phone Numbers'])
#         # Write the cleaned phone numbers to the new file
#         for number in cleaned_numbers:
#             writer.writerow([number])
#
#
#
# # Open the CSV file in read mode
# with open('cleaned_phone_numbers.csv', 'r') as file:
#     # Create a reader object
#     reader = csv.reader(file)
#     # Skip the header row
#     next(reader)
#     # Open a new file to write the cleaned phone numbers
#     with open('cleaned_phone_numbers.csv', 'w', newline='') as new_file:
#         # Create a writer object
#         writer = csv.writer(new_file)
#         # Write the header row
#         writer.writerow(['Phone Numbers'])
#         # Create an empty list to store the cleaned phone numbers
#         cleaned_numbers = []
#         # Iterate over each row in the CSV file
#         for row in reader:
#             # Replace all spaces in the phone number with an empty string
#             phone_number = row[0].replace(' ', '')
#             # Add the cleaned phone number to the list
#             cleaned_numbers.append(phone_number)
#         # Join all the cleaned phone numbers into a single string
#         all_numbers = ','.join(cleaned_numbers)
#         # Write the string to the new file
#         writer.writerow([all_numbers])
# with open('cleaned_phone_numbers.csv', 'r') as file:
#         reader = csv.reader(file)
#         for row in reader:
#             for item in row:
#                 item_length = len(item)
#                 print(f'The length of "{item}" is {item_length}')


# Open the first CSV file in read mode
# with open('BLA BLA.csv', 'r') as file1:
#     reader = csv.reader(file1)
#
#     # Open the second CSV file in append mode
#     with open('openpyxldata.csv', 'a', newline='') as file2:
#         writer = csv.writer(file2)
#
#         # Append each row from the first CSV file to the second CSV file
#         for row in reader:
#             writer.writerow(row)
#
# # Count the total number of values in the combined CSV file
# with open('openpyxldata.csv', 'r') as file:
#     reader = csv.reader(file)
#     count = 0
#
#     for row in reader:
#         count += len(row)
#
# print(f'Total number of values: {count}')



# # Open the CSV file for reading
# with open('cleaned_phone_numbers.csv', 'r') as file:
#     reader = csv.reader(file)
#
#     # Create a list to store the modified rows
#     modified_rows = []
#
#     # Iterate through each row and remove quotes from each cell
#     for row in reader:
#         modified_row = [cell.replace('"', '') for cell in row]
#         modified_rows.append(modified_row)
#
# # Open the CSV file for writing and write the modified rows
# with open('example_modified.csv', 'w', newline='') as file:
#     writer = csv.writer(file)
#     writer.writerows(modified_rows)
#

#
#
# with open('openpyxldata.csv', 'r') as infile, open('cleaned.csv', 'w', newline='') as outfile:
#     reader = csv.reader(infile)
#     writer = csv.writer(outfile)
#
#     for row in reader:
#         cleaned_row = []
#         for item in row:
#             cleaned_item = ''.join(filter(lambda x: x.isdigit() or x == ',', item))
#             cleaned_row.append(cleaned_item)
#         writer.writerow(cleaned_row)



# import csv
#
# with open('cleaned.csv', 'r') as f:
#     reader = csv.reader(f)
#     phone_numbers = [number for row in reader for number in row]
#
# # remove non-numeric characters and non-comma punctuation marks
# phone_numbers = ["".join(filter(str.isdigit, number.replace(',', ''))) for number in phone_numbers]
#
# with open('cleaned3.csv', 'w', newline='') as f:
#     writer = csv.writer(f)
#     writer.writerow(phone_numbers)
#
# import csv

# open input and output files
# with open('cleaned3.csv', newline='') as csvfile_in, open('output.csv', 'w', newline='') as csvfile_out:
#     reader = csv.reader(csvfile_in)
#     writer = csv.writer(csvfile_out)
#
#     # iterate over each row in the input file
#     for row in reader:
#         # sanitize phone number field by replacing multiple commas with single comma
#         sanitized_row = [",".join([phone.strip() for phone in phones.split(",")]) if isinstance(phones, str) else phones
#                          for phones in row]
#
#         # write the sanitized row to the output file
#         writer.writerow(sanitized_row)


import csv

# Open the input and output files
with open('output.csv', 'r') as input_file, open('cleanedoutput.csv', 'w', newline='') as output_file:

    # Create a CSV reader and writer objects
    reader = csv.reader(input_file)
    writer = csv.writer(output_file)

    # Loop through each row in the input file
    for row in reader:
        # Remove consecutive commas in the phone number field
        row[1] = ",".join(filter(None, row[1].split(",")))

        # Write the sanitized row to the output file
        writer.writerow(row)
