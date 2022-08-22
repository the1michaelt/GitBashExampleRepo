# Task 1: Reverse a String 

(Given in class)
reverse a string
def print_word_in_reverse():
    reversed_word =''
    for index in range(len(word)-1,-1,-1):
        reversed_word +=word[index]
    print(reversed_word)

print_word_in_reverse()

# Task 3: Palindrome


def test_word_see_if_palindrome():
    reversed_word = ''
    for index in range(len(user_input)-1, -1, -1):
        reversed_word += user_input[index]
        if user_input != reversed_word:
            print('')
        else:
            print('A true palindrome.')


test_word_see_if_palindrome()


# Task 2: Capitalize a Letter	
# incomplete, scratchwork

#Capitalize first individual letters
# This does not solve the task.

string_name = "world championship wrestling"


def Sentence_case():
    first_letter = string_name[0].upper()
    print(first_letter, end="")


First_letter = Sentence_case()


def Title_Case(string_name):
    index1 = string_name.index(" ", 0)
    index1 += 1
    next_letter = string_name[index1].upper()
    # next_letter1 = string_name.append()
    print(next_letter, end="")


Other_letter = Title_Case(string_name)


def sentence(string_name):
    for character in string_name:
        print(character, end=" ")


Other_letter = sentence(string_name)


# for character in string_name:
#     char= range(1,1, len(string_name))
#     print(character, end="")


#Capitalize first individual letters
string_name = "hello world"


def Sentence_case():
    first_letter = string_name[0].upper()
    print(first_letter, end="")


First_letter = Sentence_case()


def Title_Case(string_name):
    index1 = string_name.index(" ", 0)
    index1 += 1
    next_letter = string_name[index1].upper()
    # next_letter1 = string_name.append()
    print(next_letter, end="")


Other_letter = Title_Case(string_name)

# 1a. Capture the first letter of a word

string_name = "hello world"

for character in string_name:
    index_number = string_name.index(character, 0, len(string_name))
    index_number = index_number -= 1
    print(character, end="")


# # # From the web site, https://datascienceparichay.com/article/python-capitalize-first-letter-of-each-word/#:~:text=%20Python%20%E2%80%93%20Capitalize%20First%20Letter%20of%20Each,function.%203%20Using%20string.capwords%20%28%29%20function%20More%20
string_name = "hello world"
title_case = " ".join(word[0].upper()+word[1:]
                      for word in string_name.split(" "))
print(title_case)

# for character in string_name:
#     for element in range(0, 1, 1):

#     isolate_first_letter = string_name[element]
#     isolate_first_letter = isolate_first_letter.upper()

# return isolate_first_letter
`

# def capture_first_letter(string_name):
#     for element in range(0,1,1):
#         isolate_first_letter=string_name[element]
#         isolate_first_letter=isolate_first_letter.upper()
#         return isolate_first_letter

# # the_first_letter= capture_first_letter(string_name)
# # # print(the_first_letter, end="" )

# # #append string name by index

#Capitalize first individual letters
# This does not solve the task.

string_name = "hello world"


def Sentence_case():
    first_letter = string_name[0].upper()
    print(first_letter, end="")


First_letter = Sentence_case()


def Title_Case(string_name):
    index1 = string_name.index(" ", 0)
    index1 += 1
    next_letter = string_name[index1].upper()
    # next_letter1 = string_name.append()
    print(next_letter, end="")


Other_letter = Title_Case(string_name)


# # # #1b. identify space between words
# # # def identify_the_space():
# # #     for character in string_name:
# # #         print(character)
# # #         if character == ' ':
# # #             break

# 1c. Identify the first character after a space perhaps to capitalize it
def identify_the_space(string_name):
    for character in string_name:
        print(character, end="")
        if character == ' ':
            index_number = string_name.index(character, 0, len(string_name))
            index_number += 1
            isolate_first_letter = string_name[index_number]
            isolate_first_letter = isolate_first_letter.upper()
            return index_number


# the_space= identify_the_space(string_name)


def capture_first_letter(string_name):
    for element in range(0, 1, 1):
        isolate_first_letter = string_name[element]
        isolate_first_letter = isolate_first_letter.upper()
        return isolate_first_letter


the_first_letter = capture_first_letter(string_name)


# # def capture_next_letter(string_name):
# #     for element in range(index_number, int(len(string_name)), 1):
# #         isolate_first_letter = string_name[element]
# #         isolate_first_letter = isolate_first_letter.upper()
# #         return isolate_first_letter

# # the_first_letter = capture_next_letter(string_name)
# # print(the_first_letter, end="")


# # # 1c. Identify the first character after a space perhaps to capitalize it
# # def identify_character_after_space(the_space, string_name):
# #     for character in string_name:
# #         index_number2 = string_name.index(character, 1, len(string_name))
# #         if character == ' ':
# #             index_number2 += 1
# #             character_after_space=string_name[index_number2]
# #             x=(character_after_space)
#             x= x.upper()
#             return(x)
#             break

# after_the_space = identify_character_after_space(the_space, string_name)

def identify_character_after_space():
    for character in string_name:
        index = string_name.index(character, 0, len(string_name))
        if character == ' ':
            index += 1
            character_after_space = string_name[index]
            capital_letter = (character_after_space)
            capital_letter = capital_letter.upper()
            print(capital_letter)
            break
