# ------------------------------------------------------
# - timeit: - Get Execution Time Of Code By Running 1M Time And Give You Minimal Time
# -         - It Used For Performance By Testing All Functionality
# - timeit(stmt, setup, timer, number)
# - timeit(pass, pass, default, 1.000.000) Default Values
# -------------------------------------------------------
# - stmt: Code You Want To Measure The Execution Time
# - setup: Setup Done Before The Code Execution (Import Module Or Anything)
# - timer: The Timer Value
# - number: How Many Execution That Will Run
# -------------------------------------------------------




from timeit import * 

print(dir(timeit))


print(timeit("'taha' * 1000"))



#print(name * 1000)

print(timeit("name = 'taha'; name * 1000"))

# print(random.randint(0, 50))

print(timeit(stmt="random.randint(0, 50)", setup="import random"))

print(repeat(stmt="random.randint(0, 50)", setup="import random", repeat=4))






