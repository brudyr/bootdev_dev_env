def main():
    text_report("books/frankenstein.txt")

def char_count(text):
    char_count = {}

    for c in text:
        char = c.lower()
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    return char_count

def text_report(path):
    print(f"--- Begin report of {path} ---")
    with open(f"./{path}") as f:
        text = f.read()

        words = text.split()
        print(f"{len(words)} words found in the document\n")

        c = char_count(text)
        sorted_char_count = sorted(c.items(), key=lambda kv: kv[1], reverse=True)
        for char, count in sorted_char_count:
            if char.isalpha():
                print(f"The '{char}' character was found: {count} times")
    print(f"--- End report ---")

main()
