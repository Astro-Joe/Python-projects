prompt = "(Enter 'q' to quit) "
prompt+= "\nEnter your name: "
while True:
    name = input(prompt)
    if name == 'q':
        break 
    else:
        print('Welcome ' + name.title() + '\n')
        with open('guest.txt', 'a') as file_object:
            file_object.write(name.title() + '\n')




with open('guest.txt') as someWhat:
    content = someWhat.read()
    print(content.rstrip())