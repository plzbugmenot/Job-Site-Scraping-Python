import json
import pandas as pd
import os
from src.file1 import process_file1
from src.file2 import process_file2
from src.file3 import process_file3
from src.file4 import process_file4

def create_data_directory():
    if not os.path.exists('data'):
        os.makedirs('data')

def get_all_data():
    # Create data directory
    create_data_directory()
    
    # Run all processing functions
    data1 = process_file1()
    data2 = process_file2()
    data3 = process_file3()
    data4 = process_file4()
    
    # Read from JSON files to verify data
    with open('1.json', 'r') as f:
        data1 = json.load(f)
    with open('2.json', 'r') as f:
        data2 = json.load(f)
    with open('3.json', 'r') as f:
        data3 = json.load(f)
    with open('4.json', 'r') as f:
        data4 = json.load(f)
    
    # Combine all data
    all_data = data1 + data2 + data3 + data4
    return all_data

def remove_duplicates(data):
    df = pd.DataFrame(data)
    df_unique = df.drop_duplicates(subset=['link'])    
    return df_unique


def save_to_excel(df, output_path):
    # Save DataFrame to Excel
    df.to_excel(output_path, index=False)

def save_processed_data(clean_data):
    # Save as JSON
    with open('total_data.json', 'w', encoding='utf-8') as json_file:
        json.dump(clean_data.to_dict('records'), json_file, indent=4)

def main():
    # Get data from all files
    all_data = get_all_data()
    
    # Remove duplicates
    clean_data = remove_duplicates(all_data)

    save_processed_data(clean_data)
    save_to_excel(clean_data, 'processed_data.xlsx')

    print(f"\n✨ Data has been processed and saved to processed_data.xlsx")

if __name__ == "__main__":
    main()
