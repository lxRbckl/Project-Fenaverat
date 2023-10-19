# import <
from dash import html
import dash_daq as daq
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output
from backend.utility import application, jsonLoad

# >


# global <
myServerData = jsonLoad(file = '/frontend/data/myServer.json')
myServerStyle = jsonLoad(file = '/frontend/resource/myServer.json')

# >


# layout <
myServerLayout = (

    # board <
    dbc.Row(

        justify = 'center',
        id = 'myServerBoardRowId'

    )

    # >

)

# >


# callback <
@application.callback(Output('myServerBoardRowId', 'children'),
                      Input('myServerBoardRowId', 'children'))
def myServerCallabck(*args):
    '''  '''

    # build server <
    # filter server <
    server = jsonLoad(file = '/frontend/data/myServer.json')
    server = {k : v for k, v in server.items() if (v['hide'] is False)}

    # >

    # build board from server <
    board = ([], [], [])
    [board[c % len(board)].append(node) for c, node in enumerate(server)]

    # >

    # output <
    return (

        [

            dbc.Col(

                children = [

                    myServerFunction(node = node, serverData = server)

                for node in col]

            )

        for col in board]

    )

    # >

# >


# function <
def myServerFunction(node: str, serverData: dict):
    '''  '''

    # output <
    return (

        # card <
        dbc.Card(

            style = myServerStyle['cardStyle'],
            children = [

                # header <
                dbc.CardHeader(

                    style = myServerStyle['cardChildrenStyle'],
                    children = cardHeaderFunction(node, serverData)

                ),

                # >

                # body <
                dbc.CardBody(

                    style = myServerStyle['cardChildrenStyle'],
                    children = cardBodyFunction(node, serverData)

                )

                # >

            ]

        )

        # >

    )

    # >


def cardHeaderFunction(node: str, serverData: dict):
    '''  '''

    # if (online) <
    # else (offline) <
    if (serverData[node]['status'] == 'On'): status = myServerStyle['online']
    else: status = myServerStyle['offline']

    # >

    # output <
    return (

        # title <
        # description <
        html.H4(

            children = node,
            style = myServerStyle['titleH4Style']

        ),
        html.Small(serverData[node]['description']),

        # >

        # status <
        # spacer <
        daq.Indicator(

            style = myServerStyle['statusIndicatorStyle'],
            color = status,
            size = 7

        ),
        html.Hr(style = myServerStyle['spacerHrStyle'])

        # >

    )

    # >


def cardBodyFunction(node: str, serverData: dict):
    '''  '''

    # output <
    return (

        dbc.ListGroup(

            style = myServerStyle['taskListGroupStyle'],
            children = [

                # task <
                dbc.ListGroupItem(

                    children = html.Small(task),
                    style = myServerStyle['taskListGroupItemStyle']

                )

                # >

            for task in serverData[node]['running']]

        )

        # >

    )

    # >

# >
