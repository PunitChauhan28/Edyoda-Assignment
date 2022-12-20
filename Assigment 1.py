terms = int(input("Enter how many terms: "))

a, b = 0, 1
i = 0

if terms <= 0:
    print("Invalid input")

elif terms == 1:
    print("\nFibonacci series up to", terms, "terms:")
    print(a)
else:
    print("\nFibonacci series up to", terms, "terms:")
    while i < terms:
        print(a)
        next = a + b
        a= b
        b = next
        i += 1
