import csv
from random import randint
from time import sleep


program = True
main_menu = True
check_lesson = False
check_lesson_number = False
checked_cod_word_once = False
checked_prev_cod_word = ""
lesson_number_strand = ""
row = {}
import os
import platform

# Check if the code is running on Replit
if 'REPLIT_DB_URL' in os.environ:
    on_replit = True
else:
    on_replit = False

    
def try_int(response):
    try:
        response = int(response)
        return response
    except:
        repeat_response = input("You didn't enter a number, try again. : ")
        return try_int(repeat_response)

def random_character_picker(chars, rand_lesson, choice_response):

    if rand_lesson:

        max_range_lesson = int((chars[-1]).lesson)

        chosen_lesson = randint(1, max_range_lesson)

    else:

        chosen_lesson = choice_response

    print("Lesson : ",chosen_lesson)

    max_range_number = 0
    
    for ind_char in chars:
        if ind_char.lesson == chosen_lesson:
            
            max_range_number = ind_char.number
            
    chosen_number = randint(1,max_range_number)

    for ind_char in chars:

        if ind_char.lesson == chosen_lesson and ind_char.number == chosen_number:

            return ind_char



def clear():
    global on_replit
    if on_replit:
        os.system('clear')  # For Replit
    elif platform.system() == 'Windows' and on_replit:
        os.system('cls')  # For Windows
    elif on_replit:
        os.system('clear')  # For Mac/Linux
    else:
        print("\n" * 10)
        print("\n" * 10)
        print("\n" * 10)
        print("\n" * 10)
        print("\n" * 10)
        print("\n" * 10)

class character:
    def __init__(self, lesson, number, mandarin, english, pinyin, compulsory):
        self.lesson = lesson
        self.number = number
        self.mandarin = mandarin
        self.english = english
        self.pinyin = pinyin
        self.compulsory = compulsory
        
    def print_self(self):
        print("==========="*13)
        if self.compulsory != None:
            print("Lesson : ",self.lesson,"      Character :   ", self.number, self.mandarin, self.english, self.pinyin, "    To get a mark you must say : ",  self.compulsory)
        else:
            print("Lesson : ",self.lesson,"      Character :   ", self.number, self.mandarin, self.english, self.pinyin)
        print("==========="*13)
""" 
def read_codex(check_lesson, check_lesson_number, lesson_number_strand, row, checked_cod_word_once):
    global iter_read
    filepath = "HSK-Codex.csv"
    with open(filepath, "r", encoding='utf-8') as file:
        reader = csv.reader(file)
        for rows in reader:
            row = {}
            for word in rows:
                for letter in word:
                
                    #print("letter:",letter)
                
                    try:
                        int(letter)
                        check_lesson_number = True
                    except Exception as E:
                        #print(E)
                        check_lesson_number = False
                
                    if letter == "[":
                        check_lesson = True
                    
                    
                    if check_lesson and check_lesson_number:
                        lesson_number_strand = lesson_number_strand + letter
                
                if check_lesson == True:
                    None
                elif not checked_cod_word_once:
                    row[word] = ""
                    checked_cod_word_once = True
                elif checked_cod_word_once:
                    row[checked_prev_cod_word] = word
                    checked_cod_word_once = False

                checked_prev_cod_word = word
                    
            if check_lesson:
                print("\n=== Lesson: "+ lesson_number_strand + " ===\n")
                check_lesson = False
                continue
            
            print("\n",row,"\n")
"""
iter_row = 0
csv_row = 0
iter_word = 0
iter_letter = 0
current_char = None
grab_lesson = ""
lesson_grabbed = ""
all_words = []
not_lesson = True
      
def read_chars():
    global iter_row, iter_word, current_char, grab_lesson, lesson_grabbed, all_words, not_lesson, iter_letter, csv_row
    
    filepath = "HSK-Chars.csv"
    
    with open(filepath, "r", encoding='utf-8') as file:
        reader = csv.reader(file)
        
        for rows in reader:
            iter_row += 1
            iter_word = 0
            for word in rows:
                
                iter_word += 1
                iter_letter = 0

                if iter_word == 1 and not_lesson:

                    csv_row = word
                
                if iter_word == 2 and not_lesson:
                    
                    current_char = character(int(lesson_grabbed), None, None, None, None, None)
                    current_char.mandarin = word

                if iter_word == 3 and not_lesson:

                    current_char.number = int(csv_row)
                    current_char.english = word
                    
                if iter_word == 4 and not_lesson:

                    current_char.pinyin = word

                if iter_word == 5 and not_lesson:

                    converged = ""

                    listed_compulse = []
                    
                    for index, letter in enumerate(word):

                        if letter != ";":
                            
                            converged = converged + letter

                        if letter == ";" or index == len(word) - 1:

                            listed_compulse.append(converged)
                            
                            converged = ""

                    current_char.compulsory = listed_compulse
                            
                            
                
                for letter in word:
                    iter_letter += 1
                    if grab_lesson == "[":
                        try:
                            int(letter)
                            if iter_letter == 2:
                                lesson_grabbed = ""
                            lesson_grabbed = lesson_grabbed + letter
                        except:
                            grab_lesson == ""
                            
                    if letter == "]":
                        grab_lesson = ""
                        not_lesson = True
                        
                    if letter == "[":
                        grab_lesson = letter
                        not_lesson = False
                        
            if current_char != None:
                all_words.append(current_char)
        
        return all_words

chosen_chars = []


while program:
    if main_menu == True:
        print("\n")
        print((" "*15)+("="*10)+"HSK3 Helper"+("="*10))
        print("\n\n 1 - [Test]\n")
        print("\n 2 - [Help]\n")
        print("\n 3 - [Codex]\n")
        print("\n 4 - [Leave]\n")
        menu_response = input("User: ")
        clear()
        if menu_response == "1":
            
            all_words = read_chars()

            #for ind_character in all_words:
                #ind_character.print_self()

            clear()

            print("\n\nTopic 1 [1] - What's your plan for the weekend? *staying home*\n\n")
            print("\n\nTopic 2 [2] - When will he come back? *who?*\n\n")
            print("\n\nTopic 3 [3] - There are plenty of drinks on the table. *pls don't be alcohol* \n\n")
            print("\n\nTopic 4 [4] - She always smiles when talking to customers. *why* \n\n")
            print("\n\nTopic 5 [5] - I'm getting fatter and fatter lately. *bruh what are these topic names* \n\n")
            print("\n\nTopic 6 [6] - Why are they suddenly missing? *sounds a bit like topic 2* \n\n")
            print("\n\nTopic 7 [7] - I've known her for five years. *I've known her for 0 years* \n\n")
            print("\n\nTopic 8 [8] - I'll go wherever you go. *ok* \n\n")
            print("\n\nTopic 9 [9] - She speaks Chinese like a native *I speak Chinese like a foreigner* \n\n")
            print("\n\nTopic 10 [10] - Maths is much harder than History *idk I don't do history* \n\n")
            print("\n\nTopic 11 [11] - Don't forget to turn off the air conditioner *I only have a radiator*\n\n")
            print("\n\nTopic 12 [12] - Leave the important items with me *ok*\n\n")
            print("\n\nTopic 13 [13] - I walked back *where*\n\n")
            print("\n\nTopic 14 [14] - Please bring the fruit here *the fruit might be in my belly*\n\n")
            print("\n\nTopic 15 [15] - The rest of them are all OK *?*\n\n")
            print("\n\nTopic 16 [16] - I am so tired that I want to do nothing but sleep after work *that's me rn*\n\n")
            print("\n\nTopic 17 [17] - Everybody is able to cure your 'disease' *I'm not a doctor*\n\n")
            print("\n\nTopic 18 [18] - I believe they'll agree *what if i disagree*\n\n")
            print("\n\nTopic 19 [19] - Didn't you recognise him *no*\n\n")
            print("\n\nTopic 20 [20] - I've been influenced by him *efieifieigi*\n\n")
            print("\n\nRandom [21] - Chooses a random topic *if it's not that random, I'm sorry* \n\n")
            choice_response = input("\nType the number for the topic you want, so if you want random, you type 21... : ")
            print("\n\n")

            choice_response = try_int(choice_response)

            rand_lesson = True
            
            while choice_response > 21 or choice_response < 1:

                choice_response = input("Invalid response, please try again : ")

                choice_response = try_int(choice_response)

            choice_question_response = input("How many questions would you like to answer? : ")

            choice_question_response = try_int(choice_question_response)
            
            while choice_question_response < 1:

                choice_question_response = input("Invalid response, please try again : ")

                choice_question_response = try_int(choice_question_response)

            if choice_response < 21:

                rand_lesson = False

                for ind_character in all_words:
                    
                    if ind_character.lesson == choice_response:

                        chosen_chars.append(ind_character)

            else:

                chosen_chars = all_words

            num_of_q_answered = 0


            while num_of_q_answered != choice_question_response:

                clear()
                
                meaning_words =[]
                
                question_char = random_character_picker(chosen_chars, rand_lesson, choice_response)

                #question_char = chosen_chars[18]

                print("\n\nWhat is the meaning of \'" + question_char.mandarin + "\'?\n\n")

                meaning_answer = input()
                meaning_answer = meaning_answer.lower()

                compulse = False

                if (question_char.compulsory) != None:
                    meaning_words = question_char.compulsory
                    compulse = True
                else:
                    for word in (question_char.english).split():
                        if word != "part.used" and word != "at" and word != "the" and word != "to" and word != "area" and word != ";" and word != "be" and word != "of" and word != "a" and word != "or" and word != "end": # and word != "
                            meaning_words.append(word)

                not_correct = True

                for index, word in enumerate(meaning_words):
                    word = word.lower()
                    meaning_words[index] = word

                for index, word in enumerate(meaning_words):
                    for letter in word:
                        if ord(letter) < 97 or ord(letter) > 122:
                            word = word.replace(letter, "")
                            word = word.lower()
                            meaning_words[index] = word

                correct_words = 0

                #print(meaning_words)
                
                while not_correct:
                    if meaning_answer == "":
                        meaning_answer = input("\nWrong, try again : ")
                        meaning_answer = meaning_answer.lower()
                        continue
                    if meaning_answer == (question_char.english).lower():
                        not_correct = False
                    else:
                        for index, word in enumerate(meaning_answer.split()): # clean all this up use enumerate next time
                            #print(index, word)
                            for letter in word:
                                if ord(letter) < 97 or ord(letter) > 122:
                                    meaning_answer = meaning_answer.replace(letter, "")
                            if compulse == True: # this is clean

                                #print(meaning_words)

                                #print(correct_words, len(meaning_words))

                                if word in meaning_words:

                                    correct_words += 1
                                    
                                if index + 1 == len(meaning_answer.split()) and correct_words >= len(meaning_words):

                                    not_correct = False

                                    continue
                                
                                elif index + 1 == len(meaning_answer.split()) and correct_words != len(meaning_words):

                                    meaning_answer = input("\nWrong, try again : ")
                                    meaning_answer = meaning_answer.lower()
                                    correct_words = 0
                                    continue
                                
                            else: #If there are no compulsory words

                                #print(word in meaning_words)
                                if word in meaning_words: #correct

                                    not_correct = False
                                    continue
                                
                                if not_correct == False:
                                    continue
                                elif index + 1 == len(meaning_answer.split()): #not_correct == True
                                    meaning_answer = input("\nWrong, try again : ")
                                    meaning_answer = meaning_answer.lower()
                                    continue
                            

                print("\n\nCorrect!\n\n")
                sleep(2)
                print("What's its pinyin?\n\n")
                not_correct = True
                meaning_answer = (input()).lower()
                while not_correct:
                    if meaning_answer == "":
                        meaning_answer = input("\nWrong, try again : ")
                        meaning_answer = meaning_answer.lower()
                        continue
                    for index, word in enumerate(meaning_answer.split()):
                        for letter in word:
                            if ord(letter) < 97 or ord(letter) > 122:
                                word = word.replace(letter, "")
                        new_index = index
                        if len(meaning_answer.split()) > len((question_char.pinyin).split()): #if answer is longer than pinyin
                            if index != len(meaning_answer.split()) - 1:
                                continue
                            else:
                                meaning_answer = input("\nWrong, try again : ")
                                meaning_answer = meaning_answer.lower()
                                continue
                        if new_index > ( len((question_char.pinyin).split()) - 1 ) :
                            meaning_answer = input("\nWrong, try again : ")
                            meaning_answer = meaning_answer.lower()
                            continue
                            
                        elif word != ((question_char.pinyin).split())[new_index] and len(meaning_answer.split()) <= len(question_char.pinyin):
                            meaning_answer = input("\nWrong, try again : ")
                            meaning_answer = meaning_answer.lower()
                            continue

                        if index == (len((question_char.pinyin).split()) - 1) and word == ((question_char.pinyin).split())[index] and ( len((meaning_answer).split()) - 1 ) == ( len((question_char.pinyin).split()) - 1 ):
                            not_correct = False
                        elif ( len((meaning_answer).split()) - 1 ) < ( len((question_char.pinyin).split()) - 1 ):
                            meaning_answer = input("\nWrong, try again : ")
                            meaning_answer = meaning_answer.lower()
                            continue
                print("\n\nCorrect!\n\n")
                sleep(2)
                        
                    
                num_of_q_answered += 1
        if menu_response == "2":
            print("I've finished writing the whole program... and I kinda forgot what I wanted to write here")
            print("'If you would like to contact Childline, get help and advice about a wide range of issues, call us on 0800 1111, talk to a counsellor online, send Childline an email or post on the message boards.'")
            print("\n\n")
            print("I guess you should just get used to these words, and once that happens, go and revise grammar structures")
            sleep(5)
            input("\n\nPress [ENTER] to go back to main menu")
        if menu_response == "3":
            all_words = read_chars()
            for ind_character in all_words:
                ind_character.print_self()
        if menu_response == "4":
            main_menu = False
            program = False


