import csv

from products import product


def read_file(file, products):
    with open(file, newline='\n') as csvfile:
        reader = csv.reader(csvfile, delimiter='\n')
        for row in reader:
            if len(row) == 1:
                products.add_product(product.Product(row[0]))
            if len(row) == 2:
                products.add_product(product.Product(row[0], row[1]))


def write_result(file, products):
    with open(file, 'w', newline='\n') as csvfile:
        fieldnames = ['MTM', 'SN']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()
        for p in products.get_product_list():
            writer.writerow({'MTM': p.machine_type_model, 'SN': p.serial_number})