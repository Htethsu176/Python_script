import csv

def split_csv(input_file, column_name):
    data_dict = {}

    with open(input_file, newline='') as file:
        reader = csv.DictReader(file)
        header = reader.fieldnames

        for row in reader:
            value = row[column_name]

            if value in data_dict:
                data_dict[value].append(row)
            else:
                data_dict[value] = [row]

        for value, rows in data_dict.items():
            output_file = f'{column_name}_{value}.csv'
            with open(output_file, 'w', newline='') as csvfile:
                writer = csv.DictWriter(csvfile, fieldnames = header)
                writer.writeheader()
                writer.writerows(rows)
def main():
    input_file = '/home/ubuntu/Downloads/ap_ssid_status_20230822_103752.csv'
    column_name = 'model'

    split_csv(input_file, column_name)
    
if __name__ == "__main__":
    main()
