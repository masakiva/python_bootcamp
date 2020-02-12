def ft_reduce(function_to_apply, list_of_inputs):
    if len(list_of_inputs) == 1:
        return list_of_inputs[0]
    ret = function_to_apply(list_of_inputs[0], list_of_inputs[1])
    for elem in list_of_inputs[2:]:
        ret = function_to_apply(elem, ret)
    return ret

from functools import reduce
product = ft_reduce((lambda x, y: x * y), [4, 4, 4, 4])
print(product)


def big(x, y):
    if len(x) > len(y):
        return(x)
    else:
        return(y)

l = ["basile", "vim", "quarante-deux"]
print(ft_reduce(big, l))
