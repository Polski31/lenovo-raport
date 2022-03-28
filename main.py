import csv
import sys
import product
from rest import get_base_info, get_machine_type_model

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


def update_mtms():
    for p in products:
        p.update_machine_type_model(  # updates mtm of product in productList
            get_machine_type_model(  # gets mtm from json
                get_base_info(p)))  # gets json info about product


read_file()
update_mtms()
write_result()
