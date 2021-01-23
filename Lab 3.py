'''
# Problem 1:
import lab02solutions
if __name__ == "__main__":
    lab02solutions.initialize()
    lab02solutions.add(42)
    lab02solutions.subtract(2)
    lab02solutions.multiply(2)
    lab02solutions.divide(8)
    if lab02solutions.get_current_value() == 10:
        print ("Test passed")
    else:
        print ("Test failed")

'''
'''
# Problem 2:
def sum_cubes(n):
    temp = 0
    for i in range(1, n + 1):
        temp += i**3
    return temp
def sum_formula(n):
    temp_1 = 0
    for j in range(1, n + 1):
        temp_1 += j
    temp_2 = temp_1 ** 2
    return temp_2
def check_sum(n):
    if (sum_cubes(n) == sum_formula(n)):
        return True
    else:
        return False
def check_sums_up_to_n(N):
    count = 0
    for k in range(1, N+1):
        if check_sum(k) == True:
            count += 1
        else:
            return False
    if (count == N):
        return True
    else:
        return False

'''

#Problem 3:
final_sum = 0
for a in range(1001):
    if (a % 2 == 0):
        numerator = 1
    else:
        numerator = -1
    denominator = 2*a + 1
    term = numerator/denominator
    final_sum += term
pi_approx = 4 * final_sum
print(pi_approx)
