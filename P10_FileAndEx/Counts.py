def count_words(file_path):
    """Count the approximate number of words in a file"""
    try:
        with open(file_path, encoding='utf-8') as object:
            contents = object.read()
    except FileNotFoundError:
        #pass Failing Silently
        return None
    else:
        string_list = contents.split()
        string_list_count = len(string_list)
        return string_list_count

number = count_words('P10_FileAndEx\\ProjectGutenberg.txt')
print(number)