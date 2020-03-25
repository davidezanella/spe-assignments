from math import floor, ceil, sqrt, log, exp
import random as rnd
import matplotlib.pyplot as plt 


def load():
    file = open("data_ex5.csv", "r")
    values = [int(x) for x in file.readlines()[0].split(',')]
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


values = load()

print("Number of values:", len(values))

m = mean(values)
print("Probability of success (mean):", m)

s = std_dev(values, m)
print("Standard deviation:", s)


start, end = mean_interval(values, m, s, 1.96)
print("Confidence interval for mean with gamma 95%:")
print("\t[", start, ";", end, "]")

start, end = mean_interval(values, m, s, 2.58)
print("Confidence interval for mean with gamma 99%:")
print("\t[", start, ";", end, "]")


print("-" * 30)


first_rows = values[:15]

m_r = mean(first_rows)
print("Probability of success of the first 15 rows (mean):", m_r)
