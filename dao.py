import sqlite3


class Employees:
    def __init__(self, conn):
        self._conn = conn

    def insert(self, employee):
        self._conn.execute("""
                INSERT INTO Employees (id, name ,salary,coffee_stand) VALUES (?, ? , ?, ?)
            """, [employee.id, employee.name, employee.salary, employee.coffee_stand])


"""
    def find(self, student_id):
        c = self._conn.cursor()
        c.execute(
            #SELECT id, name FROM students WHERE id = ?
        , [student_id])
        return Student(*c.fetchone())
"""


class Suppliers:
    def __init__(self, conn):
        self._conn = conn

    def insert(self, supplier):
        self._conn.execute("""
                INSERT INTO Suppliers (id, name ,contact_information) VALUES (?, ? , ?)
            """, [supplier.id, supplier.name, supplier.contact_information])


class Products:
    def __init__(self, conn):
        self._conn = conn

    def insert(self, product):
        self._conn.execute("""
                INSERT INTO Products (id, description ,price) VALUES (?, ? , ?)
            """, [product.id, product.description, product.price])


class Coffee_stands:
    def __init__(self, conn):
        self._conn = conn

    def insert(self, coffee_stand):
        self._conn.execute("""
                INSERT INTO Coffee_stands (id, location ,number_of_employees) VALUES (?, ? , ?)
            """, [coffee_stand.id, coffee_stand.location, coffee_stand.number_of_employees])


class Activities:
    def __init__(self, conn):
        self._conn = conn

    def insert(self, activitie):
        self._conn.execute("""
                INSERT INTO Activities (product_id, quantity ,activator_id,date) VALUES (?, ? , ?,?)
            """, [activitie.product_id, activitie.quantity, activitie.activator_id, activitie.date])


class Sales:
    def __init__(self, conn):
        self._conn = conn

    def insert(self, sale):
        self._conn.execute("""
            INSERT INTO sales (id,0) VALUES (?)
        """, [sale.id])
