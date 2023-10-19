# Project Fenaverat by Alex Arbuckle #


# import <
from backend.resource import application, server
from frontend.layout.template import templateFunction

# >


# set layout <
application.layout = templateFunction()

# >


# main <
if (__name__ == '__main__'): application.run_server(debug = True)

# >
