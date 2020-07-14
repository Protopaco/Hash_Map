from Data_Structure import Node, LinkedList, HashMap

import pickle


def read_file(file_name):
    # reads dictionary of eligible words, scores them, then pickles them to another file to be recalled later during
    # search functions
    database = HashMap(50000)
    with open(file_name, 'r') as from_file:
        line = from_file.readline()
        while line:
            line = line.strip()
            word_score = 0
            for i in line:
                word_score += score(i)
            #print("line: {l} wordscore: {w}".format(l=line, w=word_score))
            database.assign(line, word_score)
            line = from_file.readline()


#def create_file(new_node):
#pass



def write_file(database):
    with open('score_saves.scr', 'a') as to_file:
        dbfile = open('score_saves.scr', 'wb')
        pickle.dump(database, dbfile)
        dbfile.close()
        print("Database created!")


def score(letter):
    # returns number value of each letter
    values = {'A': 1, 'B': 3, 'C': 3, 'D': 2, 'E': 1, 'F': 4, 'G': 2, 'H': 4, 'I': 1, 'J': 8, 'K': 5, 'L': 1, 'M': 3,
              'N': 1, 'O': 1, 'P': 3, 'Q': 10, 'R': 1, 'S': 1, 'T': 1, 'U': 1, 'V': 4, 'W': 4, 'X': 8, 'Y': 4, 'Z': 10}

    return values[letter]


if __name__ == "__main__":
    file_name = 'sowpods.txt'
    read_file(file_name)
