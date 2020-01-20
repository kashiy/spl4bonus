import atexit
import sqlite3
import dao


class Repository:
    def __init__(self):
        self._conn = sqlite3.connect('moncafe.db')
        self.Employees = dao.Employees(self._conn)
        self.Suppliers = dao.Suppliers(self._conn)
        self.Products = dao.Products(self._conn)
        self.Coffee_stands = dao.Coffee_stands(self._conn)
        self.Activities = dao.Activities(self._conn)
        self.Sales = dao.Sales(self._conn)

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
                    id  INTEGER PRIMARY KEY,
                    description TEXT    NOT NULL,
                    price           REAL        NOT NULL,
                    quantity        INTEGER     NOT NULL
                );

                CREATE TABLE Coffee_stands (
                    id INTEGER PRIMARY KEY,
                    location TEXT NOT NULL,
                    number_of_employees INTEGER
                );

                CREATE TABLE Activities (
                    product_id INTEGER REFERENCES Products(id),
                    quantity INTEGER NOT NULL,
                    activator_id INTEGER NOT NULL,
                    date DATE NOT NULL
                );


                    CREATE TABLE Sales (
                    id_employee      INTEGER    PRIMARY KEY REFERENCES Employees(id),
                    sum_sales       INTEGER

                );
            """)

    def get_employees_reports(self):
        c = self._conn.cursor()
        all = c.execute("""
            SELECT Employees.name, Employees.salary ,Coffee_stands.location ,Sales.sum_sales 
            FROM (Employees left inner join Coffee_stands on Employees.coffee_stand=Coffee_stands.id) 
            left inner join sales on Employees.id=sales.id_employee ORDER BY Employees.name ASC
        """).fetchall()

        return [employees_report(*row) for row in all]

    def get_activities_reports(self):
        c = self._conn.cursor()
        all = c.execute("""
               SELECT Activities.date, Products.description, Activities.quantity, Employees.name, Suppliers.name 
               FROM ((Activities left outer join Products on Activities.product_id=Products.id) 
               left outer join Employees on Activities.activator_id=Employees.id) left outer join Suppliers on Activities.activator_id=Suppliers.id
               ORDER BY Activities.date DESC
           """).fetchall()

        return [activities_report(*row) for row in all]


class employees_report:
    def __init__(self, Employees_name, Employees_salary, Coffee_stands_location, Sales_sum_sales):
        self.Employees_name = Employees_name
        self.Employees_salary = Employees_salary
        self.Coffee_stands_location = Coffee_stands_location
        self.Sales_sum_sales = Sales_sum_sales

    def __str__(self):
        return str("{} {} {} {}".format(self.Employees_name, self.Employees_salary, self.Coffee_stands_location,
                                        self.Sales_sum_sales))


class activities_report:
    def __init__(self, Activities_date, Products_description, Activities_quantity, Employees_name, Suppliers_name):
        self.Activities_date = Activities_date
        self.Products_description = Products_description
        self.Activities_quantity = Activities_quantity
        self.Employees_name = Employees_name
        self.Suppliers_name = Suppliers_name

    def __str__(self):
        return str(
            "({}, {}, {}, {}, {})".format(self.Activities_date, self.Products_description, self.Activities_quantity,
                                          self.Employees_name, self.Suppliers_name))


repo = Repository()
atexit.register(repo._close)
