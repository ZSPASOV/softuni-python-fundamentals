class Catalogue:
    def __init__(self, name):
        self.name = name
        self.products = []
    def add_product(self, product):
        self.products.append(product)
    def get_by_letter(self, first_letter):
        returned_list = []
        self.first_letter = first_letter
        for i in self.products:
            if i[0] == self.first_letter:
                returned_list.append(i)
        return returned_list
    def __repr__(self):
        for_print = "\n".join(sorted(self.products))
        return f'Items in the {self.name} catalogue:\n{for_print}'

catalogue = Catalogue("Furniture")
catalogue.add_product("Sofa")
catalogue.add_product("Mirror")
catalogue.add_product("Desk")
catalogue.add_product("Chair")
catalogue.add_product("Carpet")
print(catalogue.get_by_letter("C"))
print(catalogue)



