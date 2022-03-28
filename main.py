import argparse
import csv

import product
from rest import get_base_info, get_machine_type_model

arg_parser = argparse.ArgumentParser()
arg_parser.add_argument("source", help="path to source csv file with SN(s)")
arg_parser.add_argument("destination", help="path to destination csv file with SN(s) and MTM(s)")
args = arg_parser.parse_args()

source_file = args.source
destination_file = args.destination
products = product.ProductList()


def read_file():
    with open(source_file, newline='\n') as csvfile:
        reader = csv.reader(csvfile, delimiter='\n')
        for row in reader:
            if len(row) == 1:
                products.add_product(product.Product(row[0]))
            if len(row) == 2:
                products.add_product(product.Product(row[0], row[1]))


def write_result():
    with open(destination_file, 'w', newline='\n') as csvfile:
        fieldnames = ['MTM', 'SN']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()
        for p in products.get_product_list():
            writer.writerow({'MTM': p.machine_type_model, 'SN': p.serial_number})


def update_mtms():
    for p in products.get_product_list():
        p.update_machine_type_model(  # updates mtm of product in productList
            get_machine_type_model(  # gets mtm from json
                get_base_info(p)))  # gets json info about product


if __name__ == '__main__':
    read_file()
    update_mtms()
    write_result()
