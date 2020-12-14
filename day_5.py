#!/usr/bin/env python3


if __name__ == "__main__":
    n = int(input())

    for idx in range(1, 11):
        print("{} x {} = {}".format(n, idx, n * idx))
