import pytest
from madlib_cli.madlib import read_template, parse_template, merge, create_new_file
from os.path import exists
import os



def test_read_template_returns_stripped_string():
    actual = read_template("assets/dark_and_stormy_night_template.txt")
    expected = "It was a {Adjective} and {Adjective} {Noun}."
    assert actual == expected

#@pytest.mark.skip("pending")
def test_parse_template():
    actual_stripped, actual_parts = parse_template(
        "It was a {Adjective} and {Adjective} {Noun}."
    )
    expected_stripped = "It was a {} and {} {}."
    expected_parts = ("Adjective", "Adjective", "Noun")

    assert actual_stripped == expected_stripped
    assert actual_parts == expected_parts


#@pytest.mark.skip("pending")
def test_merge():
    actual = merge("It was a {} and {} {}.", ("dark", "stormy", "night"))
    expected = "It was a dark and stormy night."
    assert actual == expected


def test_create_new_file():
    file = create_new_file('text_file.txt','HERE IS CONTENT IN FILE')
    file_was_created = exists(file.name)
    # delete file after testing function
    if(os.path.exists(file.name)):
        os.remove(file.name)
    assert(file_was_created == True)

def test_create_new_file_has_correct_content():
    expected = 'HERE IS CONTENT IN FILE'
    actual = ''
    file = create_new_file('text_file.txt','HERE IS CONTENT IN FILE')

    if(file and exists(file.name)):
        actual = file.read()
    # delete file after testing function
    if(os.path.exists(file.name)):
        os.remove(file.name)
    assert(expected == actual)


#@pytest.mark.skip("pending")
def test_read_template_raises_exception_with_bad_path():

    with pytest.raises(FileNotFoundError):
        path = "missing.txt"
        read_template(path)
