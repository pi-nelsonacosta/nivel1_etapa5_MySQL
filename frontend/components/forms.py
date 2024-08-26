from fasthtml.common import *
from fasthtml.components import Form, Input, Button

def login_form():
    return Form(
        Input(id='username', placeholder='Username'),
        Input(id='password', type='password', placeholder='Password'),
        Button('Login', type='submit'),
        action='/login', method='post'
    )

def character_form():
    return Form(
        Input(id='name', placeholder='Character Name'),
        Input(id='description', placeholder='Character Description'),
        Button('Add Character', type='submit'),
        action='/characters/add', method='post'
    )
