import pickle


def importData():
    file = open('grades.pkl', 'rb')
    data = pickle.load(file)
    file.close()
    return data


def exportData(data):
    file = open('grades.pkl', 'wb')
    pickle.dump(data, file)
    file.close()


class Subject:
    def __init__(self, name):
        self.name = name
        self.marks = []

    def __repr__(self):
        return f"{self.name} {self.marks}"

    def addMark(self, mark):
        # adds a mark to the list of marks, stored in Object property 'marks'
        try:
            mark = float(mark)
            self.marks.append(mark)
            print(f"The '{mark}' mark was successfully added")
        except ValueError:
            print("Type a number, not a string!")

    def removeMark(self, index):
        # removes a mark from the list of marks, stored in Object property 'marks'
        try:
            index = int(index)
            try:
                self.marks.pop(index)
                print("The mark was successfully removed")
            except IndexError:
                print("There is no such index! Try again")
        except ValueError:
            print('Type a natural number!')


def changeMarks(subject):
    if subject in subjects:
        comnd = input("Type '1' to add a mark\nType '2' to delete a mark\n")
        if comnd == '1':
            mark = input("Type a mark: ")
            subjects[subject].addMark(mark)
        elif comnd == '2':
            if subjects[subject].marks:
                for (i, j) in enumerate(subjects[subject].marks):
                    print(f'{i}. {j}')
                index = input('Choose an index of mark you want to delete: ')
                subjects[subject].removeMark(index)
            else:
                print("There aren't any marks! Try again")
        else:
            print(f"'{comnd}' is not recognized as command! Try again")
    else:
        print(f"There is no such subject! Try again")


def changeSubjects(comnd):
    if comnd == '1':
        subject = input("Type a name of subject you want to add: ")
        addSubject(subject)
    elif comnd == '2':
        subject = input("Choose a name of subject you want to delete: ")
        removeSubject(subject)
    else:
        print(f"'{comnd}' is not recognized as command! Try again")


def addSubject(subject):
    # creates a Subject object and adds it to the dictionary, using its name as a key
    newsub = Subject(subject)
    subjects[subject] = newsub
    print(f"The '{subject}' was successfully added")


def removeSubject(subject):
    # removes a Subject object from the dictionary by its key
    try:
        subjects.pop(subject)
        print(f"The '{subject}' was successfully removed")
    except KeyError:
        print("There is no such subject! Try again")


print("Welcome to MyGradebook - an application for teachers for grading students!\n")
subjects = importData()
if not subjects:
    print("Let's create your first gradebook!\nType a name of subject you want to add\nIn the end type 'stop' to save"
          " changes")
    while True:
        namesub = input("Subject: ")
        if namesub == 'stop':
            break
        addSubject(namesub)
while True:
    print("\nCurrent marks:")
    for x in subjects:
        print(subjects[x])
    comnd = input("Type '1' to add or remove marks\nType '2' to add or remove subjects\n"
                  "Type 'exit' to exit application\n")
    if comnd == '1':
        print("\nType a name of subject to choose it\nType 'stop' to save changes and return to the main menu")
        while True:
            namesub = input('Subject: ')
            if namesub == 'stop':
                break
            changeMarks(namesub)
    elif comnd == '2':
        while True:
            comnd = input("\nType '1' to add a subject\nType '2' to remove a subject\nType 'stop' to save changes and"
                          " return to the main menu\n")
            if comnd == 'stop':
                break
            changeSubjects(comnd)
    elif comnd == 'exit':
        print("Well, see you next time")
        exportData(subjects)
        break
    else:
        print(f"'{comnd}' is not recognized as command! Try again")
