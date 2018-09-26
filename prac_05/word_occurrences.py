
def main():
    text = input("Text: ")
    word_list = text.split(" ")
    dictionary = {}

    for word in word_list:
        i = 0
        for n in range(len(word_list)):
            if word == word_list[n]:
                i += 1
            dictionary.update({word: i})

    list_of_keys = list(dictionary.keys())
    list_of_keys.sort()
    unique_keys = list(set(list_of_keys))
    unique_keys.sort()

    for key in unique_keys:
        print("{} : {}".format(key, dictionary[key]))


main()
