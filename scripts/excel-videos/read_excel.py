import pandas as pd

# Path to the Excel file
excel_file = 'Liste aller Juggervideos _ JuggerTube.xlsx'

# Read all sheets from the Excel file
excel = pd.ExcelFile(excel_file)

# Get list of sheet names
sheet_names = excel.sheet_names

# Iterate through each sheet
for sheet_name in sheet_names:
    print(f"\n{'='*50}")
    print(f"Sheet: {sheet_name}")
    print('='*50)
    
    # Read the sheet into a DataFrame
    df = pd.read_excel(excel_file, sheet_name=sheet_name)
    
    # Print column headers
    print("\nColumns:")
    for col in df.columns:
        print(f"- {col}")
    
    # Print first 3 rows
    print("\nFirst 3 rows:")
    print(df.head(3).to_string())
    
print("\nAnalysis complete!") 