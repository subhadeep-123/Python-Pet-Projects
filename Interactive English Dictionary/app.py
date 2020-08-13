import json
from zipfile import ZipFile
from pathlib import Path
from difflib import get_close_matches

DIR_TO_EXTRACT = Path()


def extract(filename):
    with ZipFile(filename, 'r') as file:
        file.extractall(DIR_TO_EXTRACT)
    return json.load(open('data.json'))


def main(data):
    word = input("Enter a Word: ").lower()
    if word in data:
        return data[word]
    elif len(get_close_matches(word, data.keys())) > 0:
        entry = input(
            f"Did you mean {get_close_matches(word, data.keys())[0]} instead? Enter (Y/N) if Not: ")
        if entry == 'Y':
            return data[get_close_matches(word, data.keys())[0]]
        elif entry == 'N':
            return "The word doesn't exist. Please double check it."
        else:
            return "We did not understant WHAT YO SAYIN!!"

    else:
        return f"{word} Does not exist in the dictionary, Please Check!!"


if __name__ == '__main__':
    data = extract('data.zip')
    answer = main(data)
    if type(answer) == list:
        for i in answer:
            print(i)
    else:
        print(answer)
