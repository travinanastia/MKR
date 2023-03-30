def open_file(input):
    with open(input, "r") as file:
        text = file.read()
    return text
    
def write_file(output, popular_words):
    with open(output, "w") as file:
        for word, count in popular_words:
            file.write(f"{word}-{count}\n")

def count_words(input):
    text = open_file(input)
    words = text.lower().replace("\n", " ").replace(",", " ").replace(".", " ").replace("!", " ").replace("?", " ").split()
    words_counts = {}
    for word in words:
        if word not in words_counts:
            words_counts[word] = 1
        else:
            words_counts[word] += 1
    return words_counts







