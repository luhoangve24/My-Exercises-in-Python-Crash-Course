file_path = 'P10_FileAndEx\\ProjectGutenberg.txt'
with open(file_path, 'r', encoding='utf-8') as object:
    contents = object.read()

counts = contents.lower().count('there')
print(counts)