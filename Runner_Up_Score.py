if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    array = list(arr)
    maxi = max(array)
    array.remove(maxi)
    for i in range(len(array)):
        sec  = max(array)
        if maxi == sec:
            array.remove(sec)
    else:
        print(sec)
