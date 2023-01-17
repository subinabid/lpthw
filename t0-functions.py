def return_numbers():
    return 1, 2, 3

ta = tb = tc = 0

ta += return_numbers()[0]
tb += return_numbers()[1]
tc += return_numbers()[2]

print(f"{ta} | {tb} | {tc}")