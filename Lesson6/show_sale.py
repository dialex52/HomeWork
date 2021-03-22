from sys import argv


def read_bake(start, stop=0):
    with open('bakery.csv', 'r', encoding='utf8') as f:
        line = f.readlines()
        if stop == 0:
            lines = line[start - 1:]
            for line in lines:
                print(line.rstrip())
        else:
            lines = line[start - 1:stop]
            for line in lines:
                print(line.rstrip())


def func(argv):
    start = int(argv[1])
    if len(argv) == 3:
        stop = int(argv[2])
        read_bake(start, stop)
    else:
        read_bake(start)


func(argv)
