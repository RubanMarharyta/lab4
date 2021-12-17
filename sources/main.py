from engine import Note

print(
    "enter operation and action: save-note; show(show list); edit-number; delete-number. enter exit to finish program")
print('example: save-dont forget buy a milk!, delete-3')

while 1:
    act = input()

    if act == 'exit':
        break

    if act == '':
        print('enter something')
        continue

    if act.split('-')[0] == 'save':
        a = Note.add(act.split('-')[1])

    elif act.split('-')[0] == 'show':
        Note.show()

    elif act.split('-')[0] == 'edit':
        enter = input('enter new note ')
        Note.edit(act.split('-')[1], enter)

    elif act.split('-')[0] == 'delete':
        Note.delete(act.split('-')[1])

    else:
        print("Please use command")




