from repository import repo
import dto
import dao


def printdb():


    print_table_as_a_table("Activities", "Activities.date")
    print_table_as_a_table("Coffee_stands", "Coffee_stands.id")
    print_table_as_a_table("Employees", "Employees.id")
    print_table_as_a_table("Products", "Products.id")
    print_table_as_a_table("Suppliers", "Suppliers.id")


if __name__ == '__main__':
    printdb()


def print_table_as_a_table(table_name, mylist):

    print("\n{}\n".format(table_name))
    for item in mylist:
        print(item)  ##todo str(item)

def employees_report():
    conn.execute("""SELECT Employees.name, Employees.salary,Coffee_stands.location sales.sum_sales FROM 
    (Employees left inner join Coffee_stands on Employees.coffee_stand=Coffee_stands.id) left inner join sales on Employees.id=sales.id_employee""")
    mylist = conn.fetchAll()
    print("Employees report\n")
    for item in mylist:
        print(item)  ##todo str(item)