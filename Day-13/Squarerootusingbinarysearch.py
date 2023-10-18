def square_root_binary_search(num, epsilon=1e-6):
    if num < 0:
        raise ValueError("Cannot calculate the square root of a negative number")

    if num == 0 or num == 1:
        return num

    left, right = 0, num

    while True:
        mid = (left + right) / 2
        square = mid * mid

        if abs(square - num) < epsilon:
            return mid
        elif square < num:
            left = mid
        else:
            right = mid

# Example usage:
number = 25
result = square_root_binary_search(number)
print(f"The square root of {number} is approximately {result:.6f}")
