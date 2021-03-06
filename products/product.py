class Product:
    def __init__(self, serial_number, machine_type_model="EMPTY"):
        self.serial_number = str(serial_number)
        self.machine_type_model = machine_type_model

    def update_machine_type_model(self, machine_type_model):
        self.machine_type_model = machine_type_model

    def __str__(self):
        return "MTM:{} SN:{}".format(self.machine_type_model, self.serial_number)