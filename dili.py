def test(lst):
    result = {}
    for item in lst:
        result[item[0]] = item[1:]
    return result

students = [[1, 'Nirjal', 'V'], [2, 'Lula', 'V'], [3, 'Brian', 'VI'], [4, 'Lynne', 'VI'], [5, 'Zac', 'VII']]
print('\nOriginal list of lists:')
print(students)
print('\nConverted list to a dictionary:')
print(test(students))

