from rich import print as rprint

def my_first_function(func):
    def my_second_function():
        print('BEGINNING TO EXECUTE THE FUNCTION')
        func()
        print('THE FUNCITON HAS FINISHED EXECUTING')

    return my_second_function

@my_first_function
def greeter():
    print('Hello my name is Dylan, very nice to meet you!')

greeter()

def prettify(func):
    def wrapper():
        rprint("[cyan]***************[/cyan]")
        func()
        rprint("[cyan]***************[/cyan]")
    
    return wrapper

@prettify
def banner():
    print('DO NOT ACCESS THIS DEVICE UNLESS YOU ARE AUTHORIZED')

banner()

def politeness(func):
    def wrapper(*args, **kwargs):
        rprint('[yellow]Hello, thank you for using my code![/yellow]')
        func(*args, **kwargs)
        rprint('[green]Thanks, again! Hope to see you soon![/green]')

    return wrapper

@politeness
def nameprinter(name):
    print(f'Your name is {name}')

@politeness
def adder(num1, num2):
    print(num1 + num2)

nameprinter('Dylan')
adder(4, 5)
