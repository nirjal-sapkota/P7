lst = ['Banana', 'Apple', 'Mango', 'Dragon Fruit', 'Kiwi']

print('Length of list', len(lst))
print("First Element", lst[0])
print('Last Element', lst[-1])

lst.append('Guava')
print('Updated List is ', lst)

lst.remove("Banana")
print('Updated List is ', lst)

lst.sort()
print('Sorted List ', lst)

lst.pop(1)
print('Updated List is ', lst)

lst.reverse()
print('Reversed ', lst)

print("Multiplication on list ", lst*2)

lst = lst[:3]
print('Sliced List is ', lst)

lst.clear()
print('Cleared list ', lst)