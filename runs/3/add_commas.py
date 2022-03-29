filename = "dataset1.csv"
with open(filename) as inp:
    with open(filename + ".csv", 'w') as out:
        lines = [i[:-1]+ ",\n" for i in inp.readlines()]
        out.writelines(lines)