class Employee:
    def __init__(self, id, name, salary, coffee_stand):
        self.id = id
        self.name = name
        self.salary = salary
        self.coffee_stand = coffee_stand

    def __str__(self):
        return str("({}, {}, {}, {})".format(self.id, self.name, self.salary, self.coffee_stand))


class Supplier:
    def __init__(self, id, name, contact_information):
        self.id = id
        self.name = name
        self.contact_information = contact_information

    def __str__(self):
        return str("({}, {}, {})".format(self.id, self.name, self.contact_information))


class Product:
    def __init__(self, id, description, price, quantity):
        self.id = id
        self.description = description
        self.price = price
        self.quantity = quantity

    def __str__(self):
        return str("({}, {}, {}, {})".format(self.id, self.description, self.price, self.quantity))


class Coffee_stand:
    def __init__(self, id, location, number_of_employees):
        self.id = id
        self.location = location
        self.number_of_employees = number_of_employees

    def __str__(self):
        return str("({}, {}, {})".format(self.id, self.location, self.number_of_employees))

class Activitie:
    def __init__(self, product_id, quantity, activator_id, date):
        self.product_id = product_id
        self.quantity = quantity
        self.activator_id = activator_id
        self.date = date

    def __str__(self):
        return str("({}, {}, {}, {})".format(self.product_id, self.quantity, self.activator_id, self.date))

class sale:
    def __init__(self, id_employee, sum_sales):
        self.id_employee = id_employee
        self.sum_sales = sum_sales
