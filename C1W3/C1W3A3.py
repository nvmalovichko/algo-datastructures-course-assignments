#/usr/bin/python3


def foo(end_stop, fuel, n_stops, stops):
    stops.append(end_stop)
    result = 0
    current_dist = 0
    massive = stops

    while True:
        for i, stop in enumerate(massive):
            if fuel < (stop - current_dist):
                if i == 0:
                    result = -1
                else:
                    result += 1
                    current_dist = massive[i - 1]
                break
        massive = massive[i:]

        if result < 0 or (len(massive) == 1 and fuel >= (stop - current_dist)):
            break

    return result
        

d = int(input())
m = int(input())
n = int(input())
stops = [int(x) for x in input().split()]

print(foo(d, m, n, stops))