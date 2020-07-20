import pickle

def load_database(save_file = 'score_saves.txt'):
    dbfile = open(save_file, 'rb')
    return_file = pickle.load(dbfile)
    dbfile.close()
    return return_file

def interface():

    print("Enter the word you would like to search for:")
    word = input("> ")
    search(word)

def search(database):
    entry = ""
    while entry != 'X':
        print("*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/")
        print("Search Menu!")
        print("*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/")
        print("Enter the word you'd like to search for:")
        print("enter 'x' if you'd like to exit")
        entry = input('> ')
        entry = entry.upper()
        if entry != 'X':
            answer = database.retrieve(entry)
            print("{k} - {s} points\n\n\n".format(k=answer[0], s=answer[1]))






def main_menu(database):
    entry = ''
    while entry != 'x':
        print("*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/")
        print("Main Menu!")
        print("*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/")
        print("(w) - Word Search")
        print("(x) - Exit")
        entry = input('> ')
        entry = entry.lower()
        if entry == 'w':
            search(database)
            print("main_menu")
            entry = ""
        elif entry != 'x':
            print("Invalid entry, please try again!")
        else:
            print("Goodbye!")


if __name__ == "__main__":
    #load database
    try:
        database = load_database()
        print("Database loaded!")
    except FileNotFoundError:
        print("Database file not found!")
        print("Please enter file name:")
        file_name = input("> ")
        load_database(file_name)

    print("*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/")
    print("Welcome to Scrabble Search!")
    print("*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/")
    main_menu(database)






