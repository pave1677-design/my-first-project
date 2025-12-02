from prettytable import PrettyTable
import matplotlib.pyplot as diagram
receipt = PrettyTable()
receipt.field_names = ['№', 'product', 'price', 'quantity', 'finalprice']

products = []
pay = []

for i in range(3):
    product = input('enter product name: ')
    price = int(input('enter product price: '))
    quantity = int(input('enter product quantity: '))
    receipt.add_row([i+1, product, price, quantity, price * quantity])
    products.append(product)
    pay.append(price*quantity)
print(receipt)
# сборка и вывод диаграм
diagram.bar(products, pay, color='green')
diagram.show()
