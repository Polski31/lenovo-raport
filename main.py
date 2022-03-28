import csv
import sys
import product

source_file = (sys.argv[len(sys.argv) - 1])
products = []


def read_file():
    with open(source_file, newline='\n') as csvfile:
        reader = csv.reader(csvfile, delimiter='\n')
        for row in reader:
            if len(row) == 1:
                products.append(product.Product(row[0]))
            if len(row) == 2:
                products.append(product.Product(row[0], row[1]))


def write_result():
    result_file = "products.csv"
    with open(result_file, 'w', newline='\n') as csvfile:
        fieldnames = ['MTM', 'SN']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()
        for p in products:
            writer.writerow({'MTM': p.machine_type_model, 'SN': p.serial_number})


read_file()
write_result()
