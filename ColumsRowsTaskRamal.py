table = []
ascii_offset = ord("a") - 1

for row in range(4):
    current_row = []
    for col in range(4):
        if row == 0:
            if col == 0:
                cell = "*"
            else:
                cell = f"{col}"
        else:
            if col == 0:
                cell = chr(ascii_offset + row)
            else:
                cell = "x"
        current_row.append(cell)
    table.append(current_row)

for r in table:
    print(" ".join(r))