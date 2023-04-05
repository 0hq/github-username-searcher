#!/usr/bin/python3

import itertools
import sys
import requests
from multiprocessing import Pool

def make_request(username):
    """
    This function sends a request to Github and returns the status code. If a username has been registered, we'll get a 200 status code. If the username is available/banned, we'll get a 404 status code.
    """
    user = username.strip()
    status = requests.get(f"https://github.com/{user}").status_code
    result = {"user": user, "data": status}
    if status == 404:
        print(user)
    return result

def generate_usernames(length):
    """
    This function generates all possible usernames of the given length using lowercase letters.
    """
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    return (''.join(i) for i in itertools.product(alphabet, repeat=length))

def read_dictionary(file_name):
    """
    This function reads words from a dictionary file and returns them as a list.
    """
    with open(file_name, 'r') as file:
        return [line.strip() for line in file]

if __name__ == '__main__':
    # Set how many threads you want
    num_threads = 100
    pool = Pool(processes=num_threads)

    # Set the dictionary file name
    dictionary_file = 'dictionary.txt'

    # Set the length of the usernames you want to check
    username_length = 4

    # Choose the method of username generation: dictionary (True) or n-letter combinations (False)
    use_dictionary = True

    try:
        if use_dictionary:
            # Read words from the dictionary file
            words = read_dictionary(dictionary_file)
            usernames = words
        else:
            # Generate all possible usernames of the given length
            usernames = generate_usernames(username_length)

        # Map the make_request function to the list of usernames
        results = pool.map(make_request, usernames)
        for res in results:
            print(res)
    except KeyboardInterrupt:
        sys.exit()
