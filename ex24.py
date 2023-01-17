def secret_formula(started):
    jelly_beans  = started * 500
    jars = jelly_beans / 1000
    crates = jars / 100
    return jelly_beans, jars, crates

start_point = 1000
beans, jars, crates = secret_formula(start_point)

print("Wtih start point of {}".format(start_point))
print(f"Beans - {beans} | Jars - {jars} | Crates - {crates}")

start_point /= 10

print("Method 2")
formula = secret_formula(start_point)
print("Beans - {} | Jars - {} | Crates - {}".format(*formula))