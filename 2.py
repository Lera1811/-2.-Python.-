#Задача 2. Выведите таблицу истинности для выражения ¬(X ∧ Y) ∨ Z.

#x = [0 , 1]
#y = [0 , 1]
#z = [0 , 1]

print('x y z')
for x in range(0 , 2):
  for y in range(0 , 2):
    for z in range(0 , 2):
      if (not(x) and y  or z)
        print(x, y, z)
