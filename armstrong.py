def is_armstrong(number):
    digits = [int(d) for d in str(number)]
    power = len(digits)
    return number == sum(d ** power for d in digits)

def get_armstrong_numbers_in_range(start, end):
    """Returns a list of Armstrong numbers in the given range [start, end]."""
    return [num for num in range(start, end + 1) if is_armstrong(num)]

# Example usage:
num = int(input("Enter a number: "))
if is_armstrong(num):
    print(f"{num} is an Armstrong number.")
else:
    print(f"{num} is not an Armstrong number.")

# Example usage of the new method:
start = int(input("Enter range start: "))
end = int(input("Enter range end: "))
armstrong_numbers = get_armstrong_numbers_in_range(start, end)
print(f"Armstrong numbers between {start} and {end}: {armstrong_numbers}")