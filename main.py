def open_file(input):
    with open(input, "r") as file:
        text = file.read()
    return text
    
def write_file(output_file, most_common_words):
    with open(output_file, "w") as file:
        for word, count in most_common_words:
            file.write(f"{word}-{count}\n")








