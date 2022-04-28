from products.product import Product


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
