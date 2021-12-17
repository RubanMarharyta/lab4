class Note:
    note_list = []

    def add(note):
        Note.note_list.append(note)

    def show():
        if Note.check():
            for i in range(len(Note.note_list)):
                print(str(i + 1) + "." + " " + Note.note_list[i], sep='\n')

    def edit(num, note):
        Note.note_list[int(num) - 1] = note

    def delete(num):
        if Note.check():
            del Note.note_list[int(num) - 1]

    def check():
        if Note.note_list:
            return 1
        else:
            print("list empty")
            return 0
