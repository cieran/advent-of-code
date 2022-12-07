def main():
    with open('./data/sample.txt') as f:
        lines = f.read().splitlines()

    print(lines)

if __name__ == "__main__":
    main()
