import time

class Fib:
    def __init__(self, num):
        self.num = num

    def fib_seq(self):
        return self.helper_fib_seq(self.num)

    def helper_fib_seq(self, n):
        if n == 0:
            return 0
        if n == 1:
            return 1
        return self.helper_fib_seq(n - 1) + self.helper_fib_seq(n - 2)


def time_fib(num):
    fib = Fib(num)
    t_start = time.perf_counter()
    print(f"Fib number({num}): {fib.fib_seq()}")
    t_end = time.perf_counter()
    t_elapsed = t_end - t_start

    print (f"Time elapsed (s): {t_elapsed} ")


def main():
    for n in range(5, 100, 5):
        time_fib(n)

main()
