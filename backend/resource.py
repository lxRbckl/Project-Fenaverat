# import <
from dash import Dash
from lxrbckl.local import getProjectPath
from dash_bootstrap_components import themes

# >


# setup <
# initialize <
colWidth = 8
refreshRate = 30
defaultBoard = 'b1'
projectPath = getProjectPath()
tooltipResponse = 'this is an example of a tooltip message.'

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


# connections <
connections = {
   
   'ala2q6' : 'https://github.com/ala2q6',
   'lxRbckl' : 'https://github.com/lxRbckl',
   'Email' : 'mailto:lxrbckl@protonmail.com',
   'LeetCode' : 'https://leetcode.com/lxRbckl/',
   'LinkedIn' : 'https://www.linkedin.com/in/lxRbckl/'
   
}

# >


# remote <
remote = {
   
   'style' : {
      
      'footer' : 'https://raw.githubusercontent.com/lxRbckl/Project-Fenaverat/Project-Fenaverat-3/frontend/style/footer.json',
      'header' : 'https://raw.githubusercontent.com/lxRbckl/Project-Fenaverat/Project-Fenaverat-3/frontend/style/header.json',
      'content' : 'https://raw.githubusercontent.com/lxRbckl/Project-Fenaverat/Project-Fenaverat-3/frontend/style/content.json',
      'template' : 'https://raw.githubusercontent.com/lxRbckl/Project-Fenaverat/Project-Fenaverat-3/frontend/style/template.json'
      
   },
   'data' : {
      
      'header' : 'https://raw.githubusercontent.com/lxRbckl/Project-Fenaverat/Project-Fenaverat-3/data/header.json',
      'footer' : 'https://raw.githubusercontent.com/lxRbckl/Project-Fenaverat/Project-Fenaverat-3/data/footer.json',
      'aboutMe' : 'https://raw.githubusercontent.com/lxRbckl/Project-Fenaverat/Project-Fenaverat-3/data/body/aboutMe.json',
      'myServer' : 'https://raw.githubusercontent.com/lxRbckl/Project-Fenaverat/Project-Fenaverat-3/data/body/myServer.json',
      'myProject' : 'https://raw.githubusercontent.com/lxRbckl/Project-Fenaverat/Project-Fenaverat-3/data/body/myProject.json'
      
   }
   
}

# >