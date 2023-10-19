# import <
from dash import html, dcc
from dash.dependencies import Input, Output

from frontend.layout.board import boardFunction
from frontend.layout.frame import frameFunction, frameMenu
from frontend.layout.feed import aboutMeFeed, myProjectFeed
from backend.resource import application, gRefreshRate, getFunction

# >


# global <
gData = getFunction()

#>


def templateFunction():
    '''  '''

    return html.Div(

        id = 'templateContainerId',
        children = [

            # location <
            # interval <
            dcc.Location(id = 'containerLocationId'),
            dcc.Interval(

                n_intervals = 0,
                id = 'containerIntervalId',
                interval = (60000 * gRefreshRate)

            ),

            # >

            frameFunction(pData = gData)

        ]

    )


@application.callback(

    Output('menuDivId', 'children'),
    Output('contentDivId', 'children'),
    Input('containerLocationId', 'pathname')

)
def locationCallback(pPathname: str):
    '''  '''

    return [

        frameMenu(

            pData = gData,
            pSelected = {

                '' : 'aboutMe',
                'aboutMe' : 'aboutMe',
                'myServer' : 'myServer',
                'myProject' : 'myProject',
                **{p : 'myProject' for p in gData['myProjectData'].keys()}

            }[pPathname[1:]]

        ),
        {

            '' : aboutMeFeed,
            'aboutMe' : aboutMeFeed,
            'myServer' : boardFunction,
            'myProject' : boardFunction,
            **{p : myProjectFeed for p in gData['myProjectData'].keys()}

        }[pPathname[1:]](

            pData = gData,
            pPathname = pPathname.replace('/', '')

        )

    ]


@application.callback(

    Output('containerIntervalId', 'disabled'),
    Input('containerIntervalId', 'n_intervals')

)
def intervalCallback(pInterval: int):
    '''  '''

    # get data <
    # update data <
    global gData
    gData = getFunction()

    # >

    return False
