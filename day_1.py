#!/usr/bin/env python3


def main():

    # initialized variables
    i: int = 4
    d: float = 4.0
    s: str = "HackerRank "

    # declare and read from stdin second int, float, string
    sec_int, sec_flt, sec_str = int(input()), float(input()), input()

    print(i + sec_int)
    print(d + sec_flt)
    print(s + sec_str)


if __name__ == "__main__":
    main()
