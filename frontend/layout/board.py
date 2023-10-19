# import <
from dash import html
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output, State

from frontend.layout.search import searchFunction
from backend.resource import gFilter, application, getFunction
from frontend.layout.card import cardFunction, cardServer, cardProject

# >


def boardBuild(

        pData: dict,
        pBoard: list,
        pPathname: str,

):
    '''  '''

    return cardFunction(

        pData = pData,
        pJoin = 'default',
        pComponent = dbc.Row(),
        pPadding = '0px 2px 0px 3px',
        pBorder = pData['templateStyle']['gBorderBlack'],
        pBackdropFilter = pData['templateStyle']['gBackdropFilter'],
        pBackgroundColor = pData['templateStyle']['gColorBlackTransparent'],
        pChildren = [

            cardFunction(

                pData = pData,
                pComponent = dbc.Col(),
                pPadding = '0px 3px 0px 2px',
                pChildren = [

                    {

                        'myServer' : cardServer,
                        'myProject' : cardProject

                    }[pPathname](

                        pValue = row,
                        pData = pData

                    )

                for row in col]

            )

        for col in pBoard]

    )


def boardFilter(

    pData: dict,
    pPathname: str,
    pName: str = None,
    pLibrary: str = None,
    pLanguage: str = None

):
    '''  '''

    # set (rBoard, b) <
    # iterate (project) <
    rBoard, b = [[], [], []], True
    for c, i in enumerate([i for i in pData[f'{pPathname}Data'] if (i not in gFilter)]):

        b = True

        # if (match) <
        # then (add project) <
        if (pName): b = True if (pName == i) else False
        if (pLibrary and b): b = True if (pLibrary in pData['myProjectData'][i]['library']) else False
        if (pLanguage and b): b = True if (pLanguage in pData['myProjectData'][i]['language']) else False

        if (b): rBoard[c % len(rBoard)].append(i)

        # >

    # >

    return sorted(rBoard, reverse = True)


def boardFunction(

        pData: dict,
        pPathname: str

):
    '''  '''

    return html.Div(

        children = [

            # if (search) <
            # output <
            searchFunction(pData = pData) if (pPathname == 'myProject') else None,
            html.Div(

                id = 'boardDivId',
                children = searchCallback(

                    pData = pData,
                    pPathname = pPathname

                )

            )

            # >

        ]

    )


@application.callback(

    Output('boardDivId', 'children'),
    Input('nameDropdownId', 'value'),
    Input('libraryDropdownId', 'value'),
    Input('languageDropdownId', 'value'),
    State('containerLocationId', 'pathname'),

    prevent_initial_call=True

)
def searchCallback(

        pName: str = None,
        pLibrary: str = None,
        pLanguage: str = None,
        pPathname: str = None,
        pData: dict = getFunction()

):
    '''  '''

    return [

        boardBuild(

            pData = pData,
            pPathname = pPathname.replace('/', ''),
            pBoard = boardFilter(

                pData = pData,
                pName = pName,
                pLibrary = pLibrary,
                pLanguage = pLanguage,
                pPathname = pPathname.replace('/', '')

            )

        )
    ]
