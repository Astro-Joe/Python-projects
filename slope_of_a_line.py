#This code calculates the slope of a line
x1 = float(input('Enter the value for x1: '))

x2 = float(input('Enter the value for x2: '))

y1 = float(input('Enter the value for y1: '))

y2 = float(input('Enter the value for x2: '))

change_in_x = x2 - x1
change_in_y = y2 - y1
if change_in_y == 0:
    print('horizontal line.')
else:
    slope = round((change_in_x/change_in_y),2)
    print('The slope is:,' + str(slope))
    if slope > 0:
        print('positive slope.')
    if slope < 0:
        print('negative slope.')
    if change_in_x == 0:
        print('vertical line.')
input() #This makes you see your result when it is run fron the command line
