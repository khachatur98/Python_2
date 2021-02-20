a =  [1, 4, 5, 7, 8, -2, 0, -1]
print(a[3], a[5])
a_sorted = sorted(a, reverse = True)
print(a_sorted[1:4])
print(a_sorted[2:7])
del(a_sorted[2:4])
print(a_sorted)

b = ["grapes", "Potatoes", "tomatoes", "Orange",
     "Lemon", "Broccoli", "Carrot", "Sausages"]

b_sorted = sorted(b, reverse = False)

c = a[1:4] + b[4:7]
print(c)