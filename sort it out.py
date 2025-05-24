import pandas as pd


def remove_duplicate_clients(file_path, sheet_name, client_column, output_file):
    # Load the spreadsheet
    df = pd.read_excel(file_path, sheet_name=sheet_name)

    # Identify duplicate client names
    duplicate_clients = df[client_column].value_counts()[df[client_column].value_counts() > 1].index

    # Remove rows where the client name appears more than once
    df_cleaned = df[~df[client_column].isin(duplicate_clients)]

    # Save the cleaned spreadsheet to a new file
    df_cleaned.to_excel(output_file, index=False)


# Define file paths and parameters
file_path = r'C:\Users\user\Desktop\mad\august.xlsx'
sheet_name = 'Sheet'
client_column = 'Customer name'
output_file = 'C:/Users/user/Desktop/autoclub2024.xlsx'

# Execute the function
remove_duplicate_clients(file_path, sheet_name, client_column, output_file)

# Output the path to the cleaned file
print(f"Cleaned file saved at: {output_file}")
