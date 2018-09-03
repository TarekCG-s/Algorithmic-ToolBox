# Uses python3
import sys

def get_optimal_value(capacity, weights, values):
    
    value = 0
    i = 0
    
    for x in range(len(values)):
        values[x] = (values[x] / weights[x])
        
    sortedVals = sorted(values, reverse=True)

    while (capacity > 0):
        
        index  = values.index(sortedVals[i])
        addedWgt = min(weights[index], capacity)
        value += (sortedVals[i] * addedWgt)
        capacity -= addedWgt
        i += 1                       

    return value




if __name__ == "__main__":
    data = list(map(int, sys.stdin.read().split()))
    n, capacity = data[0:2]
    values = data[2:(2 * n + 2):2]
    weights = data[3:(2 * n + 2):2]
    opt_value = get_optimal_value(capacity, weights, values)
    print("{:.10f}".format(opt_value))
