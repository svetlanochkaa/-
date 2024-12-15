def calculate_structure_sum(*args):
    total_sum = 0
    for element in args:
        if isinstance(element, (list, tuple, set)):
            total_sum += calculate_structure_sum(*element)
        elif isinstance(element, dict):
            total_sum += calculate_structure_sum(*element.keys(), *element.values())
        elif isinstance(element, str):
            total_sum += len(element)
        elif isinstance(element, (int, float)):
            total_sum += element
    return total_sum

data_structure =[ [1, 2, 3], {'a': 4, 'b': 5}, (6, {'cube': 7, 'drum': 8}), "Hello", ((), [{(2, 'Urban', ('Urban2', 35))}])]
result = calculate_structure_sum(*data_structure)
print(result)
