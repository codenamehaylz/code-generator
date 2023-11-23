import itertools

def generate_codes(word, length, first_letter):
    no_space_word = word.replace(" ", "")
    generate = itertools.permutations(no_space_word, length)

    results_of_generated = []
    codes = []

    for i in generate:
        if first_letter == "on":
            if i not in results_of_generated and i[0] == word[0]:
                results_of_generated.append(i)
        else:
            if i not in results_of_generated:
                results_of_generated.append(i)

    for i in results_of_generated:
        code = ""
        for j in i:
            code += j

        codes.append(code.upper())

    return codes

# print(generate_codes('Hayley', 3, 'on'))