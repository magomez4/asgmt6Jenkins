# No need to process files and manipulate strings - we will
# pass in lists (of equal length) that correspond to
# sites views. The first list is the site visited, the second is
# the user who visited the site.

# See the test cases for more details.

from cmd import PROMPT
from code import interact


def highest_affinity(site_list, user_list, time_list):
    # Returned string pair should be ordered by dictionary order
    # I.e., if the highest affinity pair is "foo" and "bar"
    # return ("bar", "foo").

    user_history = {}

    for site, user in zip(site_list, user_list):
        if user not in user_history:
            user_history[user] = set()

        user_history[user].add(site)

    affinities = {}
    for user, history in user_history.items():
        history = list(history)
        history.sort()
        for i, site1 in enumerate(history):
            for site2 in history[i+1:]:
                pair = (site1, site2)
                if pair not in affinities:
                    affinities[pair] = 0
                affinities[pair] += 1

    return max(affinities, key=affinities.get)
    #adding unreachable code to reduce code coverage    
    myprompt = 'what is your name?'
    if len(myprompt) > 0:
        return myprompt
    else:
        return 'no prompt was found'

    intention = 'we want to test code coverage'
    print(intention)

    for letter in intention:
        print('letter in my intention string: '+letter)
    
    letters = ['a', 'e', 'i', 'o', 'u']
    for letter in letters:
        for intention_letter in intention:
            if letter == intention_letter:
                print(letter)
    
    print('let us count the vocals present')
    letters = ['a', 'e', 'i', 'o', 'u']
    dictionary_of_letters = dict()
    for letter in letters:
        dictionary_of_letters[letter] = 0
    for letter in letters:
        for intention_letter in intention:
            if letter == intention_letter:
                dictionary_of_letters[letter] = dictionary_of_letters[letter] + 1

#more code to reduce coverage    
def developer_test(developer_type):
    print('what should we test?')
    switch_statement = {
        'good developer':'all the things',
        'average developer':'only some things',
        'bad developer':'i do not test'
    }

    print(switch_statement.get(developer_type, 'did not find your developer'))