from math import floor, ceil, sqrt, log, exp
import random as rnd
import matplotlib.pyplot as plt 


def load():
    file = open("data_ex4.csv", "r")
    values = [float(x) for x in file.readlines()]
    return values

def mean(values):
    tot = 0
    for i in values:
        tot += i
    return tot / len(values)

def std_dev(values, mean):
    tot = 0
    for i in values:
        tot += (i - mean) ** 2
    return sqrt(tot / len(values))

def mean_interval(values, mean, std, eta):
    incr = eta * std / sqrt(len(values))
    return mean - incr, mean + incr

def calc_cov(values):
    m = mean(values)
    s = std_dev(values, m)

    return s / m

def calc_jfi(cov):
    return 1 / (1 + cov ** 2)

def lorenz_cg(values, mean):
    tot = 0
    for i in values:
        tot += abs(i - mean)

    mad = tot / len(values)
    return mad / (2 * mean)

def lorenz_curve(values, mean):
    x = []
    y = []

    values = sorted(values)
    n = len(values)
    tot = 0
    for i in range(len(values)):
        x.append((i + 1) / n)
        tot += values[i]
        y.append(tot / (n * mean))

    return x, y

def bootstrap(values, r0, gamma, t_func):
    R = ceil(2 * r0 / (1 - gamma)) - 1
    n = len(values)
    T = []
    for r in range(R):
        samples = []
        for _ in range(n):
            idx = rnd.randrange(0, n)
            samples.append(values[idx])
        stat = t_func(samples)
        T.append(stat)
    T = sorted(T)
    return T[r0], T[R + 1 - r0]



values = load()

print("Number of values:", len(values))

m = mean(values)
print("Mean:", m)

s = std_dev(values, m)
print("Standard deviation:", s)

r0 = 25


fn = lambda a: mean(a)
start, end = bootstrap(values, r0, 0.95, fn)
print("Bootstrap of Mean 95%:")
print("\t[", start, ";", end, "]")

start, end = bootstrap(values, r0, 0.99, fn)
print("Bootstrap of Mean 99%:")
print("\t[", start, ";", end, "]")


print("-" * 30)


start, end = mean_interval(values, m, s, 1.96)
print("Confidence interval for mean with gamma 95%:")
print("\t[", start, ";", end, "]")

start, end = mean_interval(values, m, s, 2.58)
print("Confidence interval for mean with gamma 99%:")
print("\t[", start, ";", end, "]")


print("-" * 30)


log_values = [log(x) for x in values]
log_mean = mean(log_values)
log_std = std_dev(log_values, log_mean)

trans_mean = exp(log_mean)
print("Trasformation mean:", trans_mean)

trans_std = exp(log_std)
print("Trasformation standard deviation:", trans_std)

start, end = mean_interval(log_values, log_mean, log_std, 1.96)
print("Confidence interval for transformation mean with gamma 95%:")
print("\t[", exp(start), ";", exp(end), "]")

start, end = mean_interval(log_values, log_mean, log_std, 2.58)
print("Confidence interval for transformation mean with gamma 99%:")
print("\t[", exp(start), ";", exp(end), "]")

