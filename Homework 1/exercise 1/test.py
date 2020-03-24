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
