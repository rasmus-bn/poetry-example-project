from myapp.module1.greeting import english

def start():
    print(f'Hello from {__name__}!')
    print(english())


if __name__ == '__main__':
    start()