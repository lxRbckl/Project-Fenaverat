# < Project Fenaverat 3 by Alex Arbuckle > #


# import <
from backend.database import database
from frontend.layout.header import header
from frontend.layout.footer import footer
from frontend.layout.framework import framework
from frontend.layout.body.aboutMe import aboutMe
from backend.resource import (server, application)
from frontend.layout.body.myServers import myServers
from frontend.layout.body.myProjects import myProjects

# >


obj = framework()
obj.header = header()
obj.footer = footer()
obj.database = database()
obj.body = {
   
   'aboutMe' : aboutMe(),
   'myServers' : myServers(),
   'myProjects' : myProjects()
   
}


obj.registerIntervalCallback()
application.layout = obj.framework()





if (__name__ == '__main__'): application.run(debug = True)