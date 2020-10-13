from views import render_template

from models import User, Phone


def default_controller(data=None, cls=True):
    """Default controller"""
    render_template(context={}, template="default.jinja2", cls=cls)
    return input(), None


def exit_controller(data=None, cls=True):
    render_template(context={}, template="exit.jinja2", cls=cls)
    exit()


def all_users_controller(data=None, cls=True):
    users = User.all()
    render_template(context={'users': users}, template="all_users.jinja2", cls=cls)
    input("Продолжить?")
    return 'main', None  # (next state, data)


def special_user_controller(data=None, cls=True):
    render_template(context={}, template="add_user.jinja2", cls=cls)
    name = input()
    users = User.temp(name)
    render_template(context={'users': users}, template="all_users.jinja2", cls=cls)
    input("Продолжить?")
    return 'main', None  # (next state, data)


def add_user_controller(data=None, cls=True):
    render_template(context={}, template="add_user.jinja2", cls=cls)
    username = input().strip().title()
    user = User.add(username)
    return 21, user  # (next state, data)


def add_phone_controller(user, cls=True):
    render_template(context={}, template="add_phone.jinja2", cls=cls)
    phone_number = input()
    phone = Phone.add(phone_number, user)
    return 212, user  # (next state, data)


def delete_user(data=None, cls=True):
    render_template(context={}, template="add_user.jinja2", cls=cls)
    user = input().strip().title()
    User.delete(user)
    return 51, None


def delete_phone(data=None, cls=True):
    render_template(context={}, template="add_phone.jinja2", cls=cls)
    phone = input()
    Phone.delete(phone)
    return 51, None


def update_phone(data=None, cls=True):
    render_template(context={}, template="add_phone.jinja2", cls=cls)
    phone = input()
    render_template(context={}, template="add_new_phone.jinja2", cls=cls)
    new_phone = input()
    Phone.update(phone, new_phone)
    return 51, None


def add_more_controller(user, cls=True):
    render_template(context={}, template="add_more.jinja2", cls=cls)
    answer = input().strip().title()
    if answer == 'Y':
        return 21, user
    return 51, user  # (next state, data)


def get_controller(state):
    return controllers_dict.get(state, default_controller)


controllers_dict = {  # use dict type instead of if else chain
    '0': exit_controller,
    '1': all_users_controller,
    '2': add_user_controller,
    '3': update_phone,
    '4': delete_user,
    '5': delete_phone,
    '6': special_user_controller,
    21: add_phone_controller,  # user can't enter 21 of int type
    212: add_more_controller,
    211: delete_phone,
}
