from one_robocopy_info import OneRobocopyInfo

if __name__ == "__main__":
    # sekcja testowa - testujemy to co wytworzysliśmy
    info = OneRobocopyInfo('24 kwieciec 2022', '25 wkiecień 2022', 'c:\dane\source', 'c:\dane\dest', 1, 2, 3, 10, 20, 30)
    print('hello')
    print(info.__str__())
