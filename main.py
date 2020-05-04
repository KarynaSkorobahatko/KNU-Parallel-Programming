from utiles import normalize
import time
import pymp

input_list = list(range(1, 1000))
input_list = list(set(input_list))

start = time.time()

results = pymp.shared.list()

with pymp.Parallel(2) as p:
    for iter_item in p.iterate(input_list):
        _, r = normalize([iter_item], input_list)
        results.append(r)

print("Paralel work", time.time() - start, "seconds")