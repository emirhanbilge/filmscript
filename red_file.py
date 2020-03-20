from matplotlib.ticker import FuncFormatter
import matplotlib.pyplot as plt
import numpy as np

stops = "i me my myself we our ours ourselves you your yours yourself yourselves he him his himself she her hers herself it its itself they them their theirs themselves what which who whom" 
stops +=  " this that these those am is are was were be been being have has had having do does did doing a an the and but if or because " 
stops += "as until while of at by for with about against between into through during " 
stops += " before after above below to from up down in out on off over under again further then once here there when where why how all any both each few more most other some such no nor not only own same " 
stops += "so than too very s t can im dont will just don should now two "

stop_words = {}
def stop_words_hash():
    stop_words_array = stops.split(" ")
    for i in stop_words_array:
        stop_words[i] = i
stop_words_hash()

def sort_dictionary(dictionary):
    keys = sorted(dictionary.keys())
    PRINT_LIMIT = sorted(dictionary.values())
    PRINT_LIMIT = PRINT_LIMIT[len(PRINT_LIMIT)-20:len(PRINT_LIMIT)]
    choose_max = {}
    for i in keys:
        if (dictionary[i] in PRINT_LIMIT) and (i not in choose_max):
            choose_max[i]=dictionary[i]
        if len(choose_max) == 20:
            break
    values = sorted(choose_max.values())
    keys = choose_max.keys()
    return_dictionary= {}
    counter = 19
    while(counter>0):
        for i in keys:
            if choose_max[i] == values[counter] and i not in return_dictionary.keys():
                return_dictionary[i] = values[counter]
                counter -=1
    return return_dictionary

def read_and_indexing(TXT_FILE_NAME):
    file = open(TXT_FILE_NAME, "r")
    file_words_array = file.read().replace("'","").replace(".","").replace('"',"").replace(",","").replace(";","").replace("-","").replace("\n","").lower().replace("(","").replace(")","").split(" ")
    dictionary = {}
    for i in file_words_array:
        if i not in stop_words.keys() and i !="":
            if i in dictionary.keys():
                count = dictionary[i]
                dictionary[i] = count+1
            else:
                dictionary[i] =1
    return dictionary

def two_file_intersection(FILE_NAME_1 , FILE_NAME_2):
    word_values = []
    clear_dictionary ={}
    intersection = FILE_NAME_1.keys() & FILE_NAME_2.keys()
    same_dictionary = {}
    for i in intersection : 
        if("" != i):
            same_dictionary[i] = int(FILE_NAME_1[i]) + int(FILE_NAME_2[i])
            word_values.append(int(FILE_NAME_1[i]) + int(FILE_NAME_2[i]))
    same_dictionary = sort_dictionary(same_dictionary)
    return same_dictionary
def plot_show(dictionary):
    for i in dictionary.keys():
        print("Word : " , i , "    Frequancy " , dictionary[i])
    x = np.arange(20)
    fig, ax = plt.subplots()       
    plt.bar(x,dictionary.values())
    plt.xticks(x, dictionary)
    plt.show()         

while(1):
    print(" 1 - Only one txt read ")
    print(" 2 - Two txt read ")
    print(" 3 - Exit ")
    try:
        choosing = int(input())
        if(choosing == 1):
            txt_file = input("Enter txt file name (full-path) : ")
            movie = read_and_indexing(txt_file)
            movie = sort_dictionary(movie)
            plot_show(movie)
        elif(choosing == 2):
            txt_file_1 = input("Enter first movie txt file name (full-path) : ")
            txt_file_2 = input("Enter second movie txt file name (full-path) : ")
            movie_1 = read_and_indexing(txt_file_1)
            movie_2 = read_and_indexing(txt_file_2)
            intersection = two_file_intersection(movie_1,movie_2)
            plot_show(intersection)
        elif(choosing == 3):
            break
        else:
            print("Entry must be 1 or 2 ")
    except  :
        print("Enter integer number 1 or 2 ")
