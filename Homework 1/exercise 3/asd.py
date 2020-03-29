import math


file = open("data_ex3.csv", "r")
data = [float(x) for x in file.readlines()]

def mean1():
  return sum(data)/len(data)

def mean2():
  tot = 0
  for d in data:
    tot += d
  return tot/len(data)

def std1():
  m = mean1()
  var = sum((d-m)**2 for d in data)/len(data)
  return math.sqrt(var)

def std2():
  m = mean2()
  tot = 0
  for d in data:
    tot += (d-m)**2
  return math.sqrt(tot/len(data))


m1, m2 = mean1(), mean2()
s1, s2 = std1(), std2()
c1, c2 = m1/s1, m2/s2

print("Mean 1 == Mean 2: {} ({}, {})".format(m1 == m2, m1, m2))
print("Std 1 == Std 2: {} ({}, {})".format(s1 == s2, s1, s2))
print("CoV 1 == CoV 2: {} ({}, {})".format(c1 == c2, c1, c2))

