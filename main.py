import argparse

from connection.rest import get_base_info, get_machine_type_model
from db.db import backup_products
from file_processing import read_file, write_result
from products import product_list

arg_parser = argparse.ArgumentParser()
arg_parser.add_argument("source", help="path to source csv file with SN(s)")
arg_parser.add_argument("destination", help="path to destination csv file with SN(s) and MTM(s)")
args = arg_parser.parse_args()

source_file = args.source
destination_file = args.destination
products = product_list.ProductList()


def update_mtms():
    for p in products.get_product_list():
        p.update_machine_type_model(  # updates mtm of product in productList
            get_machine_type_model(  # gets mtm from json
                get_base_info(p)))  # gets json info about product


if __name__ == '__main__':
    read_file(source_file, products)
    update_mtms()
    write_result(destination_file, products)
    backup_products(destination_file)
