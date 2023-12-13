import csv
from collections import defaultdict

def split_csv(input_file, column_index):
    data_dict = defaultdict(list)
    
    with open(input_file,'r') as file:
        reader = csv.reader(file)
        header = next(reader)

        for row in reader:
            print(row)
            value = row[column_index]
            data_dict[value].append(row)

        for value, rows in data_dict.items():
            output_file = f'{header[column_index]}_{value}.csv'
            with open(output_file, 'w') as csvfile:
                writer = csv.writer(csvfile)
                writer.writerow(header)
                writer.writerows(rows)

split_csv('/home/ubuntu/Downloads/ap_ssid_status_20230822_103752.csv',3)

