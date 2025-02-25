
logo_size = 10;
for row in range(logo_size):
    for col in range(logo_size):
        if col == 2 or col == 7 or (row == logo_size // 2 and 2<= col <= 7):
            print("H", end = " ")
        else:
            print(" ", end = " ")
    print()