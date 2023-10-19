# import <
from dash import html
from os import listdir
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output
from backend.utility import application, jsonLoad, directory

# >


# global <
aboutMeData = jsonLoad(file = '/frontend/data/aboutMe.json')
myProjectData = jsonLoad(file = '/frontend/data/myProject.json')
myProjectStyle = jsonLoad(file = '/frontend/resource/myProject.json')

# >


# layout <
myProjectLayout = (

    # board <
    dbc.Row(

        justify = 'center',
        id = 'myProjectBoardRowId'

    ),

    # >

)

# >


# callback <
@application.callback(Output('myProjectBoardRowId', 'children'),
                      Input('myProjectBoardRowId', 'children'))
def myProjectCallback(*args):
    '''  '''

    # local <
    path = directory + '/frontend/data/feed'
    myProjectData = jsonLoad(file = '/frontend/data/myProject.json')
    feed = {t : jsonLoad(f'/frontend/data/feed/{t}') for t in listdir(path)}

    # >

    # build data <
    # filter data <
    project = {t : f for u in myProjectData.keys() for t, f in myProjectData[u]['project'].items()}
    project = {t : f for t, f in project.items() if (f['hide'] is False)}

    # >

    # build queue from data <
    # filter queue <
    queue = [title for user in myProjectData for title in myProjectData[user]['queue'][::-1]]
    queue = [title for title in queue if (title in project.keys())][::-1]

    # >

    # build board from queue <
    board = ([], [], [])
    [board[c % len(board)].append(title) for c, title in enumerate(queue)]

    # >

    # output <
    return (

        [

            dbc.Col(

                children = [

                    myProjectFunction(title = title, projectData = project, feedData = feed)

                for title in col]

            )

        for col in board]

    )

    # >

# >


# function <
def myProjectFunction(title: str, projectData: dict, feedData: dict):
    '''  '''

    # output <
    return (

        # card <
        dbc.Card(

            style = myProjectStyle['cardStyle'],
            children = [

                # header <
                dbc.CardHeader(

                    style = myProjectStyle['cardChildrenStyle'],
                    children = cardHeaderFunction(title, projectData, feedData)

                ),

                # >

                # body <
                dbc.CardBody(

                    style = myProjectStyle['bodyCardBodyStyle'],
                    children = cardBodyFunction(title, projectData, feedData)

                ),

                # >

                # footer <
                dbc.CardFooter(

                    style = myProjectStyle['cardChildrenStyle'],
                    children = cardFooterFunction(title, projectData, feedData)

                )

                # >

            ]

        )

        # >

    )

    # >


def cardHeaderFunction(title: str, projectData: dict, feedData: dict):
    '''  '''

    # output <
    return (

        # title <
        # description <
        # spacer <
        html.H4(title.replace('-', ' ')),
        html.Small(html.Small(projectData[title]['description'])),
        html.Hr(style = myProjectStyle['headerSpacerHrStyle'])

        # >

    )

    # >


def cardBodyFunction(title: str, projectData: dict, feedData: dict):
    '''  '''

    # output <
    return [

        dbc.Badge(

            children = subject.title(),
            color = myProjectStyle['bodyBadgeColor'],
            style = myProjectStyle['bodyBadgeStyle']

        )

    for subject in feedData[f'{title}.json'].keys()
    if (subject not in myProjectStyle['subjectFilter'])]

    # >


def cardFooterFunction(title: str, projectData: dict, feedData: dict):
    '''  '''

    # if (no feed) <
    if (not feedData[f'{title}.json'].keys()):

        spacer = None
        feed = None

    # >

    # else (feed) <
    else:

        spacer = html.Hr(style = myProjectStyle['footerSpacerHrStyle'])
        feed = dbc.CardLink(

            href = f'/{title}',
            style = myProjectStyle['footerCardLinkStyle'],
            children = '{} ⇾'.format(title.replace('-', ' '))

        )

    # >

    # output <
    return (

        spacer,

        dbc.Row(

            justify = 'between',
            children = [

                # feed <
                dbc.Col(

                    width = 'auto',
                    children = feed

                ),

                # >

                # link <
                dbc.Col(

                    width = 'auto',
                    children = [

                        html.A(

                            href = projectData[title]['link'],
                            children = [

                                html.Img(

                                    src = myProjectStyle['linkImgSrc'],
                                    style = myProjectStyle['linkImgStyle']

                                )

                            ]

                        )

                    ]

                )

                # >

            ]

        ),

    )

    # >

# >
