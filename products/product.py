class Product:
    def __init__(self, serial_number, machine_type_model="EMPTY"):
        self.serial_number = str(serial_number)
        self.machine_type_model = machine_type_model

    def update_machine_type_model(self, machine_type_model):
        self.machine_type_model = machine_type_model

    def __str__(self):
        return "MTM:{} SN:{}".format(self.machine_type_model, self.serial_number)


class ProductList:
    __product_list = []

    def add_product(self, product: Product):
        self.__product_list.append(product)

    def find_product(self, sn):
        return (product for product in self.__product_list if sn == product.serial_number)

    def get_product(self, index):
        if 0 < index < len(self.__product_list):
            return self.__product_list[index]
        else:
            return None

    def get_product_list(self):
        return self.__product_list
