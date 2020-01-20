




def _close_db():
    conn.commit()
    conn.close()


atexit.register(_close_db)


def main(args):
    conn.executescript("""
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

    filepath = args[2]

    with open(filepath) as fp:
        for line in fp:
            word = line.strip().split(", ")
            if (word[0] == "E"):
                insert_Employee(word[1], word[2], word[3], word[4])
            elif (word[0] == "S"):
                insert_Supplier(word[1], word[2], word[3])
            elif (word[0] == "P"):
                insert_Product(word[1], word[2], word[3])
            elif (word[0] == "C"):
                insert_Coffee_stand(word[1], word[2], word[3])


if __name__ == '__main__':
    main(sys.argv)


def insert_Employee(id, name, salary, coffee_stand):
    conn.execute("""
        INSERT INTO Employees (id, name ,salary,coffee_stand) VALUES (?, ? , ?, ?)
    """, [id, name, salary, coffee_stand])
    conn.execute("""
            INSERT INTO sales (id,0) VALUES (?)
        """, [id])


def insert_Supplier(id, name, contact_information):
    conn.execute("""
        INSERT INTO Suppliers (id, name ,contact_information) VALUES (?, ? , ?)
    """, [id, name, contact_information])


def insert_Product(id, description, price):
    conn.execute("""
        INSERT INTO Products (id, description ,price) VALUES (?, ? , ?)
    """, [id, description, price])


def insert_Coffee_stand(id, location, number_of_employees):
    conn.execute("""
        INSERT INTO Coffee_stands (id, location ,number_of_employees) VALUES (?, ? , ?)
    """, [id, location, number_of_employees])