import numpy as np

#function for power iteration method

def power_method(matrix, x=None, tolerance=0.001, max_iter=1000):
    def abs_max_elem(vec):
        largest = vec[0]
        for i in range(len(vec)):
            if largest < abs(vec[i]):
                largest = vec[i]
        return largest

    def dot(matrix_, vec):
        ans = []
        for i in range(len(matrix_)):
            ans.append(sum(matrix_[i][j] * vec[j] for j in range(len(matrix_))))
        return ans

    def max_elem(vec):
        largest = vec[0]
        for i in range(len(vec)):
            if largest < vec[i]:
                largest = vec[i]
        return largest

    if x is None: x = np.ones(len(matrix))
    count = 0
    lambda_1 = 0
    while count < max_iter:
        x_new = dot(matrix, x)
        lambda_1_new = abs_max_elem(x_new)
        x_new = x_new / max_elem(x_new)
        deviation = x - x_new
        x = x_new
        if abs(lambda_1_new - lambda_1) < tolerance:
            break
        lambda_1 = lambda_1_new
    return lambda_1_new, x

# reading the file in a matrix
matrix = []
with open("mstrimat.txt", "r") as datafile:
    for line in datafile.readlines():
        # print(line.split("  "))
        elems = list(map(lambda x: int(x.strip()), line.split("  ")))
        matrix.append(elems)

original_matrix = matrix

# calculation of the largest eigen value
val, vec = power_method(matrix)
if np.allclose(np.dot(matrix, vec), val*vec, atol=0.01):
    print("\nLargest eigen value and the corresponding eigen vector")
    print(val, vec)

# calculation of the second largest eigen value
vec = vec/np.linalg.norm(vec)
vec = np.array([vec])
matrix = matrix - val*np.outer(vec, vec)
val, vec = power_method(matrix)

if np.allclose(np.dot(original_matrix, vec), val*vec, atol=0.01):
    print("\nSecond largest eigen value and the corresponding eigen vector")
    print(val, vec)

# comparing with equations provided in the question
def val_exp(k):
    return 2 + 2*np.cos(k*np.pi/6)

def vec_exp(k):
    v = []
    for i in range(5):
        v.append(2*np.sin(i*k*np.pi/6))
    return v


def dot(matrix_, vec):
    ans = []
    for i in range(len(matrix_)):
        ans.append(sum(matrix_[i][j] * vec[j] for j in range(len(matrix_))))
    return ans

print("\nThe values generated from the expression are")
for i in range(1, 6):
    print(val_exp(i), vec_exp(i))
    if not np.allclose(dot(original_matrix, vec_exp(i)), list(map(lambda x: val_exp(i)*x, vec_exp(i))), atol=0.1):
        print(f"\nThe values from expression for k={i} do not follow Mv = ev")


# ********************output*******************************

# Largest eigen value and the corresponding eigen vector
# 3.7330929418323073 [ 0.50048352 -0.86630456  1.         -0.86630456  0.50048352]

# Second largest eigen value and the corresponding eigen vector
# 1.999860777173622 [ 1.00000000e+00  5.39477390e-04 -1.00086963e+00  5.39477390e-04
#   1.00000000e+00]

# The values generated from the expression are
# 3.7320508075688776 [0.0, 0.9999999999999999, 1.7320508075688772, 2.0, 1.7320508075688774]

# The values from expression for k=1 do not follow Mv = ev
# 3.0 [0.0, 1.7320508075688772, 1.7320508075688774, 2.4492935982947064e-16, -1.732050807568877]

# The values from expression for k=2 do not follow Mv = ev
# 2.0 [0.0, 2.0, 2.4492935982947064e-16, -2.0, -4.898587196589413e-16]

# The values from expression for k=3 do not follow Mv = ev
# 1.0000000000000004 [0.0, 1.7320508075688774, -1.732050807568877, -4.898587196589413e-16, 1.7320508075688783]

# The values from expression for k=4 do not follow Mv = ev
# 0.2679491924311226 [0.0, 0.9999999999999999, -1.7320508075688772, 2.0, -1.7320508075688774]

# The values from expression for k=5 do not follow Mv = ev