import sys
import os
import pytest
current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)
from main import count_words, popular_words

@pytest.fixture
def input_file():
    input_file = "input.txt"
    with open(input_file, "w") as f:
        f.write("Hello, how are you? Are you ok? We shall go to the mall. We are at the mall. Are apples sweet?")
    return input_file

@pytest.fixture
def output_file():
    return "output.txt"

def test_count_words(input_file):
    words_counts = count_words(input_file)
    expected = {'hello': 1, 'how': 1, 'are': 4, 'you': 2, 'ok': 1, 'we': 2, 'shall': 1, 'go': 1, 'to': 1, 'the': 2, 'mall': 2, 'at': 1, 'apples': 1, 'sweet': 1}
    assert words_counts == expected

def test_popular_words_prewritten(input_file, output_file):
    popular_words(input_file, output_file)
    result = []
    with open(output_file, "r") as file:
        for line in file:
            word, count = line.strip().split("-")
            result.append((word, int(count)))
    expected = [('are', 4), ('you', 2),('we', 2),('the', 2),('mall', 2), ('hello', 1),('how', 1),('ok', 1),('shall', 1),('go', 1)]
    assert result == expected

@pytest.mark.parametrize("input_text, expected", [
    ("Good morning. Eat your lunch. Here is your morning coffee.", [('morning', 2), ('your', 2), ('good', 1), ('eat', 1),('lunch', 1), ('here', 1), ('is', 1), ('coffee', 1)]),
    ("Hi, lets go. We will go in 5 minutes, won`t we?", [('go', 2), ('we', 2),('hi', 1),('lets', 1),('will', 1),('in', 1),('5', 1),('minutes', 1),('won`t', 1)]),
    ("word1 word3 word2!!!! word3, word2", [('word3', 2), ('word2', 2),('word1', 1)]),
])
def test_popular_words_parametrization(input_file, output_file, input_text, expected):
    with open(input_file, "w") as f:
        f.write(input_text)
    popular_words(input_file, output_file)
    result = []
    with open(output_file, "r") as file:
        for line in file:
            word, count = line.strip().split("-")
            result.append((word, int(count)))
    assert result == expected


