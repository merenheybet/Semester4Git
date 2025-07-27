def polynom_eval_horner(coeffs, x):
    result = 0
    for i in range(len(coeffs)):
        result += coeffs[i] * (x ** (len(coeffs) - 1 - i))
    return result

# print(polynom_eval_horner([2, 0, 5, 8], 2))

def row_sum_norm(A):
    result = float('-inf')
    y = len(A)
    x = len(A[0])
    for i in range(y):
        row_sum = 0
        for j in range(x):
            row_sum += abs(A[i][j])
        if row_sum > result:
            result = row_sum
    return result   

# print(row_sum_norm([[1, 2, 3], [4, 5, 6], [-7, 8, 9]]))

def mat_mult(A,B):
    n = len(A)
    result = []
    for i in range(n):
        row = []
        for j in range(n):
            sum_product = 0
            for k in range(n):
                sum_product += A[i][k] * B[k][j]
            row.append(sum_product)
        result.append(row)

    return result