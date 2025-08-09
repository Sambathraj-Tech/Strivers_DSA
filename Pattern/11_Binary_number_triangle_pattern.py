n = 5

for i in range(1, n + 1):
    # Start value: 1 if row number is odd, 0 if even
    if i % 2 == 0:
        val = 0
    else:
        val = 1
    for j in range(i):
        print(val, end=" ")
        val = 1 - val  # Flip after each print
    print()
