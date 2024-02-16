# import <
from dash import Dash
from dash_bootstrap_components import themes

# >


# setup <
application = Dash(
   
   name = 'lxRbckl',
   title = 'lxRbckl',
   assets_folder = 'backend/assets',
   suppress_callback_exceptions = True,
   external_stylesheets = [
      
      themes.GRID,
      themes.BOOTSTRAP
      
   ]
   
)
server = application.server

# >