from datetime import datetime

class NotAllowed(Exception):
    pass

def greet_goodday_decorator(func):
    def wrapper(*args, **kwargs):
        print("GoodDay decorator")
        print("welcome to decorators class")
        func(*args, **kwargs)
        print("Have a great Day!")
    return wrapper

def after1pmdeny(func):
    def wrapper(*args, **kwargs):
        now = datetime.now().hour
        try:
            if now > 15:
                raise Exception("Not Allowed")
            else:
                func(*args, **kwargs)
        except Exception.NotAllowed:
            print("Not Allowed to watch after 3 pm")
        except Exception as e:
            print(e)
    return wrapper()


def greet_decorator(func):
    def wrapper(*args, **kwargs):
        print("Greet decorator")
        func(*args, **kwargs)
        print("Good Evening")
    return wrapper

def greet_eve():
    print("Good Evening")

# @after1pmdeny
@greet_goodday_decorator
@greet_decorator
def greet_all():
    print("Hello all")
    # greet_eve()

if __name__ == "__main__":
    greet_all()
