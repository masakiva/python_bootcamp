def ft_reduce(function_to_apply, list_of_inputs):
    ret = function_to_apply(list_of_inputs[0], list_of_inputs[1])
    for elem in list_of_inputs[2:]:
        ret = function_to_apply(elem, ret)
    return ret

from functools import reduce
product = ft_reduce((lambda x, y: x * y), [4, 4, 4, 4])
print(product)
