class Employee:
    def __init__(self, id, name, salary, coffee_stand):
        self.id = int(id)
        self.name = name
        self.salary = float(salary)
        self.coffee_stand = int(coffee_stand)

    def __str__(self):
        return str((self.id, self.name, self.salary, self.coffee_stand))


class Supplier:
    def __init__(self, id, name, contact_information):
        self.id = int(id)
        self.name = name
        self.contact_information = contact_information

    def __str__(self):
        return str((self.id, self.name, self.contact_information))


class Product:
    def __init__(self, id, description, price, quantity):
        self.id = int(id)
        self.description = description
        self.price = float(price)
        self.quantity = int(quantity)

    def __str__(self):
        return str((self.id, self.description, self.price, self.quantity))


class Coffee_stand:
    def __init__(self, id, location, number_of_employees):
        self.id = int(id)
        self.location = location
        self.number_of_employees = int(number_of_employees)

    def __str__(self):
        return str((self.id, self.location, self.number_of_employees))

class Activitie:
    def __init__(self, product_id, quantity, activator_id, date):
        self.product_id = int(product_id)
        self.quantity = int(quantity)
        self.activator_id = int(activator_id)
        self.date = date

    def __str__(self):
        return str((self.product_id, self.quantity, self.activator_id, self.date))

class sale:
    def __init__(self, id_employee, sum_sales):
        self.id_employee = int(id_employee)
        self.sum_sales = float(sum_sales)

    def __str__(self):
        return str((self.id_employee,  self.sum_sales))