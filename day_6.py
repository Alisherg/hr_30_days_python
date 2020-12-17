#!/usr/bin/env python3

if __name__ == "__main__":

    test_cases = int(input())

    for _ in range(test_cases):
        string = input()
        print(string[::2], string[1::2])
