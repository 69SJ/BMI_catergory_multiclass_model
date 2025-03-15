import pandas as pd
import glob
import os

# Set the directory where your XPT files are located
directory = 'C:/Users/Wen Jun/Desktop/sch ml'  # Change this to your actual directory path

# Find all XPT files in the directory
xpt_files = glob.glob(os.path.join(directory, '*.xpt'))

for xpt_file in xpt_files:
    try:
        # Read the XPT file
        df = pd.read_sas(xpt_file, format='xport')
        
        # Define the CSV file name by replacing the .xpt extension with .csv
        csv_file = os.path.splitext(xpt_file)[0] + '.csv'
        
        # Save the DataFrame to CSV without the index
        df.to_csv(csv_file, index=False)
        print(f"Successfully converted {xpt_file} to {csv_file}")
    except Exception as e:
        print(f"Error converting {xpt_file}: {e}")
