def remove(num, k):
    stack = []
    for n in num:
        while stack and k > 0 and stack[-1] < n:  # if u need to return the minimum possible
            stack.pop()
            k -= 1
        if stack or n != '0':
            stack.append(n)
    if k:
        stack = stack[:-k]
    return ''.join(stack) or '0'
k=int(input())
num=input()
print(remove(num,k))

#input = "462389"
# k = 2
# output = "6389"

# stack = empty
# 4 -> stack
# stack [-1]  = 4
# 6  > 4
# 4 popped out and 6 will be inside the stack => k =1
# 2  < 6 ---> 2 is popped  k =0

# 3 -> 8 -> 9
# 6389

# 98765 -> desceding order
# k =2
#987

