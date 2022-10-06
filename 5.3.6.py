def filter_teens(a=13, b=13, c=13):
    fixed = fix_teen(a) + fix_teen(b) + fix_teen(c)
    print(fixed)


def fix_teen(n):
    match n:
        case 13 | 14 | 17 | 18 | 19:
            return 0
        case _:
            return n


filter_teens(15, 16, 17)
















