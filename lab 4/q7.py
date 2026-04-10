n = int(input())
r = int(input())

fact_n = 1
for i in range(1, n + 1):
    fact_n = fact_n * i

fact_r = 1
for i in range(1, r + 1):
    fact_r = fact_r * i

fact_n_minus_r = 1
for i in range(1, (n - r) + 1):
    fact_n_minus_r = fact_n_minus_r * i

nPr = fact_n // fact_n_minus_r
nCr = nPr // fact_r

print(nCr)
print(nPr)