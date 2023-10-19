# import <
from dash import html
import dash_bootstrap_components as dbc

from frontend.layout.badge import badgeIcon
from frontend.layout.card import cardFunction

# >


def frameHeader(pData: dict):
    '''  '''

    return cardFunction(

        pData = pData,
        pJoin = 'default',
        pJustify = 'center',
        pComponent = dbc.Row(),
        pBorder = pData['templateStyle']['gBorderBlack'],
        pBackdropFilter = pData['templateStyle']['gBackdropFilter'],
        pBackgroundColor = pData['templateStyle']['gColorBlackTransparent'],
        pChildren = [

            html.Img(

                src = pData['frameData']['headerImgSrc'],
                style = pData['frameStyle']['headerImgStyle']

            )

        ]

    )


def frameMenu(

        pData: dict,
        pSelected: str

):
    '''  '''

    return cardFunction(

        pData = pData,
        pJoin = 'default',
        pJustify = 'evenly',
        pComponent = dbc.Row(),
        pBorder = pData['templateStyle']['gBorderBlack'],
        pBackdropFilter = pData['templateStyle']['gBackdropFilter'],
        pBackgroundColor = pData['templateStyle']['gColorBlackTransparent'],
        pChildren = [

            dbc.Col(

                width = 'auto',
                children = dbc.Button(

                    id = k,
                    href = k,
                    children = [

                        # pointer <
                        # tab <
                        html.Img(

                            src = pData['frameData']['pointerImgSrc'],
                            style = pData['frameStyle']['pointerImgStyle']

                        ) if (k == pSelected) else None,
                        html.Img(

                            src = v,
                            style = pData['frameStyle']['menuImgStyle']

                        )

                        # >

                    ]

                )

            )

        for k, v in pData['frameData']['menuChildren'].items()]

    )


def frameFooter(pData: dict):
    '''  '''

    return cardFunction(

        pData = pData,
        pJoin = 'default',
        pJustify = 'evenly',
        pComponent = dbc.Row(),
        pBorder = pData['templateStyle']['gBorderBlack'],
        pBackdropFilter = pData['templateStyle']['gBackdropFilter'],
        pBackgroundColor = pData['templateStyle']['gColorBlackTransparent'],
        pChildren = [

            badgeIcon(

                pHref = k,
                pSrc = [v],
                pHeight = 35,
                pData = pData,
                pWidth = 'auto',
                isExternal = True,
                pStyle = pData['frameStyle']['footerBadgeStyle']

            )[0]

        for k, v in pData['frameData']['footerChildren'].items()]

    )


def frameFunction(pData: dict):
    '''  '''

    return dbc.Container(

        fluid = True,
        id = 'frameContainerId',
        style = dict(

            **pData['frameStyle']['frameContainerStyle'],
            backgroundImage = 'url({})'.format(pData['frameData']['frameContainerBackgroundImage'])

        ),
        children = [

            # header <
            # menu <
            # content <
            # footer <
            frameHeader(pData = pData),
            html.Div(id = 'menuDivId'),
            html.Div(id = 'contentDivId'),
            frameFooter(pData = pData)

            # >

        ]

    )
