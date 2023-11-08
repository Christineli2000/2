
def append_to_file(pth, line):
    """
    Appends the new line to the end of the given file

    pth: path of the file to write to
    line: new line to be added to the file
    """
    with open(pth, 'a') as file:
        file.write(line)


def replace_line_words(line, new_words):
    """
    Replace the words of line that are among the keys
    of the new_words dictionary with their corresponding value

    For example, given:
    new_words = {'hello' : 'bye}
    line = 'Hello there, hello'

    This function should return
    'Bye there, bye'

    Parameters:
        line:       string to be modified
        new_words:  dictionary of the form {original_word : new_word}

    """
    new_line = []
    for word in line.strip().split(" "):
        if word in new_words:
            new_line.append(new_words[word])
        elif word.lower() in new_words:
            new_line.append(new_words[word.lower()].capitalize())
        else:
            new_line.append(word)

    return " ".join(new_line)


def create_modified_file(old_file_pth, new_file_pth, new_words):
    """
    Create a new file called new_file_pth that is the exact same as
    old_file_pth, but with its words replaced according to the new_words dictionary.
    Words not found in the new_words dictionary should be left unchanged.

    The text in old_file_pth should be left unchanged at the end.

    old_file_pth: path of original file
    new_file_pth: path of new file created containing replaced words
    new_words: dictionary of the form {original_word : new_word}
    """
    with open(old_file_pth, 'rt') as old_file:
        for line in old_file:
            new_str = replace_line_words(line, new_words) + "\n"
            append_to_file(new_file_pth, new_str)


ori_file = 'lyrics.txt'
new_file = 'modified_lyrics.txt'
words_replacement = {
    'life': 'new_life',
    'no': 'new_no',
    'open': 'new_open',
    'me': 'new_me',
}

create_modified_file(ori_file, new_file, words_replacement)
