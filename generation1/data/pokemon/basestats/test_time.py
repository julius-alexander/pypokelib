from poke_base_class import call_int, call_str
import time

res_str = []
res_int = []


for i in range(10):
    res_str.append(call_str())
    res_int.append(call_int())

print(f"String average: {sum(res_str)/len(res_str)}\n \
      Integer average: {sum(res_int)/len(res_int)}")
