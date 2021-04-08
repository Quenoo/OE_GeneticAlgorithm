# Booth function - two-dimensional, usually evaluated on the square x_i in [-10, 10] for all i = 1, 2.
# Global minimum: f(x*) = 0 at x* = (1, 3)
def booth_function(x1, x2):
    return (x1 + 2 * x2 - 7) ** 2 + (2 * x1 + x2 - 5) ** 2


if __name__ == '__main__':
    print(booth_function(0, 0))  # should be 74
    print(booth_function(1, 3))  # should be 0
