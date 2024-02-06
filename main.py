# < Project Fenaverat 3 by Alex Arbuckle > #


# import <
from frontend.layout.template import fTemplate
from backend.resource import (server, application)

# >


application.layout = fTemplate()


if (__name__ == '__main__'): application.run()