import sqlite3
import dto


class Employees:
    def __init__(self, conn):
        self._conn = conn

    def insert(self, employee):
        self._conn.execute("""
                INSERT INTO Employees (id, name ,salary,coffee_stand) VALUES (?, ? , ?, ?)
            """, [employee.id, employee.name, employee.salary, employee.coffee_stand])

    def find_all(self,orderby):
        c = self._conn.cursor()
        all = c.execute("""
            SELECT id, name, salary, coffee_stand FROM Employees ORDER BY ?
        """, [orderby]).fetchall()

        return [dto.Employee(*row) for row in all]

class Suppliers:
    def __init__(self, conn):
        self._conn = conn

    def insert(self, supplier):
        self._conn.execute("""
                INSERT INTO Suppliers (id, name ,contact_information) VALUES (?, ? , ?)
            """, [supplier.id, supplier.name, supplier.contact_information])

    def find_all(self, orderby):
        c = self._conn.cursor()
        all = c.execute("""
            SELECT id, name, contact_information FROM Suppliers ORDER BY ?
        """, [orderby]).fetchall()

        return [dto.Supplier(*row) for row in all]

class Products:
    def __init__(self, conn):
        self._conn = conn

    def insert(self, product):
        self._conn.execute("""
                INSERT INTO Products (id, description ,price, quantity) VALUES (?, ? , ?, ?)
            """, [product.id, product.description, product.price, product.quantity])

    def find(self, product_id):
        c = self._conn.cursor()
        c.execute("""
                SELECT Products.id, Products.description, Products.price, Products.quantity FROM Products WHERE id = ?
            """, [product_id])

        return dto.Product(*c.fetchone())

    def update_quantity(self,product_id,quantity):
        self._conn.execute("""
                UPDATE Products SET quantity=quantity+? + WHERE id = ?
                """, [quantity,product_id])

    def find_all(self,orderby):
        c = self._conn.cursor()
        all = c.execute("""
            SELECT id, description, price, quantity FROM Products ORDER BY ?
        """, [orderby]).fetchall()

        return [dto.Product(*row) for row in all]

class Coffee_stands:
    def __init__(self, conn):
        self._conn = conn

    def insert(self, coffee_stand):
        self._conn.execute("""
                INSERT INTO Coffee_stands (id, location ,number_of_employees) VALUES (?, ? , ?)
            """, [coffee_stand.id, coffee_stand.location, coffee_stand.number_of_employees])

    def find_all(self,orderby):
        c = self._conn.cursor()
        all = c.execute("""
            SELECT id, location, number_of_employees FROM Coffee_stands ORDER BY ?
        """, [orderby]).fetchall()

        return [dto.Coffee_stand(*row) for row in all]

class Activities:
    def __init__(self, conn):
        self._conn = conn

    def insert(self, activitie):
        self._conn.execute("""
                INSERT INTO Activities (product_id, quantity ,activator_id,date) VALUES (?, ? , ?,?)
            """, [activitie.product_id, activitie.quantity, activitie.activator_id, activitie.date])


    def find_all(self,orderby):
        c = self._conn.cursor()
        all = c.execute("""
            SELECT product_id, quantity, activator_id, date FROM Activities ORDER BY ?
        """, [orderby]).fetchall()

        return [dto.Activitie(*row) for row in all]

class Sales:
    def __init__(self, conn):
        self._conn = conn

    def insert(self, sale):
        self._conn.execute("""
            INSERT INTO sales (id,0) VALUES (?)
        """, [sale.id])

    def update_quantity(self, product_id, amount):
        self._conn.execute("""
                UPDATE sales SET sum_sales=sum_sales+? WHERE id= ?
                """, [amount, product_id])
