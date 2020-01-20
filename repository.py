import atexit
import sys
import sqlite3
import dao


class _repository:
    def __init__(self):
        self._conn = sqlite3.connect('moncafe.db')
        self.Employees = dao.Employees(self._conn)
        self.Suppliers =dao.Suppliers(self._conn)
        self.Products = dao.Products(self._conn)
        self.Coffee_stands = dao.Coffee_stands(self._conn)
        self.Activities = dao.Activities(self._conn)
        self.sales = dao.Sales(self._conn)

    def _close(self):
        self._conn.commit()
        self._conn.close()

    def create_tables(self):
        self._conn.executescript("""
                CREATE TABLE Employees (
                    id      INTEGER         PRIMARY KEY,
                    name    TEXT        NOT NULL,
                    salary  REAL         NOT NULL,
                    coffee_stand INTEGER REFERENCES Coffee_stands(id)

                );

                CREATE TABLE Suppliers (
                    id      INTEGER         PRIMARY KEY,
                    name    TEXT        NOT NULL,
                    contact_information    TEXT

                );

                CREATE TABLE Products (
                    id  INTEGER PRIMARY KEY
                    description     TEXT        NOT NULL
                    price           REAL        NOT NULL
                    quantity        INTEGER     NOT NULL
                );

                CREATE TABLE Coffee_stands (
                    id INTEGER PRIMARY KEY
                    location TEXT NOT NULL
                    number_of_employees INTEGER
                );

                CREATE TABLE Activities (
                    product_id INTEGER REFERENCES Products(id)
                    quantity INTEGER NOT NULL
                    activator_id INTEGER NOT NULL
                    date DATE NOT NULL
                );


                    CREATE TABLE sales (
                    id_employee      INTEGER    PRIMARY KEY REFERENCES Employees(id),
                    sum_sales       INTEGER


            """)
