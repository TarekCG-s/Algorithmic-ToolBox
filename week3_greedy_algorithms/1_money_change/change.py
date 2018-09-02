# Uses python3
import sys

def get_change(m):
    n = 0
    while (m > 0):
        if(m >= 10):
            n += 1
            m -= 10
        elif(m >= 5):
            n += 1
            m -= 5
        else:
            n += 1
            m -= 1
        
    return n

if __name__ == '__main__':
    m = int(input())
    print(get_change(m))
