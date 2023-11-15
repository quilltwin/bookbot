file_path = "books/frankenstein.txt"
with open(file_path) as f:
    num_words = 0
    num_letters = {}

    file_contents = f.read()
    for i in file_contents.split():
        num_words += 1
    for char in file_contents.lower():
        if char not in num_letters:
            num_letters[char] = 0
        num_letters[char] += 1
    
    #def letter_report():
    values = []
    for i in num_letters:
        if i.isalpha() == True:
            values.append(num_letters[i])
    values.sort(reverse = True)
    def letter_count():
        for v in values:
            for i in num_letters:
                if num_letters[i] == v:
                    print(f"The '{i}' character was found {v} times")


    
        


    #print(num_words)
    #print(num_letters)
    #print(values)

    print(f"--- report of {file_path} ---")
    print(f"{num_words} words found in {file_path}")
    letter_count()
    print("--- end of report ---")

