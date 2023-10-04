def generate_odd_order_magic_square(n):
    if n % 2 == 0:
        raise ValueError("Only odd-order magic squares are supported.")
    
    # Create an empty square filled with zeros
    magic_square = [[0] * n for _ in range(n)]

    num = 1  # The starting number
    i, j = 0, n // 2  # Initial position for number 1 (top row, middle column)

    while num <= n * n:
        # Place the current number in the current position
        magic_square[i][j] = num
        num += 1

        # Calculate the next position (move one row up and one column right)
        newi, newj = (i - 1) % n, (j + 1) % n

        # If the next position is already filled, adjust the position
        if magic_square[newi][newj] != 0:
            i = (i + 1) % n  # Move one row down
        else:
            i, j = newi, newj  # Move up and right

    return magic_square

def print_magic_square(magic_square):
    for row in magic_square:
        # Print each row as a space-separated string
        print(" ".join(map(str, row)))

# Example usage:
order = 3 # Specify the order of the magic square (e.g., 3 for a 3x3 square)
magic_square = generate_odd_order_magic_square(order)
print("Magic Square of Order", order)
print_magic_square(magic_square)