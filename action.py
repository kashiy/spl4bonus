import atexit
import sys
import sqlite3

conn = sqlite3.connect('moncafe.db')


def _close_db():
    conn.commit()
    conn.close()


atexit.register(_close_db)


def actionMain(args):
    filepath = args[2]

    with open(filepath) as fp:
        for line in fp:
            word = line.strip().split(", ")
            product_id_a = word[0]
            quantity_a = word[1]
            activator_id_a = word[2]
            date_a = word[3]

            if quantity_a > 0:  # supply
                insert_Activities(product_id_a, quantity_a, activator_id_a, date_a)
                conn.execute("""UPDATE Products SET quantity=quantity+""" + quantity_a+ """ WHERE id="""+product_id_a)

            elif quantity_a < 0:  # sell
                conn.execute("""SELECT Products.quantity FROM Products WHERE id="""+quantity_a)
                quantity_Of_product = conn.fetchone()
                if quantity_a <= quantity_Of_product:
                    conn.execute("""UPDATE Products SET quantity=quantity-""" + quantity_a+ """WHERE id="""+product_id_a)
                    insert_Activities(product_id_a, quantity_a, activator_id_a, date_a)
                    price=conn.execute("""SELECT Products.price FROM Products WHERE id="""+product_id_a)
                    conn.execute("""UPDATE sales SET sum_sales=sum_sales+""" + quantity_a*-1*price+ """WHERE id="""+product_id_a)


if __name__ == '__main__':
    actionMain(sys.argv)


def insert_Activities(product_id, quantity, activator_id, date):
    conn.execute("""
        INSERT INTO Activities (product_id, quantity ,activator_id,date) VALUES (?, ? , ?,?)
    """, [product_id, quantity, activator_id, date])