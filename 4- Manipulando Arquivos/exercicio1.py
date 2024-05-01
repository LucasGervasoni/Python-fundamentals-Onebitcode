def file(fname, nline):
    from itertools import islice
    with open(fname, encoding="UTF-8") as f:
        for line in islice(f,nline):
            print(line)
file('texto.txt', 1)