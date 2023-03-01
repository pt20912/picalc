import decimal
import time
import matplotlib.pyplot as plt
from tqdm import tqdm

def pi_bbp(n_digits):
    decimal.getcontext().prec = n_digits + 1
    pi = decimal.Decimal(0)
    pi_values = []
    times = []
    iterations = []
    for k in tqdm(range(n_digits)):
        start_time = time.time()
        pi += (decimal.Decimal(1)/(16**k))*((decimal.Decimal(4)/(8*k+1))-(decimal.Decimal(2)/(8*k+4))-(decimal.Decimal(1)/(8*k+5))-(decimal.Decimal(1)/(8*k+6)))
        end_time = time.time()
        times.append(end_time - start_time)
        pi_values.append(float(str(pi)[2:]))
        iterations.append(k)

    # Final progress and time plot
    plt.clf()
    plt.plot(iterations, times, color='orange')
    plt.title("Time per Iteration")
    plt.xlabel("Iteration")
    plt.ylabel("Time (s)")
    plt.show()

    return pi

n_digits = int(input("Enter the number of digits after the decimal point for pi: "))
pi = pi_bbp(n_digits)
print("Pi with {0} digits after the decimal point is: {1:.{2}f}".format(n_digits, pi, n_digits))
