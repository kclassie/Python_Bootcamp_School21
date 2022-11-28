import argparse


def main():
    parser = argparse.ArgumentParser(description='Decypher, ex01. Takes one string argument')
    parser.add_argument('string', type=str, help='Input string')
    input_str = parser.parse_args()
    try:
        text = list(map(lambda x: x[0], input_str.string.split(' ')))
        print(''.join(text))
    except IndexError:
        exit(0)


main()
