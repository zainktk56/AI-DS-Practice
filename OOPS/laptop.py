class Laptop:
    def __init__(self, brand, processor, generation, ram, storage):
        self.brand = brand
        self.processor = processor
        self.genetration = generation  # Note: minor typo here in your original code ("genetration")
        self._ram = ram  #Protected
        self.storage = storage

    def show_configuration(self):
        return f"""Brand: {self.brand}
                Processor: {self.processor}
                Generation: {self.genetration}
                RAM: {self._ram}
                STORAGE: {self.storage}"""

    def run_code(self):
        return "Code is working fine!"


    def get_ram(self):
     return {self._ram}

    def set_ram(self,new_ram):     
        if new_ram>64:
            return f"{new_ram} gb is not supported "   
        else:
            self._ram = new_ram
