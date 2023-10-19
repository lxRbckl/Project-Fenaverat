# import <
from os import path
from dash import Dash
from json import load, dump
import dash_bootstrap_components as dbc

# >


# global <
realpath = path.realpath(__file__)
directory = ('/'.join(realpath.split('/')[:-2]))
application = Dash(

    suppress_callback_exceptions = True,
    external_stylesheets = [dbc.themes.BOOTSTRAP]

)
server = application.server

# >


# function <
def jsonLoad(file: str) -> dict:
    '''  '''

    # read file <
    # get data <
    with open(f'{directory}{file}', 'r') as fileIn:

        return load(fileIn)

    # >

def jsonDump(file: str, data: dict) -> None:
    '''  '''

    # write file <
    # set data <
    with open(f'{directory}{file}', 'w') as fileOut:

        dump(data, fileOut, indent = 3)

    # >

# >
