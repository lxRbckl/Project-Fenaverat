# import <
from dash import html
import dash_bootstrap_components as dbc

from frontend.layout.badge import badgeFunction, badgeIcon

# >


def cardFunction(

        pData: dict,
        pComponent: str,
        pTitle: str = None,
        pWidth: int = None,
        pAlign: str = None,
        pJoin: str = 'none',
        pBorder: str = None,
        pMargin: int = None,
        pJustify: str = None,
        pPadding: int = None,
        pChildren: list = [],
        pBadgeIcon: list = [],
        pBadgeHeight: int = None,
        pBadgeStyle: dict = None,
        pDescription: str = None,
        borderBottom: bool = False,
        pBackdropFilter: str = None,
        pBackgroundColor: str = False

):
    '''  '''

    pComponent.width = pWidth
    pComponent.align = pAlign
    pComponent.justify = pJustify
    pComponent.children = [

        # (title, if (icon)) <
        # if (description) <
        # children <
        dbc.Row(

            children = [

                # title <
                # icon <
                dbc.Col(

                    width = {'order' : 1, 'size' : 'auto'},
                    children = html.H2(

                        children = html.Small(pTitle),
                        style = dict(

                            **pData['cardStyle']['cardH2Style'],
                            color = pData['templateStyle']['gColorWhite'],
                            fontFamily = pData['templateStyle']['gFontFamily']

                        )

                    )

                ),
                *badgeIcon(

                    pData = pData,
                    pSrc = pBadgeIcon,
                    pHeight = pBadgeHeight,
                    pWidth = {'order' : 2, 'size' : 'auto'},
                    pStyle = pBadgeStyle if (pBadgeStyle) else pData['cardStyle']['cardBadgeStyle']

                )

                # >

            ]

        ) if (pTitle) else None,
        html.Small(

            children = pDescription,
            style = dict(

                **pData['cardStyle']['cardSmallStyle'],
                color = pData['templateStyle']['gColorWhite'],
                fontFamily = pData['templateStyle']['gFontFamily']

            )

        ) if (pDescription) else None,
        *pChildren

        # >

    ]
    pComponent.style = dict(

        backdropFilter = pBackdropFilter,
        padding = pPadding if (pPadding) else pData['templateStyle']['gPadding'],
        backgroundColor = pData['templateStyle']['gColorBlack'] if (pBackgroundColor == True) else pBackgroundColor,
        **{

            False : {

                'borderTop' : pBorder,
                'borderLeft' : pBorder,
                'borderRight' : pBorder,
                'marginTop' : 0 if (pJoin in ['none']) else pData['templateStyle']['gMargin'],
                'borderBottom' : pBorder if (borderBottom or (pJoin in ['default'])) else None,
                'marginBottom' : 0 if (pJoin in ['none']) else pData['templateStyle']['gMargin'],
                'marginLeft' : pMargin if (pJoin in ['none']) else pData['templateStyle']['gMargin'],
                'marginRight' : pMargin if (pJoin in ['none']) else pData['templateStyle']['gMargin'],
                'borderRadius' : 0 if (pJoin in ['none']) else pData['templateStyle']['gBorderRadius']

            },
            True : {

                **{'borderBottom' if (borderBottom ) else '' : pBorder},
                **{k : v for k, v in {

                    'borderTop': pBorder,
                    'borderLeft': pBorder,
                    'borderRight': pBorder,
                    'borderBottom': pBorder,
                    'marginLeft': pMargin if (pMargin) else 0,
                    'marginRight': pMargin if (pMargin) else 0,
                    'borderTopLeftRadius': pData['templateStyle']['gBorderRadius'],
                    'borderTopRightRadius': pData['templateStyle']['gBorderRadius'],
                    'borderBottomLeftRadius': pData['templateStyle']['gBorderRadius'],
                    'borderBottomRightRadius': pData['templateStyle']['gBorderRadius'],
                    'marginTop': pMargin if (pMargin) else pData['templateStyle']['gMargin'],
                    'marginBottom': pMargin if (pMargin) else pData['templateStyle']['gMargin']

                }.items() if (pJoin.title() not in k)},

            }

        }[False if (pJoin in ['none', 'default']) else True],

    )

    return pComponent


def cardProject(

        pData: dict,
        pValue: str,
        pKey: str = 'myProjectData'

):
    '''  '''

    return html.Div(

        children = [

            # header <
            # body <
            # footer <
            cardFunction(

                pData = pData,
                pJoin = 'bottom',
                pComponent = dbc.Col(),
                pPadding = '5px 5px 4px 5px',
                pTitle = pValue.replace('-', ' '),
                pBorder = pData['templateStyle']['gBorderWhite'],
                pDescription = pData[pKey][pValue]['description'],
                pBackgroundColor = pData['templateStyle']['gColorBlack'],

            ),
            cardFunction(

                pData = pData,
                borderBottom = True,
                pComponent = dbc.Col(),
                pPadding = '3px 3px 3px 3px',
                pBorder = pData['templateStyle']['gBorderWhite'],
                pBackgroundColor = pData['templateStyle']['gColorBlackTransparent'],
                pChildren = [

                    badgeFunction(

                        pData = pData,
                        pWidth = 'auto',
                        pIterable = pData[pKey][pValue],
                        pSubject = ['language', 'library', 'feedSubject'],
                        pBorder = pData['templateStyle']['gBorderWhite']

                    )

                ]

            ),
            cardFunction(

                pJoin = 'top',
                pData = pData,
                pComponent = dbc.Col(),
                pPadding = '5px 22px 1px 5px',
                pBorder = pData['templateStyle']['gBorderWhite'],
                pBackgroundColor = pData['templateStyle']['gColorBlack'],
                pChildren = [

                    dbc.Row(

                        children = [

                            # github <
                            # update <
                            # if (feed) <
                            badgeIcon(

                                pData = pData,
                                isExternal = True,
                                pWidth = {'order' : 1, 'size' : 'auto'},
                                pSrc = [pData['badgeData']['githubIcon']],
                                pHref = pData['myProjectData'][pValue]['projectLink']

                            )[0],
                            badgeIcon(

                                pData = pData,
                                pWidth = {'order' : 1, 'size' : 'auto'},
                                pSrc = [pData['badgeData']['updateIcon']]

                            )[0],
                            dbc.Col(

                                width = {'order' : 1},
                                children = html.Small(

                                    children = pData[pKey][pValue]['update'],
                                    style = dict(

                                        color = pData['templateStyle']['gColorWhite'],
                                        fontFamily = pData['templateStyle']['gFontFamily']

                                    )

                                )

                            ),
                            badgeIcon(

                                pData = pData,
                                pSrc = [pData['badgeData']['viewIcon']],
                                pWidth = {'order' : 5, 'size' : 'auto'},
                                pHref = '/{}'.format(pValue.replace(' ', '-'))

                            )[0] if (len(pData['myProjectData'][pValue]['feedSubject']) != 0) else None

                            # >

                        ]

                    )

                ]

            )

            # >

        ]

    )


def cardServer(

        pData: dict,
        pValue: str,
        pKey: str = 'myServerData'

):
    '''  '''

    try:

        return html.Div(

            children = [

                # header <
                # if (body) <
                cardFunction(

                    pData = pData,
                    pBadgeHeight = 17,
                    pComponent = dbc.Row(),
                    pPadding = '5px 5px 5px 4px',
                    pBorder = pData['templateStyle']['gBorderWhite'],
                    pBackgroundColor = pData['templateStyle']['gColorBlack'],
                    pJoin = 'bottom' if (len(pData[pKey][pValue]['service']) > 0) else 'server',
                    borderBottom = True if (len(pData[pKey][pValue]['service']) > 0) else False,
                    pTitle = html.H4(pValue, style = dict(padding = 0, margin = '5px 0px 0px -11px')),
                    pBadgeIcon = [pData[pKey][pValue][i] for i in pData[pKey][pValue].keys() if ('Icon' in i)],
                    pDescription = '{} - {}'.format(

                        pData[pKey][pValue]['description'].replace('-', ' '),
                        pData[pKey][pValue]['type'].replace('-', ' ')

                    )

                ),
                cardFunction(

                    pJoin = 'top',
                    pData = pData,
                    pComponent = dbc.Row(),
                    pPadding = '3px 7px 3px 3px',
                    pBorder = pData['templateStyle']['gBorderWhite'],
                    pBackdropFilter = pData['templateStyle']['gBackdropFilter'],
                    pBackgroundColor = pData['templateStyle']['gColorBlackTransparent'],
                    pChildren = [

                        badgeFunction(

                            pData = pData,
                            pSubject = ['service'],
                            pIterable = pData[pKey][pValue]

                        )

                    ]

                ) if (len(pData[pKey][pValue]['service']) > 0) else None

                # >

            ]

        )

    except (KeyError, AttributeError): return None
