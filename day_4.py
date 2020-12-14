#!/usr/bin/env python3


class Person:
    def __init__(self, initialAge):
        self.age = initialAge

        if self.age < 0:
            print("Age is not valid, setting age to 0.")
            self.age = 0

    def amIOld(self):
        if self.age < 13:
            print("You are young.")
        elif 13 <= self.age < 18:
            print("You are a teenager.")
        else:
            print("You are old.")

    def yearPasses(self):
        self.age += 1


if __name__ == "__main__":
    t = int(input())

    for _ in range(t):
        age = int(input())
        p = Person(age)
        p.amIOld()

        for _ in range(3):
            p.yearPasses()
        p.amIOld()
        print("")
