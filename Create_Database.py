from Data_Structure import Node, LinkedList, HashMap

import pickle


def read_file(file_name):
    # reads dictionary of eligible words, scores them, then pickles them to another file to be recalled later during
    # search functions
    database = HashMap(1000000)
    cnt = 0
    collision_count = 0
    test_values = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K,' 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    test_numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    with open(file_name, 'r') as from_file:
        for j in test_values:
            for k in test_numbers:
                test = [j, k]
                line = from_file.readline()
                while line:
                    cnt += 1
                    line = line.strip()
                    word_score = 0
                    for i in line:
                        word_score += score(i)
                    collision_count += database.assign(line, word_score, test)
                    line = from_file.readline()
                    #if cnt % 10000 == 0:
                        #print("cnt: {c}".format(c=cnt))
        #print("cnt: {c}".format(c=cnt))
        print("{j} == {k}".format(j=j, k=k))
        print("Collision Count: {c}\n\n".format(c= collision_count))


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
