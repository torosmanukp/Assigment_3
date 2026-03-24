def evaluate_polynomial(poly_dict, x):
    result = 0
    for i in poly_dict:
        result += poly_dict[i] * (x ** i)
    return result

my_poly = {0: -10, 2: 3, 4: 1}

x1=2
x2=-1.5