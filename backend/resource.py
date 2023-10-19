# import <
from os import path
from dash import Dash
from lxRbckl import requestsGet
from dash_bootstrap_components import themes

# >


# global <
gRefreshRate = 5
gPath = path.realpath(__file__)
gFilter = ('library', 'language', 'toolkit')
gDirectory = '/'.join(gPath.split('/')[:-2])
application = Dash(

    name = 'lxRbckl',
    title = 'lxRbckl',
    suppress_callback_exceptions = True,
    external_stylesheets = [themes.GRID],
    assets_folder = f'{gDirectory}/backend/asset'

)
server = application.server
gBootLink = {

    # data <
    # style <
    'aboutMeFeed' : 'https://raw.githubusercontent.com/lxRbckl/lxRbckl/main/feed.json',
    'myProjectData' : 'https://raw.githubusercontent.com/lxRbckl/Project-Heimir/main/data.json',
    'myServerData' : 'https://raw.githubusercontent.com/lxRbckl/Project-Acta-Mea-4/main/data.json',
    'frameData' : 'https://raw.githubusercontent.com/lxRbckl/Project-Fenaverat-2/main/backend/data/frame.json',
    'badgeData' : 'https://raw.githubusercontent.com/lxRbckl/Project-Fenaverat-2/main/backend/data/badge.json',
    'aboutMeData' : 'https://raw.githubusercontent.com/lxRbckl/Project-Fenaverat-2/main/backend/data/aboutMe.json',

    'cardStyle' : 'https://raw.githubusercontent.com/lxRbckl/Project-Fenaverat-2/main/frontend/style/card.json',
    'feedStyle' : 'https://raw.githubusercontent.com/lxRbckl/Project-Fenaverat-2/main/frontend/style/feed.json',
    'loadStyle' : 'https://raw.githubusercontent.com/lxRbckl/Project-Fenaverat-2/main/frontend/style/load.json',
    'frameStyle' : 'https://raw.githubusercontent.com/lxRbckl/Project-Fenaverat-2/main/frontend/style/frame.json',
    'badgeStyle' : 'https://raw.githubusercontent.com/lxRbckl/Project-Fenaverat-2/main/frontend/style/badge.json',
    'searchStyle' : 'https://raw.githubusercontent.com/lxRbckl/Project-Fenaverat-2/main/frontend/style/search.json',
    'templateStyle' : 'https://raw.githubusercontent.com/lxRbckl/Project-Fenaverat-2/main/frontend/style/template.json'

    # >

}


def getFunction(

        isJSON: bool = True,
        pLink: dict = gBootLink

): return {k : requestsGet(pLink = v, isJSON = isJSON) for k, v in pLink.items()}
