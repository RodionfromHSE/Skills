#! /opt/homebrew/bin/python3

import os
import sys
from argparse import ArgumentParser

def get_args():
    parser = ArgumentParser(description='Check algorithm')
    parser.add_argument('-i', '--input', type=str, help='Input file', default='input.txt')
    parser.add_argument('-o', '--output', type=str, help='Output file', default=sys.stdout)

    return parser.parse_args()

def main():
    args = get_args()
    if args.output == sys.stdout:
        os.system(f'python3 main.py < {args.input}')
    else:
        os.system(f'python3 main.py < {args.input} > {args.output}')

if __name__ == '__main__':
    main()