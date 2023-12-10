def count_characters(text):
    text = text.lower()
    char_count = {}

    for char in text:
        if char.isalnum():
            char_count[char] = char_count.get(char, 0) + 1

    return char_count


count = 0
with open(
        'C:\\Users\\Vladimir\\Desktop\\Git\\workspace\\github.com\\VladimirAlkin\\bookbot\\books\\frankenstein.txt') as f:
    file_contents = f.read()
    print(file_contents)
    words = file_contents.split()
    count += len(words)

print("\n\n--- Begin report of books/frankenstein.txt ---")
print(count, ' words found in the document\n')

character_counts = count_characters(file_contents)

sorted_items = sorted(character_counts.items(), key=lambda x: x[1], reverse=True)

for key, value in sorted_items:
    print(f"The '{key}' character was found {value} times")

print('--- End report ---')