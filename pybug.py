def main():
    x = 1
    y = 0
    try:
        print(x / y)
    except ZeroDivisionError:
        return None

if __name__ == '__main__':
    main()
