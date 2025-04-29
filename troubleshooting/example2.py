def greeting(name: str) -> str:
    return 'Hello ' + name

def number_print(x: int, y: int) -> None:
    print(x + y)

print(greeting('Dylan'))

number_print(4, 5)

def name_printer(name: str, uppercase: bool = False) -> None:
    if uppercase == True:
        print(name.upper())
    else:
        print(name)

name_printer('dylan', uppercase=True)
