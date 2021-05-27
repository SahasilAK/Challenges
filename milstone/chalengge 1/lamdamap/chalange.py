
def sol(ls):

    ls1 = []
    for i in ls:
        if i > 0:

            ls1.append(i**2)

    return ls1






def lambdaMap(arr):


    ans = map(sol, arr)
    return ans


if __name__ == '__main__':
    n = int(raw_input())
    arr = []
    for _ in range(n):
        arr.append(list(map(int, raw_input().split())))

    ans = lambdaMap(arr)
    for row in ans:
        print(' '.join(map(str, row)))
