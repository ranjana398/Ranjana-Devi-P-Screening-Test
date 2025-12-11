
# Problem-2: Generate odd number series till 'a'

a = int(input("Enter a number: "))
result = []

for i in range(1, a*2, 2):
    result.append(i)

print(*result, sep=", ")
