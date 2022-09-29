def add(*numbers_to_be_added):
    """A function to add values.
    At least two arguments are need for this function to work.
    :rtype: object"""
    i = 0
    final_num = 0
    # for i in range(len(numbers_to_be_added)):
    #     final_num += numbers_to_be_added[i]

    if len(numbers_to_be_added) != 1:
        while i < len(numbers_to_be_added):
            final_num += numbers_to_be_added[i]
            i += 1
        return final_num
    else:
        print('Two numbers are required!')


def sub(*numbers_to_be_sub):
    """A function to subtract values.
    At least two arguments are needed for this function to work"""
    if len(numbers_to_be_sub) != 1:
        i = 2
        value = numbers_to_be_sub[0] - numbers_to_be_sub[1]
        while i < len(numbers_to_be_sub):
            value -= numbers_to_be_sub[i]
            i += 1
        return value
    else:
        print('Two numbers are required!')
