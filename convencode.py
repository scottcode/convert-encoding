"""Converts a file or stream from one encoding to another"""

import argparse

parser = argparse.ArgumentParser()

parser.add_argument('infile')
parser.add_argument('inencoding')
parser.add_argument('outfile')
parser.add_argument('outencoding')


def main(args=None):
    args = parser.parse_args(args=args)
    with open(args.infile, encoding=args.inencoding) as f:
        data = f.read()
    with open(args.outfile, 'w', encoding=args.outencoding) as o:
        o.write(data)


if __name__ == '__main__':
    main()
