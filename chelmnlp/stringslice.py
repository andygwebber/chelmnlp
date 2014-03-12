def first_space(sentence):
    answer = sentence.find(' ')
    return(answer)

def first_word(sentence):
    space1 = first_space(sentence)
    answer = sentence[0:space1]
    return(answer)

def second_word(sentence):
    space1 = first_space(sentence)
    print(space1)
    space2 = sentence.find(' ',space1+1)
    print(space2)
    answer = sentence[space1+1:space2]
    return answer

def list_of_words(sentence):
    index = 0
    failsafe = 0
    while True:
        right_space = sentence.find(' ', index+1)
        word = sentence[index:right_space]
        print(word)
        if index > len(sentence):
            break
        index = right_space + 1
        failsafe = failsafe + 1
        if failsafe > 10:
            break



def main():
    sentence = 'Hello my name is Karima'
    answer_space = first_space(sentence)
    answer_word = first_word(sentence)
    print('first space is {:d}, first word is {:s}'.format(answer_space, answer_word))
    print(second_word(sentence))
    print(len(sentence))
    list_of_words(sentence)

if __name__ == "__main__":
    main()
