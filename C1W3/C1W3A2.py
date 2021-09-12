#/usr/bin/python3


def foo(W, values):
    result = 0.0
    values = sorted(values, key=lambda x: x[2], reverse=True)
    for value, weight, teta in values:
        if not W:
            break

        if weight <= W:
            result += value
            W -= weight
        else:
            result += round(teta * W, 4)
            W = 0
    return result
            
    


n, W = [int(x) for x in input().split()]
dvals = []
for i in range(n):
    v, w = [int(x) for x in input().split()]
    dvals.append((v, w, v / w))

print(foo(W, dvals))