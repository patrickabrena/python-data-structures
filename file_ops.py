def read_file(file_name):
    """ Reads in a file.

    [IMPLEMENT ME]
        1. Open and read the given file into a variable using the File read()
           function
        2. Print the contents of the file
        3. Return the contents of the file

    Args:
        file_name: the name of the file to be read

    Returns:
        string: contents of the given file.
    """
    ### WRITE SOLUTION HERE
    
    with open(file_name, "r") as file:
        r_file = file.read()
        print(r_file)
        return r_file

    

    #raise NotImplementedError()

def read_file_into_list(file_name):
    """ Reads in a file and stores each line as an element in a list

    [IMPLEMENT ME]
        1. Open the given file
        2. Read the file line by line and append each line to a list
        3. Return the list

    Args:
        file_name: the name of the file to be read

    Returns:
        list: a list where each element is a line in the file.
    """
    ### WRITE SOLUTION HERE
    with open(file_name, "r") as file:
        list = file.readlines()
        return list

    #raise NotImplementedError()

def write_first_line_to_file(file_contents, output_filename):
    """ Writes the first line of a string to a file.

    [IMPLEMENT ME]
        1. Get the first line of file_contents
        2. Use the File write() function to write the first line into a file
           with the name from output_filename

        We determine the first line to be everything in a string before the
        first newline ('\n') character.

    Args:
        file_contents: string to be split and written into output file
        output_filename: the name of the file to be written to
    """
    ### WRITE SOLUTION HERE
    split_lines = file_contents.split("\n")
    with open(output_filename, "w") as file:
        file.write(split_lines[0])

    #raise NotImplementedError()


def read_even_numbered_lines(file_name):
    """ Reads in the even numbered lines of a file

    [IMPLEMENT ME]
        1. Open and read the given file into a variable
        2. Read the file line-by-line and add the even-numbered lines to a list
        3. Return the list

    Args:
        file_name: the name of the file to be read

    Returns:
        list: a list of the even-numbered lines of the file
    """
    ### WRITE SOLUTION HERE
    with open(file_name, "r") as file:
        read_file = file.readlines()
        even_lines = []
        for lines in range(len(read_file)):
            if lines % 2 != 0:
                even_lines.append(read_file[lines])
        

    #raise NotImplementedError()

def read_file_in_reverse(file_name):
    """ Reads a file and returns a list of the lines in reverse order

    [IMPLEMENT ME]
        1. Open and read the given file into a variable
        2. Read the file line-by-line and store the lines in a list in reverse order
        3. Print the list
        4. Return the list

    Args:
        file_name: the name of the file to be read

    Returns:
        list: list of the lines of the file in reverse order.
    """
    ### WRITE SOLUTION HERE
   
    #initialize empty list
    li = []
    #read file into list using for loop
    with open(file_name, 'r') as file:
        for x in file:
            li.append(x)
    
    #Use stack-like approach to reverse the list
    #init a new list(array)
    reversed_list = []
    while li: #while there are still eements in li, keep appending the popped elements from li array into 
        reversed_list.append(li.pop())
    #print(reversed_list)
    return reversed_list


    #raise NotImplementedError()


'''
Here are some sample commands to help you run/test your implementations.
Feel free to uncomment/modify/add to them as you wish.
'''
def main():
    file_contents = read_file("sampletext.txt")
    print(read_file_into_list("sampletext.txt"))
    write_first_line_to_file(file_contents, "online.txt")
    print(read_even_numbered_lines("sampletext.txt"))
    print(read_file_in_reverse("sampletext.txt"))

if __name__ == "__main__":
    main()




#Function read_file
#All test cases passed.
#Function read_file_into_list
#Short file test did not pass.
#Expected (newlines added for legibility):
#
#['Because I could not stop for Death,\n', 'He kindly stopped for me;\n', 'The carriage held but just ourselves\n', 'And Immortality.']
#
#Got (newlines added for legibility):
#
#['Because I could not stop for Death,', 'He kindly stopped for me;', 'The carriage held but just ourselves', 'And Immortality.']
#
#
#Long file test did not pass.
#Expected (newlines added for legibility):
#
#['Let me not to the marriage of true minds\n', 'Admit impediments. Love is not love\n', 'Which alters when it alteration finds,\n', 'Or bends with the remover to remove:\n', 'O, no! it is an ever-fix`ed mark,\n', 'That looks on tempests and is never shaken;\n', "It is the star to every wand'ring bark,\n", "Whose worth's unknown, although his heighth be taken.\n", "Love's not Time's fool, though rosy lips and cheeks\n", "Within his bending sickle's compass come;\n", 'Love alters not with his brief hours and weeks,\n', 'But bears it out even to the edge of doom:\n', 'If this be error and upon me proved,\n', 'I never writ, nor no man ever loved.']
#
#Got (newlines added for legibility):
#
#['Let me not to the marriage of true minds', 'Admit impediments. Love is not love', 'Which alters when it alteration finds,', 'Or bends with the remover to remove:', 'O, no! it is an ever-fix`ed mark,', 'That looks on tempests and is never shaken;', "It is the star to every wand'ring bark,", "Whose worth's unknown, although his heighth be taken.", "Love's not Time's fool, though rosy lips and cheeks", "Within his bending sickle's compass come;", 'Love alters not with his brief hours and weeks,', 'But bears it out even to the edge of doom:', 'If this be error and upon me proved,', 'I never writ, nor no man ever loved.']
#
#
#Empty file test did not pass.
#Expected (newlines added for legibility):
#
#[]
#
#Got (newlines added for legibility):
#
#['']
#
#
#Function write_first_line_to_file
#All test cases passed.
#Function read_even_numbered_lines
#Short file test did not pass.
#Expected (newlines added for legibility):
#
#['He kindly stopped for me;\n', 'And Immortality.']
#
#Got (newlines added for legibility):
#
#None
#
#
#Long file test did not pass.
#Expected (newlines added for legibility):
#
#['Admit impediments. Love is not love\n', 'Or bends with the remover to remove:\n', 'That looks on tempests and is never shaken;\n', "Whose worth's unknown, although his heighth be taken.\n", "Within his bending sickle's compass come;\n", 'But bears it out even to the edge of doom:\n', 'I never writ, nor no man ever loved.']
#
#Got (newlines added for legibility):
#
#None
#
#
#Single line file test did not pass.
#Expected (newlines added for legibility):
#
#[]
#
#Got (newlines added for legibility):
#
#None
#
#
#Empty file test did not pass.
#Expected (newlines added for legibility):
#
#[]
#
#Got (newlines added for legibility):
#
#None
#
#
#Function read_file_in_reverse
#Short file test did not pass.
#Expected (newlines added for legibility):
#
#['And Immortality.', 'The carriage held but just ourselves\n', 'He kindly stopped for me;\n', 'Because I could not stop for Death,\n']
#
#Got (newlines added for legibility):
#
#None
#
#
#Long file test did not pass.
#Expected (newlines added for legibility):
#
#['I never writ, nor no man ever loved.', 'If this be error and upon me proved,\n', 'But bears it out even to the edge of doom:\n', 'Love alters not with his brief hours and weeks,\n', "Within his bending sickle's compass come;\n", "Love's not Time's fool, though rosy lips and cheeks\n", "Whose worth's unknown, although his heighth be taken.\n", "It is the star to every wand'ring bark,\n", 'That looks on tempests and is never shaken;\n', 'O, no! it is an ever-fix`ed mark,\n', 'Or bends with the remover to remove:\n', 'Which alters when it alteration finds,\n', 'Admit impediments. Love is not love\n', 'Let me not to the marriage of true minds\n']
#
#Got (newlines added for legibility):
#
#None
#
#
#Single line file test did not pass.
#Expected (newlines added for legibility):
#
#['Because I could not stop for Death,']
#
#Got (newlines added for legibility):
#
#None
#
#
#Empty file test did not pass.
#Expected (newlines added for legibility):
#
#[]
#
#Got (newlines added for legibility):
#
#None