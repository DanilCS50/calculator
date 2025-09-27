purchases = [
    ("apple", 3),
    ("banana", 2),
    ("apple", 4),
    ("orange", 1),
    ("banana", 5),
    ("apple", 1)
]
products = {}

for i in range(0, len(purchases)):
    j = 0
    products[purchases[i]] = purchases[j+1]
    j += 1

print(products)
# for k, v in products.items():     Почему выводит 6 раз banana 2?
#     print(k, v)