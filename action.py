import sys

from repository import repo
import dto
import printdb


def actionMain(args):
    filepath = args[1] ## todo change to 2

    with open(filepath) as fp:
        for line in fp:
            word = line.strip().split(", ")
            product_id_a = word[0]
            quantity_a = word[1]
            quantity_a = int(quantity_a)
            activator_id_a = word[2]
            date_a = word[3]


            if quantity_a > 0:  # supply
                repo.Activities.insert(dto.Activitie(product_id_a, quantity_a, activator_id_a, date_a))
                repo.Products.update_quantity(product_id_a, quantity_a)

            elif quantity_a < 0:  # sell
                product = repo.Products.find(product_id_a)
                quantity_of_product = product.quantity
                if quantity_a <= quantity_of_product:
                    ## todo quantity is negative.. check if we subtract
                    repo.Products.update_quantity(product_id_a, quantity_a)
                    repo.Activities.insert(dto.Activitie(product_id_a, quantity_a, activator_id_a, date_a))
                    price = product.price
                    repo.Sales.update_quantity(product_id_a, quantity_a * -1 * price)
                    repo.Sales.update_quantity(product_id_a, quantity_a * -1 * price)

    printdb.printdb()


if __name__ == '__main__':
    actionMain(sys.argv)
