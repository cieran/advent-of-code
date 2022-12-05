def main():
    with open('./data/input.txt') as f:
        lines = f.read().splitlines()

    fully = 0
    overlap = 0
    for line in lines:
        x,y = line.split(',')
        x1,x2 = x.split('-')
        y1,y2 = y.split('-')

        xs = list(range(int(x1), int(x2)+1))
        ys = list(range(int(y1), int(y2)+1))
        
        if all(e in xs for e in ys) or all(e in ys for e in xs):
            fully += 1
        if any(e in xs for e in ys) or any(e in ys for e in xs):
            overlap += 1

    print(fully, overlap)

if __name__ == "__main__":
    main()
