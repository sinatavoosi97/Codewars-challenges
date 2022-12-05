
def tribonacci(signature, n):

        list2=[]
        if n==1:
            list2.append(signature[-1])
            return list2

        elif n==0:
            return list2

        else:
            while len(signature)<n:
                signature.append(signature[-1]+signature[-2]+signature[-3])

            return signature

# print(tribonacci([1, 1, 1], 10))
# print(tribonacci([1, 1, 1], 1))
# print(tribonacci([300, 200, 100], 0))
# print(tribonacci([0.5, 0.5, 0.5], 30))
print(tribonacci([1, 0, 0], 10))
print(tribonacci([3, 2, 1], 10))
