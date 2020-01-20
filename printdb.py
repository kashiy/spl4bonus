from repository import repo
import dao


def printdb():
    print_table_as_a_table("Activities", dao.Activities.find_all("Activities.date"))
    print_table_as_a_table("Coffee_stands", dao.Coffee_stands.find_all("Coffee_stands.id"))
    print_table_as_a_table("Employees", dao.Employees.find_all("Employees.id"))
    print_table_as_a_table("Products", dao.Products.find_all("Products.id"))
    print_table_as_a_table("Suppliers", dao.Suppliers.find_all("Suppliers.id"))
    employees_report()
    activities_report()


if __name__ == '__main__':
    printdb()


def print_table_as_a_table(table_name, mylist):
    print("\n{}\n".format(table_name))
    for item in mylist:
        print(item)


def employees_report():
    mylist = repo.get_employees_reports()
    print("\n\nEmployees report\n")
    for item in mylist:
        print(item)


def activities_report():
    mylist = repo.get_activities_reports()
    print("\n\nActivities\n")
    for item in mylist:
        print(item)
