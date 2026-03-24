def evaluate_polynomial(poly_dict, x):
    result = 0
    for i in poly_dict:
        result += poly_dict[i] * (x ** i)
    return result

