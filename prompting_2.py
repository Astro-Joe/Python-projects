from sys import argv
script = argv
prompt = '> '
username = input('Enter your name: ')

print(f"Hi {username}, I'm the {script} script.")
print("I'd like to ask you a few questions")
print(f"Do you like me {username}?")
likes = input(prompt)

print(f"Where do you live {username}?")
lives = input(prompt)
if username == 'Deborah' or 'Debbie' and likes == 'Yes':
    print(f"""
    Alright, so you said {likes} about liking me. That's cool!
    You live in {lives}. Not sure where that is. Anyways thanks for running thus program
    """)
else:
     print(f"""
    Alright, so you said {likes} about liking me. I didn't think you would tho.
    You live in {lives}. Not sure where that is. Anyways thanks for running this program
    """)