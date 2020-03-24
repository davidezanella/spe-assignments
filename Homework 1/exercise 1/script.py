from math import floor, ceil, sqrt


def load():
    file = open("data_ex1.csv", "r")
    values = [float(x) for x in file.readlines()]
    return values

def median(values):
    values = sorted(values)
    n = len(values)
    if(n % 2 != 0):  # odd
        idx = int((n+1) / 2)
        return values[idx]
    else:
        idx = int(n/2)
        return (values[idx] + values[idx + 1]) / 2

def calc_j_k(values):  # calculate j, k for confidence level 95%
    n = len(values)
    j_idx = floor(0.5 * n - 0.98 * sqrt(n))
    k_idx = ceil(0.5 * n + 1 + 0.98 * sqrt(n))

    return j_idx, k_idx

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
values = sorted(values)

med = median(values)

print("Number of values:", len(values))
print("Median:", med)

j, k = calc_j_k(values)
print("j:", j, " - k:", k)

j_val, k_val = values[j], values[k]
print("95% confidence interval for median:")
print("[", j_val, ";", k_val, "]")

print("-" * 30)


m = mean(values)
print("Mean:", m)

s = std_dev(values, m)
print("Standard deviation:", s)


start, end = mean_interval(values, m, s, 1.96)
print("Confidence interval for mean with gamma 95%:")
print("[", start, ";", end, "]")

start, end = mean_interval(values, m, s, 2.58)
print("Confidence interval for mean with gamma 99%:")
print("[", start, ";", end, "]")
