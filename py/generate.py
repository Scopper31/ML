import argparse
import pickle
import re
import sys
import os
import random


def main():
    parser = argparse.ArgumentParser()

    parser.add_argument('--model', dest='model_dir', required=True)

    parser.add_argument('--prefix', dest='prefix', required=False)
    
    parser.add_argument('--length', dest='length', type=int, required=True)

    args = parser.parse_args()

    model = open(args.model_dir, 'rb+')
    try:
        data = pickle.load(model)["sanyasupertank"]
    except EOFError:
        data = dict()

    if "--prefix" not in sys.argv:
            args.prefix = list(list(data.keys())[random.randint(0, len(data.keys()) - 1)])

    args.prefix = args.prefix.split()

    for i in range(args.length):

        if tuple(args.prefix) not in data:
            break
        next_word = data[tuple(args.prefix)][random.randint(0, len(data[tuple(args.prefix)]) - 1)]

        print(next_word, end=' ')

        args.prefix = args.prefix[1::]
        args.prefix.append(next_word)


if __name__ == '__main__':
    main()
