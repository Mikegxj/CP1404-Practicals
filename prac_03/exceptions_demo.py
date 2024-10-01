"""
CP1404/CP5632 - Practical
"""

try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    fraction = numerator / denominator
    print(fraction)
except ValueError:
    print("Numerator and denominator must be valid numbers!")
except ZeroDivisionError:
    print("Cannot divide by zero!")
print("Finished.")

# Answer the following questions:
# 1. When will a ValueError occur?
# When the user enter non-integer number in the numerator and the denominator.
# 2. When will a ZeroDivisionError occur?
# When the user enter Zero as denominator the ZeroDivisionError will occur.
# 3. Could you change the code to avoid the possibility of a ZeroDivisionError?

try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    if denominator == 0:
        print("Cannot divide by zero!")
    else:
        fraction = numerator / denominator
        print(fraction)
except ValueError:
    print("Numerator and denominator must be valid numbers!")

print("Finished.")