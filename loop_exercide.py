# print even numbers from 1 <= to < 10

number = 10

count = 0

for i in range(1, number):
    if i % 2 == 0:
        count += 1
        print(i)
print(f"We have {count} even numbers")
