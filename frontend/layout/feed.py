# import <
from dash import html, dcc
from backend.utility import jsonLoad
import dash_bootstrap_components as dbc

# >


# global <
feedStyle = jsonLoad(file = '/frontend/resource/feed.json')
myProjectStyle = jsonLoad(file = '/frontend/resource/myProject.json')

# >


# function <
def feedFunction(data: dict):
    '''  '''

    # local <
    feed = [linkFunction()]

    # >

    # build feed <
    for subject, article in data.items():

        # if (header or image) <
        # else (anything) <
        if (subject in myProjectStyle['subjectFilter']): feed.append(imageFunction(article))
        else: feed.append(markdownFunction(subject, article))

        # >

    # >

    # output <
    return (

        dbc.Card(

            style = feedStyle['cardStyle'],
            children = [post for post in feed]

        )

    )

    # >


def linkFunction():
    '''  '''

    # output <
    return (

        # back <
        dbc.CardBody(

            style = feedStyle['backCardBodyStyle'],
            children = [

                dbc.CardLink(

                    href = '/myProject',
                    children = '⇽ Go Back',
                    style = feedStyle['backCardLinkStyle']

                )

            ]

        )

        # >

    )

    # >


def imageFunction(article: str):
    '''  '''

    # output <
    return (

        dbc.CardImg(

            src = article,
            style = feedStyle['cardImgStyle']

        )

    )

    # >


def markdownFunction(subject: str, article: list):
    '''  '''

    # output <
    return (

        dbc.CardBody(

            style = feedStyle['cardBodyStyle'],
            children = [

                # subject <
                # article <
                html.H3(subject),
                html.Small(dcc.Markdown([i for i in article]))

                # >

            ]

        )

    )

    # >

# >
