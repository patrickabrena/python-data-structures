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
        list = file.read().split("\n")
        #print(list)
        #print(list[1]) #testing to see if it prints second line
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
    # so need to write the first line of file_content and write it to output_filename variable
    # islolate first line, try print(list[0]) to see if it appears in the console
    file_contents_list = file_contents.split("\n")
    the_first_line = file_contents_list[0]
    with open(output_filename, "w") as file:
        file.write(the_first_line)
        

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
    # use with open() and read file_name into some variable
    # read the file line by line using .split method into another variable
    # use a for loop to iterate through the length of that list generated from the split method
    # use modulo operator to add that element to another list that will be returned at the end

    # init indices_to_remove = []
    indices_to_remove = []

    with open(file_name, "r") as file:
        contents_in_list = file.read().split("\n")

        #for i in len(contents_in_list): # this isn't right, need to have range() wrapped around the len()
        for i in range(len(contents_in_list)):

            if (i%2 != 0): # condition to pass the current iteration if i % 2 does not equal 0. (pretty much exclude odd numbers)
                indices_to_remove.append(i)

        print(indices_to_remove)
    
    print(contents_in_list)
        
        

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
    # need to init an empty array "lines_reversed"
    # need to use split method to put each line in a list
    # need for loop to iterate through the original list then pop the element of the array and put it in the lines_reversed array
    lines_reversed = []

    with open(file_name, "r") as file:
    #create line variable and apply read() on file and .split() method on that file.read()
        lines = file.read().split("\n")

    while lines:
        line = lines.pop()
        lines_reversed.append(line)

    print(lines_reversed)


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