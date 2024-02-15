# < Project Fenaverat 3 by Alex Arbuckle > #


# import <
from frontend.layout.template import template
from backend.resource import (server, application)

# >


obj = template()
obj.registerCallbacks()
application.layout = obj.component()


if (__name__ == '__main__'): application.run(debug = True)