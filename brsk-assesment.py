import argparse
import sys
from collections import defaultdict


def find_matching_words(input_words, file_path):
    words_by_length_and_initial = defaultdict(set)
    with open(file_path) as f:
        for line in f:
            word = line.strip()
            initial = word[0].lower()
            words_by_length_and_initial[(len(word), initial)].add(word)

    results = []
    for word in input_words:
        candidates = words_by_length_and_initial.get((len(word), word[0].lower()), set())
        if candidates:
            results.append(next(iter(candidates)))  # Take any candidate
        else:
            results.append("'No alternative found for: " + word + "'")

    return " ".join(results)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='BRSK assessment.')
    parser.add_argument('words', type=str, help='List of words separated by spaces.')
    args = parser.parse_args()

    word_list = args.words.split()
    print(find_matching_words(word_list, 'words_alpha.txt'))
