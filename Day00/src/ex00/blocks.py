import sys


def check_input(input_str: str) -> bool:
    if len(input_str) != 32:
        return False
    if (input_str[0:5] == '00000') & (input_str[5] != '0'):
        return True
    return False


def main():
    try:
        for i in range(int(sys.argv[1])):
            input_str = sys.stdin.readline()
            if check_input(input_str.rstrip()):
                print(input_str.rstrip())
    except (IndexError, ValueError):
        exit(1)


main()
