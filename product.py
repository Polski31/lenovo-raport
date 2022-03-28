class Product:
    def __init__(self, serial_number, machine_type_model="EMPTY"):
        self.serial_number = str(serial_number)
        self.machine_type_model = machine_type_model

    def update_machine_type_model(self, machine_type_model):
        self.machine_type_model = machine_type_model

    def __str__(self):
        return "MTM:{} SN:{}".format(self.machine_type_model, self.serial_number)


class ProductList:
    product_list = []

    def add_product(self, product: Product):
        self.product_list.append(product)

    def find_product(self, sn):
        return (product for product in self.product_list if sn == product.serial_number)

    def get_product(self, index):
        if 0 < index < len(self.product_list):
            return self.product_list[index]
        else:
            return None
