# Write a program that prints the first 20 even numbers. There are several correct approaches, but they all use a loop of some sort. Do no write twenty print statements

# The first even number is 0:

# 0 2 4 6 8 10 12 14 16 18 20 22 24 26 28 30 32 34 36 38


# Method 1: Using a for loop with range
for i in range(0, 20):
    print(i * 2, end=" ")

# Alternatively, Method 2: Using a for loop with range step
# for i in range(0, 39, 2):
#     if i // 2 < 20:  # Ensuring we only print 20 numbers
#         print(i, end=" ")

# Alternatively, Method 3: Using a while loop
# count = 0
# num = 0
# while count < 20:
#     print(num, end=" ")
#     num += 2
#     count += 1