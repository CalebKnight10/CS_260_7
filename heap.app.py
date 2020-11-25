#Heap driver
from heap import BinHeap


def main():
    h = BinHeap()
    h.insert([32, 23, 19, 4, 67, 12, 9])
    print(h)


if __name__ == '__main__':
    main()
