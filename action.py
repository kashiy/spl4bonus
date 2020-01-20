import sys

from repository import repo
import dto
import dao


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
                repo.Activities.insert(dto.Activitie(product_id_a, quantity_a, activator_id_a, date_a))
                dao.Products.update_quantity(product_id_a, quantity_a)

            elif quantity_a < 0:  # sell
                product = dao.Products.find(product_id_a)
                quantity_Of_product = product.quantity
                if quantity_a <= quantity_Of_product:
                    ## todo quantity is negative.. check if we subtract
                    dao.Products.update_quantity(product_id_a, quantity_a)
                    repo.Activities.insert(dto.Activitie(product_id_a, quantity_a, activator_id_a, date_a))
                    price = product.price
                    dao.Sales.update_quantity(product_id_a, quantity_a * -1 * price)


if __name__ == '__main__':
    actionMain(sys.argv)
