import itertools

# word = input("Input the word or short phrase that you wish to create a code from: ")
# code_length = int(input("How many characters should the generated code have?: "))
# first_letter_option = input("Should the generated code start with the first letter of your word/phrase?: ")

def generate_code(word, length, first_letter):
    generated = itertools.permutations(word, length)

    results = []

    for i in generated:
        if first_letter:
            if i not in results and i[0] == word[0]:
                results.append(i)
        else:
            if i not in results:
                results.append(i)
    
    return results