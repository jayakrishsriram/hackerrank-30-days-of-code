class Calculator():
    def power(n,p):
        if n<0 or p<0:
            raise Exception('n and p should be non-negative')
        else:
            return pow(n,p)


T=int(input())
for i in range(T):
    n,p = map(int, input().split())
    try:
        ans=Calculator.power(n,p)
        print(ans)
    except Exception as e:
        print(e)   
