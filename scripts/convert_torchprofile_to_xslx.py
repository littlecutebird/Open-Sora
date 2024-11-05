import re
import sys
import csv

# Read the file
with open(sys.argv[1], 'r') as f:
    lines = f.readlines()

# Parse the lines
data = []
for line in lines:
    # Use regular expression to split by whitespace
    columns = re.split(r'\s{2,}', line.strip())
    data.append(columns)

# Write to CSV
output_file = sys.argv[2]
with open(output_file, mode='w', newline='') as file:
    writer = csv.writer(file)
    # Write each row to the CSV file
    for row in data:
        writer.writerow(row)

print(f"Data has been written to {output_file}")