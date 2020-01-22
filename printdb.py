from repository import repo


def print_table_as_a_table(table_name, mylist):
    print("{}".format(table_name))
    for item in mylist:
        print(item)


def employees_report():
    mylist = repo.get_employees_reports()
    print("\nEmployees report")
    for item in mylist:
        print(item)


def activities_report():
    mylist = repo.get_activities_reports()
    print("\nActivities")
    for item in mylist:
        print(item)


def printdb():
    print_table_as_a_table("Activities", repo.Activities.find_all())
    print_table_as_a_table("Coffee_stands", repo.Coffee_stands.find_all())
    print_table_as_a_table("Employees", repo.Employees.find_all())
    print_table_as_a_table("Products", repo.Products.find_all())
    print_table_as_a_table("Suppliers", repo.Suppliers.find_all())
    employees_report()
    activities_report()


if __name__ == '__main__':
    printdb()
