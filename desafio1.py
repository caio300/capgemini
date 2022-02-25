def triangle(n):
    if type(n) != int:
        return False
    my_string = ""
    for row in range(1, n + 1):
        if row == n:
            my_string += f"{(row * '*')}"
        else:
            my_string += f"{(n - row) * ' ' + (row * '*')}\n"
    return my_string
