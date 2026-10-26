from random import randint

month = randint(1,12)

match month:
    case 1 | 3 | 5 | 7 |8 | 10 | 12:
        print(f"{month}月有31填")
    case 4 | 6 | 9:
        print(f"{month}月有30天")
    case 2:
        print(f"{month}月有28天")