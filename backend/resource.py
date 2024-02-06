# import <
from dash import Dash
from lxrbckl.local import getProjectPath
from dash_bootstrap_components import themes

# >


# setup <
# initialize <
refreshRate = 30
projectPath = getProjectPath()

application = Dash(
   
   name = 'lxRbckl',
   title = 'lxRbckl',
   suppress_callback_exceptions = True,
   assets_folder = (projectPath + 'backend/assets'),
   external_stylesheets = [
      
      themes.GRID,
      themes.BOOTSTRAP
      
   ]
   
)
server = application.server

# >


# remote <
remote = {
   
   'data' : {
      
      
      
   },
   'style' : {
      
      
      
   }
   
}

# >