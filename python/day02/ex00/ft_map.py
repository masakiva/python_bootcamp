def ft_map(function_to_apply, list_of_inputs):
    return (function_to_apply(i) for i in list_of_inputs)
    #for i in list_of_inputs:
    #    yield function_to_apply(i)

items = [1, 2, 3, 4, 5]
squared = ft_map(lambda x: x**2, items)

print(squared)
print(next(squared))
print(next(squared))
for n in squared:
    print(n)
