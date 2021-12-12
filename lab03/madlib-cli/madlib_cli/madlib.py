import os
import re
import textwrap

def read_template(file_path):
    """Reads a madlib template file and returns the content as a string

    Args:
        file_path (string): File path to the madlib template file

    Raises:
        FileNotFoundError: Error thrown if template file not found

    Returns:
        [string]: The content of the madlib template file
    """    
    # get current directory name 
    # Reference - https://stackoverflow.com/questions/5137497/find-the-current-directory-and-files-directory
    dir_path = os.path.dirname(os.path.realpath(__file__))
    try:
        with open(dir_path + '/' + file_path) as file:
            content = file.read()
            return content
    except FileNotFoundError as e:
        print(e)
        raise FileNotFoundError


def parse_template(template):
    """Parses the template and returns a list containing the strippled template
    as the first element and a tuple containing madlib parts as the second element

    Args:
        template (string): Content of a madlib template file

    Returns:
        list: List contains stripped template and tuple of madlib parts
    """    
    stripped = ''
    madlib_parts = []
    for line in template.splitlines():
        # regex finds all words in current line of the form -> {word}
        matches = re.findall(r"{(.*?)}", line)
        for match in matches:
            madlib_parts.append(match)  
        stripped += re.sub(r"{(.*?)}", '{}', line)
    return [stripped, tuple(madlib_parts)]


def merge(stripped_template, madlib_parts):
    """Merges a stripped madlib template with words to generate a new madlib.

    Args:
        stripped_template (string): Madlib template stripped of word identifiers
        madlib_parts (list): All words that have been entered by user to fill madlib

    Returns:
        string: Completed madlib
    """    
    merged_string = stripped_template
    for part in madlib_parts:
        merged_string = re.sub('{}', part, merged_string, 1)
    return merged_string


def prompt_for_template_path():
    """Prompt a user to enter a path to the desired madlib template file.

    Returns:
        string: Returns the path entered by user
    """    
    print('Enter the path to the template file')
    template_path = input('> ')
    return template_path


def prompt_for_madlib_input(template_parts):
    """Prompts the user to enter words for each of the madlib template parts

    Args:
        template_parts (list): All template parts

    Returns:
        list: Returns list of all user input
    """    
    madlib_input = []
    for part in template_parts:
        if isVowel(part[0:1]): # check if first letter is vowel
            print('Enter an ', part)
        else:
            print('Enter a ', part)
        madlib_input.append(input('> '))
    return madlib_input


def create_new_file(file_name, content):
    """Creates a new file

    Args:
        file_name (string): Name of new file to create
        content (string): Content that will be written to new file
    """    
    try:
        dir_path = os.path.dirname(os.path.realpath(__file__))
        with open(dir_path + '/assets/' + file_name , 'w') as output_file:
            output_file.write(content)
            return output_file
    except Exception as e:
        print('Error writing new file:', e)

     
def print_welcome_msg(): 
    print('-----| Welcome to Madlib-CLI |-----')
    intro = '''
    Mad Libs is a word game where one player prompts another for a list of words to substitute for blanks in a story.
    These word substitutions have a humorous effect when the resulting story is then read aloud.
    Madlib-CLI allows you to use a Mad Lib template file to create your own Mad Lib!
    '''
    print(textwrap.dedent(intro))

def isVowel(char):
    """[summary]

    Args:
        char ([type]): [description]

    Returns:
        [type]: [description]
    """    
    vowels = {'a','e','i','o','u','A','E','I','O','U'}
    return char in vowels
    

if __name__ == "__main__":
    print_welcome_msg()
    template_path = prompt_for_template_path()
    template = read_template(template_path)
    template_stripped, template_parts = parse_template(template)
    madlib_input = prompt_for_madlib_input(template_parts)
    madlib_result = merge(template_stripped, madlib_input)

    # Output new file containing madlib
    print('Enter name of new file for generated madlib')
    madlib_file_name = input('> ')
    create_new_file(madlib_file_name, madlib_result)
  
    
   


