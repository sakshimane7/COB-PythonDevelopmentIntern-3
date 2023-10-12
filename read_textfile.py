from collections import Counter
import string


def count_unique_words(filename):
    # Read the file and remove punctuation
    translator = str.maketrans('', '', string.punctuation)
    with open(filename, 'r') as file:
        text = file.read().lower().translate(translator)

    # Split the text into words and count their occurrences
    word_counts = Counter(text.split())

    # Print the unique words and their occurrences
    for word, count in word_counts.items():
        print(f'{word}: {count}')


if __name__ == "__main__":
    # Replace with the actual file path
    filename = "text.file"
    count_unique_words(filename)
