stack = []

stack.append(5)
stack.append(2)
stack.append(3)
stack.append(7)
stack.pop()
stack.append(1)
stack.append(4)
stack.pop()

print(stack)
# 반대로 출력
print([stack[i] for i in range(len(stack)-1,-1,-1)])
print(stack[::-1])
