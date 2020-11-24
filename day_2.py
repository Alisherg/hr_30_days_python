#!/usr/bin/env python3


def solve(meal_cost: float, tip_percent: int, tax_percent: int) -> int:

    total_cost: int

    total_cost = (
        meal_cost + (meal_cost * tip_percent / 100) + (meal_cost * tax_percent / 100)
    )

    print(round(total_cost))


if __name__ == "__main__":
    meal_cost = float(input())

    tip_percent = int(input())

    tax_percent = int(input())

    solve(meal_cost, tip_percent, tax_percent)
