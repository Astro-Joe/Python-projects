#from sys import argv
#script, filename = argv

#For this to work the file has to be in the same location as the python script
filename = input('Type the name of a valid file: ')
print(f'We are going to erase {filename}.')
print('If you don\'t want that, hit CRTL-C(^C).')
print('If you do want that, hit RETURN.')

input('? ')

print('opening the file...')
#If the file is valid it will open. If it isn't valid a new file would be created.
file_open = open(filename, 'r')
input('Press ENTER')

#There is no point truncating since the file is opened in write mode.
# print('Truncating the file. Goodbye!')
# file_open.truncate()
# input('Press ENTER')

print("Now I'm going to ask you to add few sentences to the file.")


print('............................................................')

print("Enter/Paste your content. Ctrl-D or Ctrl-Z ( windows ) to save it.")
#Allows multiple inputs of lines
while True:
    try:
        line = input()
        file_open.write(line + '\n')
    except EOFError:
        break
    

input()
print('\nFinally, we close the file')
file_open.close()

