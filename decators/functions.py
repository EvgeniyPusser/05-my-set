from hand_made_decorator import my_logger

@my_logger
def hello(name = 'World'):
    """This function say hello to someone"""
    return f'Hello {name}!'

greet1 = hello

print(greet1('John'))

def apply_callback(callback, name):
    return callback(name)

print(apply_callback(greet1, 'Peter'))

def get_greeter(greeting):
    def greet(name):
        return f'{greeting} {name}!'
    return greet

greet_aloha = get_greeter('Aloha')
print(greet_aloha('Alice'))

# Closure

nick_name = 'Jose'

def greeting():
    # nick_name = 'Peter'
    def fn1():
        # nick_name = 'Jone'
        print(nick_name)
    return fn1

nick_name = 'Rabindranate'
hello1 = greeting()
hello1()