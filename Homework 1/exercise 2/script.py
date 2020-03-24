from math import floor, ceil, sqrt


def load():
    file = open("data_ex2.csv", "r")
    values = [[float(x) for x in line.split(",")] for line in file.readlines()]
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

first_row = values[0]
m = mean(first_row)
print("Mean of the first row:", m)

s = std_dev(first_row, m)
print("Standard deviation of the first row:", s)


start, end = mean_interval(first_row, m, s, 1.96)
print("Confidence interval for mean with gamma 95% of the first row:")
print("[", start, ";", end, "]")

print("-" * 30)

count = 0
for row in values[1:]:
    m = mean(row)
    if m <= end and m >= start:
        count += 1

print("Number of rows with mean falling in the confidence interval:", count)
