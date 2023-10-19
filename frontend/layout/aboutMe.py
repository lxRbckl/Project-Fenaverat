# import <
from dash import html, dcc
import plotly.graph_objects as go
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output
from backend.utility import application, jsonLoad

# >


# global <
aboutMeData = jsonLoad(file = '/frontend/data/aboutMe.json')
aboutMeStyle = jsonLoad(file = '/frontend/resource/aboutMe.json')

# >


# layout <
aboutMeLayout = (

    dbc.Row(

        children = [

            # image <
            dbc.Col(

                width = 'auto',
                id = 'iamgeColId',
                children = [

                    dbc.Card(

                        style = aboutMeStyle['imageCardStyle'],
                        children = [

                            dbc.CardImg(

                                src = aboutMeData['imageCardImgSrc'],
                                style = aboutMeStyle['imageCardImgStyle']

                            )

                        ]

                    ),

                ]

            ),

            # >

            # biography <
            dbc.Col(

                id = 'biographyColId',
                children = [

                    dbc.Card(

                        style = aboutMeStyle['biographyCardStyle'],
                        children = [

                            dbc.CardBody(

                                children = [

                                    # title <
                                    # spacer <
                                    # article <
                                    html.H4(aboutMeData['biographyTitle']),
                                    html.Hr(style = aboutMeStyle['spacerHrStyle']),
                                    html.H6(dcc.Markdown([i for i in aboutMeData['biographyArticle']]))

                                    # >

                                ]

                            )

                        ]

                    )

                ]

            )

            # >

        ]

    ),

    dbc.Row(

        # graph <
        children = [

            # language <
            dbc.Col(

                id = 'languageColId',
                style = aboutMeStyle['graphColStyle'],
                children = [

                    dbc.Card(

                        style = aboutMeStyle['graphCardStyle'],
                        children = [

                            # header <
                            # body <
                            dbc.CardBody(

                                style = aboutMeStyle['graphHeaderStyle'],
                                children = [

                                    # title <
                                    # spacer <
                                    html.H6(

                                        children = 'Language',
                                        style = aboutMeStyle['titleH6Style']

                                    ),
                                    html.Hr(style = aboutMeStyle['spacerHrStyle']),

                                    # >

                                    # graph <
                                    dcc.Graph(id = 'languageGraphId'),

                                    # >

                                ]

                            ),

                            # >

                        ]

                    )

                ],

            # >

            ),

            # >

            # topic <
            dbc.Col(

                id = 'topicColId',
                style = aboutMeStyle['graphColStyle'],
                children = [

                    dbc.Card(

                        style = aboutMeStyle['graphCardStyle'],
                        children = [

                            dbc.CardBody(

                                style = aboutMeStyle['graphHeaderStyle'],
                                children = [

                                    # title <
                                    # spacer <
                                    html.H6(

                                        children = 'Topic',
                                        style = aboutMeStyle['titleH6Style']

                                    ),
                                    html.Hr(style = aboutMeStyle['spacerHrStyle']),

                                    # >

                                    # graph <
                                    dcc.Graph(id = 'topicGraphId'),

                                    # >

                                ]

                            )

                        ]

                    )

                ]

            ),

            # >

        ]

        # >

    )

)

# >


# callback <
@application.callback(Output('topicGraphId', 'figure'),
                      Output('languageGraphId', 'figure'),
                      Input('languageColId', 'children'))
def aboutMeCallback(*args):
    '''  '''

    # global <
    global aboutMeData
    aboutMeData = jsonLoad(file = '/frontend/data/aboutMe.json')

    # >

    # get topic and language <
    # iterate (user) <
    topicList = aboutMeData['bonusTopic']
    languageList = aboutMeData['bonusLanguage']
    for user in aboutMeData['users']:

        topicList.extend(aboutMeData[user]['topic'])
        languageList.extend(aboutMeData[user]['language'])

    # >

    # get topic and language figure <
    topicGraph = aboutMeFunction(topicList)
    languageGraph = aboutMeFunction(languageList)

    # >

    # output <
    return (topicGraph, languageGraph)

    # >

# >


# function <
def aboutMeFunction(data: list):
    '''  '''

    # iterate (arg) <
    dictVariable = {}
    for i in data:

        # if (element in dict then increment) <
        # else (element not in dict then initialize) <
        if (i in dictVariable.keys()): dictVariable[i] += 1
        else: dictVariable[i] = 1

        # >

    # >

    # figure <
    figure = {

        'data' : [

            go.Pie(

                hole = 0.4,
                textinfo = 'label',
                hoverinfo = 'none',
                showlegend = False,
                textposition = 'inside',
                insidetextorientation = 'radial',
                labels = list(dictVariable.keys()),
                values = list(dictVariable.values()),
                marker = {

                    'colors' : [aboutMeStyle['figureColors'] for i in dictVariable.keys()],
                    'line' : aboutMeStyle['figureLine']

                }

            )

        ],

        'layout' : aboutMeStyle['figureLayout']

    }

    # >

    # output <
    return figure

    # >

# >
