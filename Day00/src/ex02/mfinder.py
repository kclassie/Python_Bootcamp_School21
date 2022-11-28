import argparse
import sys
import re


def main():
    parser = argparse.ArgumentParser(description='Find M, ex02. No arguments required')
    parser.parse_args()
    input_str = sys.stdin.read()
    if re.fullmatch(r'.{5}\n.{5}\n.{5}\n*', input_str) is None:
        print("Error")
    elif re.fullmatch(r'\*[^*][^*][^*]\*\n\*\*[^*]\*\*\n\*[^*]\*[^*]\*\n*', input_str) is None:
        print("False")
    else:
        print("True")

main()
