calls = 0
def counts_calls():
    global calls
    calls += 1
     
def string_info(string):

    string_info = [len(string), string.upper(), string.lower()]
    counts_calls()
    return string_info

def is_contains(string, list_to_search):
    string = string.lower()
    list_to_search = [s.lower() for s in list_to_search]
 
    if string in list_to_search:
        is_contains = True
    else:
        is_contains = False
    counts_calls()
    return is_contains
             
print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN']))
print(is_contains('cycle', ['recycling', 'cyclic']))

print(calls)