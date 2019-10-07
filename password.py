#/usr/bin/env python3.6
from user import User

def create_user(user_name,password):
    '''
    Function to create a new user
    '''
    new_user = User(user_name,password)
    return new_user

def save_user(user):
    '''
    Function to save user
    '''
    user.save_user()

def del_user(user):
    '''
    Function to delete a user
    '''
    user.delete_user()

def find_user(name):
    '''
    Function that finds a user by name and returns the user
    '''
    return User.find_by_name(name)


