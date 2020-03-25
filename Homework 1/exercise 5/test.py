import numpy as np, scipy.stats as st

def load():
    file = open("data_ex5.csv", "r")
    s = file.readlines()[0].strip()
    values = [int(x) for x in s.split(',')]
    return values

values = load()
succ = values.count(1)
insucc = values.count(0)
print("Successes: {}".format(succ))
print("Insuccesses: {}".format(insucc))

p_1 = succ / (insucc + succ)
print("Probability of success: {}".format(p_1))
print("Mean 95% ci: {}".format(st.t.interval(0.95, len(values)-1, loc=p_1, scale=st.sem(values))))
print("Mean 99% ci: {}".format(st.t.interval(0.99, len(values)-1, loc=p_1, scale=st.sem(values))))

print("-"*30)
values = values[:15]
print("Consider only the first row")
print(values)
succ = values.count(1)
insucc = values.count(0)
print("Successes: {}".format(succ))
print("Insuccesses: {}".format(insucc))

p_1 = succ / (insucc + succ)
print("Probability of success: {}".format(p_1))
print("Mean 95% ci: {}".format(st.t.interval(0.95, len(values)-1, loc=p_1)))
print("Mean 99% ci: {}".format(st.t.interval(0.99, len(values)-1, loc=p_1)))