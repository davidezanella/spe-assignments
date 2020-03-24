import numpy as np, scipy.stats as st

def load():
    file = open("data_ex1.csv", "r")
    values = [float(x) for x in file.readlines()]
    return values


values = np.array(load())
print("Number of values:", len(values))
print("Median:", np.median(values))
print("Median 95% ci: {}".format(st.t.interval(0.95, len(values)-1, loc=np.median(values), scale=st.sem(values))))
print("------------------------------")
print("Mean: {}".format(np.mean(values)))
print("Standard deviation: {}".format(np.std(values)))
print("Mean 95% ci: {}".format(st.t.interval(0.95, len(values)-1, loc=np.mean(values), scale=st.sem(values))))
print("Mean 99% ci: {}".format(st.t.interval(0.99, len(values)-1, loc=np.mean(values), scale=st.sem(values))))


"""

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
"""
