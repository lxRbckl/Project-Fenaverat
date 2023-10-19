# import <
from dash import html, dcc
import dash_bootstrap_components as dbc

from backend.resource import getFunction
from frontend.layout.card import cardFunction

# >


def loadText(

        pData: dict,
        pValue: str,
        pColor: str,
        **kwargs

):
    '''  '''

    return dbc.Col(

        style = pData['loadStyle']['textColStyle'],
        children = [

            html.Small(

                children = [v, html.Div(style = pData['loadStyle']['textDivStyle'])],
                style = dict(

                    **pData['loadStyle']['textSmallStyle'],
                    fontFamily = pData['templateStyle']['gFontFamily'],
                    color = pColor if (pColor) else pData['templateStyle']['gColorWhite']

                )

            )

        for v in pValue]

    )


def loadTitle(

        pColor: str,
        pData: dict,
        pValue: list,

):
    '''  '''

    return dbc.Col(

        style = pData['loadStyle']['titleColStyle'],
        children = html.H1(

            id = pValue,
            children = pValue.title(),
            style = dict(

                color = pColor,
                fontFamily = pData['templateStyle']['gFontFamily']

            )

        )

    )


def loadMarkdown(

        pData: dict,
        pValue: str,
        pColor: str,
        pBorder: str,
        **kwargs

):
    ''' '''

    return dbc.Col(

        style = dict(paddingBottom = 5),
        children = dbc.Col(

            style = dict(

                border = pBorder,
                **pData['loadStyle']['markdownColStyle'],
                borderRadius = pData['templateStyle']['gBorderRadius']

            ),
            children = dcc.Markdown(

                children = getFunction(

                    isJSON = False,
                    pLink = {'md' : pValue}

                )['md'],
                style = dict(

                    color = pColor,
                    **pData['loadStyle']['markdownStyle'],
                    fontFamily = pData['templateStyle']['gFontFamily']

                )

            )

        )

    )


def loadSpace(

        pData: dict,
        **kwargs

):
    '''  '''

    return html.Div(style = pData['loadStyle']['spaceDivStyle'])


def loadImage(

        pData: dict,
        pValue: str,
        **kwargs

):
    '''  '''

    return dbc.Col(

        style = pData['loadStyle']['imageColStyle'],
        children = html.Img(

            src = pValue,
            style = dict(

                **pData['loadStyle']['imageImgStyle'],
                borderRadius = pData['templateStyle']['gBorderRadius']

            )

        )

    )


def loadSubtitle(

        pData: dict,
        pValue: str,
        pColor: str,
        **kwargs

):
    '''  '''

    return dbc.Col(

        style = pData['loadStyle']['subtitleColStyle'],
        children = html.H2(

            children = pValue,
            style = dict(

                **pData['loadStyle']['subtitleH2Style'],
                fontFamily = pData['templateStyle']['gFontFamily'],
                color = pColor if (pColor) else pData['templateStyle']['gColorWhite']

            )

        )

    )


def loadFunction(

        pFeed: dict,
        pData: dict,
        pBorder: str,
        pLength: list

):
    '''  '''

    return [

        cardFunction(

            pMargin = 5,
            pData = pData,
            pBorder = pBorder,
            pComponent = dbc.Col(),
            pPadding = '5px 0px 0px 0px',
            borderBottom = (c == (pLength - 1)),
            pBackgroundColor = pFeed['content'][k]['background'],
            pJoin = {1 : 'bottom', pLength : 'top'}[c] if (pLength > 1) else 'default',
            pChildren = [

                # title <
                # iterate (content) <
                loadTitle(

                    pValue = k,
                    pData = pData,
                    pColor = v['title'] if (v['title']) else pData['templateStyle']['gColorWhite']

                ) if k not in ['About Me'] else None,
                *[

                    {

                        'text' : loadText,
                        'space' : loadSpace,
                        'image' : loadImage,
                        'markdown' : loadMarkdown,
                        'subtitle' : loadSubtitle

                    }[vType](

                        pData = pData,
                        pColor = vColor,
                        pValue = vContent,
                        pBorder = pBorder,
                        isBorder = vColor

                    )

                for vType, vColor, vContent in v['subject']]

                # >

            ]

        )

    for c, (k, v) in enumerate(pFeed['content'].items(), start = 1)]
