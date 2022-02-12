import argparse
import numpy as np


class Color:
    GREEN = '\033[42m'
    YELLOW = '\033[43m'
    WHITE = '\033[47m'
    END = '\033[0m'


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("seed")
    args = parser.parse_args()
    seed = int(args.seed)
    np.random.seed(seed)

    with open("dict.txt", "r") as f:
        dictionary = list(map(lambda x: x.strip("\n"), f.readlines()))

    word_num = len(dictionary)
    dictionary_set = set(dictionary)

    answer = dictionary[np.random.randint(0, word_num)]
    char_set = set(answer)

    print("game start")
    while True:
        print("input guess")
        input_str = input()
        if input_str not in dictionary_set:
            print("wrong input")
            continue
        for i, c in enumerate(input_str):
            if c == answer[i]:
                print(Color.GREEN + c + Color.END, end="")
            elif c in char_set:
                print(Color.YELLOW + c + Color.END, end="")
            else:
                print(Color.WHITE + c + Color.END, end="")
        print()
        if input_str == answer:
            print("correct!")
            break


if __name__ == "__main__":
    main()
