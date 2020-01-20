import os

import sys

if os.path.exists('moncafe.db'):
    os.remove('moncafe.db')

from repository import repo
import dto


def main(args):
    repo.create_tables()

    filepath = args[1] ## todo change to 2
    with open(filepath) as fp:
        for line in fp:
            word = line.strip().split(", ")
            if word[0] == "E":
                repo.Employees.insert(dto.Employee(word[1], word[2], word[3], word[4]))
                repo.Sales.insert(dto.sale(word[1], 0))
            elif word[0] == "S":
                repo.Suppliers.insert(dto.Supplier(word[1], word[2], word[3]))
            elif word[0] == "P":
                repo.Products.insert(dto.Product(word[1], word[2], word[3], 0))
            elif word[0] == "C":
                repo.Coffee_stands.insert(dto.Coffee_stand(word[1], word[2], word[3]))


if __name__ == '__main__':
    main(sys.argv)
