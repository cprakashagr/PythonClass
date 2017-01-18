import cv2
import argparse


def main():
    parser = argparse.ArgumentParser()

    '''
    # Positional Argument
    parser.add_argument("echo", help="Help Message", type=str)
    '''

    # Optional Argument
    parser.add_argument("-v", "--verbosity", help="increase output verbosity")

    args = parser.parse_args()

    if args.verbosity:
        print(args)
    else:
        print(args)

    pass


if __name__ == '__main__':
    main()
