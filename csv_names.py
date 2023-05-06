import os
import csv

csv_folder = 'dataset/'
txt_file = 'heads.txt'
with open(txt_file, 'w') as output_file:
    # Iterate over all CSV files in the folder
    for filename in os.listdir(csv_folder):
        if filename.endswith('.csv'):
            csv_path = os.path.join(csv_folder, filename)
            # Write the CSV filename (without extension) to the output file
            output_file.write(os.path.splitext(filename)[0] + '\n')
            # Read the CSV file and write the column headers to the output file
            with open(csv_path, 'r') as csv_file:
                reader = csv.reader(csv_file)
                headers = next(reader)
                output_file.write(','.join(headers) + '\n')
                output_file.write('\n')