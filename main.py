from bigo.bigo import BigO

n = 10
big_o = BigO()

print(big_o.logarithmic_time()(n))      # Output: 3
print(big_o.linear_time()(n))           # Output: 10
print(big_o.quadratic_time()(n))        # Output: 100
print(big_o.exponential_time()(n))      # Output: 1024
print(big_o.factorial_time()(n))        # Output: 3628800