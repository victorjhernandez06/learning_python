##microsoft
#print the current time

def print_time():
    print('Task completed')
    print(datetime.now())
    print()

firs_name = 'Sofia'
print_time() 

for x in range(0,10):
    print(x)
print_time()

    
"""Pass the task name as a parameter"""
#print the current time and task name
def print_time(task_name):
    print(task_name)
    print(datetime.now())
    print()
first_name = 'Sofia'
print_time('first name assigned')

for x in range (0,10):
    print(x)
print_time('Loop Completed')
    

## Fix the next code.
first_name = input('Enter your first name: ')
first_name_initial = first_name[0:1]

last_name  = input('Enter your last name: ')
last_name_initial =  last_name[0:1]

print('Your initials are: ' + first_name_initial + last_name_initial)
#imprime las iniciales de los nombres tipeados.

## Functions that return values allow clever code, but you migth trade readability for less code.

def get_initial(name):
    initial = name[0:1].upper()
    return initial

first_name = input('Enter your first name: ')
last_name = input('Enter your last name: ')
print('Your initial are: '+ get_initial(first_name) + get_initial(last_name))


##Functions With parameters

def get_initial(name, force_uppercase=True):
    if force_uppercase:
        initial = name[0:1].upper()
    else:
        initial = name[0:1]
    return initial

first_name = input('Enter your name: ')
first_name_initial =  get_initial(first_name)

print(f'Your initial name is: {first_name_initial}')

#You can also assign the values to  parameters by name whe you call the function

def get_initial(name, force_uppercase):
    if force_uppercase:
        initial = name[0:1].upper()
    else:
        initial = name[0:1]
    return initial
first_name =  input('enter your first name: ')
first_name_initial = get_initial(force_uppercase=True, name=first_name)
print(f'Your initial is: {first_name_initial}')

#Using the named notation when calling functions makes your code more readable
# def error_logger(error_code, error_severity, log_to_db, error_message, source_module):
#     print(f'oh no error {error_message}')
#     #imagine code here that logs our error to database a file.
    
# first_number = 10
# second_number = 5
# if first_number > second_number:
#     error_logger(45, 1, True, 'second number than first','may_math_method')


def error_logger(error_code, error_severity, log_to_db, error_message, source_module):
    print('oh no error:' + error_message)
    #imagine code here that logs our error to database or file
    
first_number = 10
second_number = 5
if first_number > second_number:
    error_logger(error_code = 45, error_severity=1, log_to_db = True, error_message= 'second number greater than first', source_module='May math method')