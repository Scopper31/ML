import argparse
import pickle
import re
import sys
import os


def form(file_str):
    pattern = re.compile('[\W_0-9]+')
    file_str = pattern.sub(' ', file_str).lower().split()
    return file_str


def train(file_str, model_dir):
    file_arr = form(file_str)
    model = open(model_dir, 'wb+')
    try:
        data = pickle.load(model)["sanyasupertank"]
    except EOFError:
        data = dict()
    for n in range(1, len(file_arr)):
        for i in range(len(file_arr) - n):
            if tuple(file_arr[i: i + n]) not in data:
                data[tuple(file_arr[i: i + n])] = []
            data[tuple(file_arr[i: i + n])].append(file_arr[i + n])
    new_data = dict()
    new_data["sanyasupertank"] = data

    pickle.dump(new_data, model)
    model.close()


def main():
    parser = argparse.ArgumentParser()

    parser.add_argument('--input-dir', dest='files_dir', required=False)
    parser.add_argument('--model', dest='model_dir', required=True)

    if "--input-dir" not in sys.argv:
            files_dir = input()

    args = parser.parse_args()

    model = open(args.model_dir, 'wb+')
    model.write(b'')
    model.close()

    for path, zxc, files in os.walk(args.files_dir):
        for file in files:
            samples_txt = open(str(path + "\\" + file), 'r', encoding='utf-8')
            train(samples_txt.read(), args.model_dir)
            samples_txt.close()
            

if __name__ == '__main__':
    main()