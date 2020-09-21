data = {
    "login1": "password1",
    "login2": "password2",
    "login3": "password3",
    "login4": "password4",
    "login5": "password5",
    "login6": "password6",
    "login7": "password7",
    "login8": "password8",
}


def decorator(function):
    def wrapper_decorator(*args, **kwargs):
        print("Please, enter your login!")
        input_login = input()
        print("Please, enter your password!")
        input_password = input()
        if input_login not in data or data[input_login] != input_password:
            return "Authentication required"
        value = function(*args, **kwargs)
        return value

    return wrapper_decorator


@decorator
def some_func(a, b):
    return a ** b


# To use VS code comment 32-33 and use 36
if __name__ == "__main__":
    print(some_func(10, 10))

# print(some_func(10,10))
