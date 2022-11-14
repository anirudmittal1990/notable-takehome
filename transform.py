import sys

def transform(text):

    transformed_array = []

    """convert word to number"""
    word_to_num = {"one": 1, "two": 2, "three": 3, "four": 4, "five": 5, "six": 6, "seven": 7, "eight": 8, "nine": 9}

    """transform the text"""
    summary_headline, pointers = text.split(" number ", 1)
    sub_pointers = pointers.split (" number next ")
    transformed_array.append(str.capitalize(summary_headline))

    for idx, pointer in enumerate(sub_pointers):
        if idx == 0:
            index, pointer = pointer.split(' ', 1)
            point = word_to_num[index]
        else:
            point += 1
        transformed_array.append(f"{point}. {str.capitalize(pointer)}")

    return "\n".join(transformed_array)


def main():

    """Take transcribed text from the user input"""
    text = input ("Enter the transcribed text in double quotes: ").strip('"')

    if not text or not isinstance(text, str):
        print ("Either the entered text is empty or not in a string format. Exiting..")
        sys.exit(1)

    """Transform the string and print the output"""
    output = transform(text.lower())
    print (output)

if __name__ == "__main__":
    main()
