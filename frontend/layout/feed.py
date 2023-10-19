
# import <
from dash import html
import dash_bootstrap_components as dbc

from backend.resource import getFunction
from frontend.layout.card import cardFunction
from frontend.layout.load import loadFunction
from frontend.layout.badge import badgeFunction, badgeIcon

# >


def aboutMeFeed(

        pData: dict,
        pPathname: str,
        pBorder: str = '1px solid '

):
    '''  '''

    # local <
    feed = pData['aboutMeFeed']['feed']

    # >

    return cardFunction(

        pData = pData,
        pJoin = 'default',
        pComponent = dbc.Row(),
        pPadding = '0px 0px 0px 0px',
        pChildren = [

            # left <
            # right <
            cardFunction(

                pWidth = 3,
                pData = pData,
                pJoin = 'right',
                pComponent = dbc.Col(),
                pMargin = '0px 0px 0px 0px',
                pPadding = '5px 5px 0px 4px',
                pBorder = pData['templateStyle']['gBorderBlack'],
                pBackgroundColor = pData['templateStyle']['gColorBlack'],
                pBackdropFilter = pData['templateStyle']['gBackdropFilter'],
                pChildren = [

                    html.Div(

                        style = pData['feedStyle']['feedDivStyle'],
                        children = [

                            # photo <
                            # biography <
                            cardFunction(

                                pData = pData,
                                pJoin = 'bottom',
                                pComponent = dbc.Col(),
                                pPadding = '0px 0px 0px 0px',
                                pBorder = pData['templateStyle']['gBorderWhite'],
                                pChildren = [

                                    html.Img(

                                        src = pData['aboutMeData']['photo'],
                                        style = dict(

                                            **pData['feedStyle']['aboutImgStyle'],
                                            borderTopLeftRadius = pData['templateStyle']['gBorderRadius'],
                                            borderTopRightRadius = pData['templateStyle']['gBorderRadius']

                                        )

                                    )

                                ]

                            ),
                            *[

                                cardFunction(

                                    pData = pData,
                                    pBadgeHeight = 17,
                                    pComponent = dbc.Col(),
                                    pBadgeIcon = [v['icon']],
                                    pPadding = '8px 4px 2px 4px',
                                    pJoin = 'top' if (k in ['library']) else 'none',
                                    pBorder = pData['templateStyle']['gBorderWhite'],
                                    pBadgeStyle = pData['feedStyle']['aboutBadgeStyle'],
                                    pBackgroundColor = pData['templateStyle']['gColorBlack'],
                                    borderBottom = (k == list(pData['aboutMeData']['biography'].keys())[-2]),
                                    pTitle = [

                                        html.H4(

                                            children = v['title'],
                                            style = pData['feedStyle']['aboutH4TitleStyle']

                                        )

                                    ],
                                    pDescription = [

                                        html.H4(

                                            children = v['description'],
                                            style = pData['feedStyle']['aboutH4DescriptionStyle']

                                        )

                                    ],
                                    pChildren = [

                                        badgeFunction(

                                            pData = pData,
                                            pSubject = [k],
                                            pWidth = 'auto',
                                            pIterable = pData['myProjectData'],
                                            pBorder = pData['templateStyle']['gBorderWhite']

                                        ) if (k in ['language', 'library']) else None

                                    ]

                                )

                            for k, v in pData['aboutMeData']['biography'].items()]

                            # >

                        ]

                    )

                ]

            ),
            cardFunction(

                pWidth = 9,
                pData = pData,
                pJoin = 'left',
                pComponent = dbc.Col(),
                pMargin = '0px 0px 0px 0px',
                pPadding = '0px 0px 0px 0px',
                pBorder = pData['templateStyle']['gBorderBlack'],
                pBackdropFilter = pData['templateStyle']['gBackdropFilter'],
                pBackgroundColor = pData['templateStyle']['gColorBlackTransparent'],
                pChildren = [

                    *loadFunction(

                        pFeed = feed,
                        pData = pData,
                        pBorder = pBorder,
                        pLength = len(feed['content'].keys())

                    )

                ]

            )

            # >

        ]

    )


def myProjectFeed(

        pData: dict,
        pPathname: str,
        pBorder = '1px solid '

):
    '''  '''

    # local <
    feed = getFunction(pLink = {'feedData' : pData['myProjectData'][pPathname]['feedLink']})['feedData']['feed']
    pBorder += feed['border'] if (feed['border']) else pData['templateStyle']['gColorWhite']

    # >

    return cardFunction(

        pData = pData,
        pJoin = 'default',
        pComponent = dbc.Row(),
        pPadding = '0px 0px 0px 0px',
        pChildren = [

            # feed <
            # panel <
            cardFunction(

                pWidth = 8,
                pData = pData,
                pJoin = 'right',
                pComponent = dbc.Col(),
                pMargin = '0px 0px 0px 0px',
                pPadding = '0px 0px 0px 0px',
                pBorder = pData['templateStyle']['gBorderBlack'],
                pBackdropFilter = pData['templateStyle']['gBackdropFilter'],
                pBackgroundColor = pData['templateStyle']['gColorBlackTransparent'],
                pChildren = [

                    *loadFunction(

                        pFeed = feed,
                        pData = pData,
                        pBorder = pBorder,
                        pLength = feed['content'].keys()

                    )

                ]

            ),
            cardFunction(

                pWidth = 4,
                pData = pData,
                pJoin = 'left',
                pComponent = dbc.Col(),
                pMargin = '0px 0px 0px 0px',
                pPadding = '5px 5px 0px 5px',
                pBorder = pData['templateStyle']['gBorderBlack'],
                pBackgroundColor = pData['templateStyle']['gColorBlack'],
                pChildren = [

                    html.Div(

                        style = pData['feedStyle']['feedDivStyle'],
                        children = [

                            # photo <
                            # about <
                            # stack <
                            # content <
                            # nav bar <
                            cardFunction(

                                pData = pData,
                                pJoin = 'bottom',
                                pComponent = dbc.Col(),
                                pMargin = '0px 0px 0px 0px',
                                pPadding = '0px 0px 0px 0px',
                                pChildren = [

                                    html.Img(

                                        src = feed['image'],
                                        style = dict(

                                            **pData['feedStyle']['projectImgStyle'],
                                            borderTopLeftRadius = pData['templateStyle']['gBorderRadius'],
                                            borderTopRightRadius = pData['templateStyle']['gBorderRadius']

                                        )

                                    )

                                ]

                            ) if (feed['image']) else None,
                            cardFunction(

                                pData = pData,
                                pBorder = pBorder,
                                pComponent = dbc.Col(),
                                pMargin = '0px 0px 0px 0px',
                                pPadding = '5px 5px 4px 5px',
                                pJoin = 'bottom' if (not feed['image']) else 'none',
                                pDescription = pData['myProjectData'][pPathname]['description'],
                                pTitle = [

                                    html.H1(

                                        children = pPathname.replace('-', ' '),
                                        style = pData['feedStyle']['feedH4TitleStyle']

                                    )

                                ] if (not feed['image']) else None,

                            ),
                            cardFunction(

                                pData = pData,
                                pBorder = pBorder,
                                pComponent = dbc.Col(),
                                pPadding = '3px 2px 3px 3px',
                                pChildren = [

                                    badgeFunction(

                                        pData = pData,
                                        pWidth = 'auto',
                                        pBorder = pBorder,
                                        pSubject = ['language', 'library'],
                                        pIterable = pData['myProjectData'][pPathname]

                                    )

                                ]

                            ),
                            cardFunction(

                                pData = pData,
                                pBorder = pBorder,
                                borderBottom = True,
                                pComponent = dbc.Col(),
                                pMargin = '0px 0px 0px 0px',
                                pPadding = '3px 2px 3px 3px',
                                pChildren = [

                                    badgeFunction(

                                        pData = pData,
                                        pType = 'link',
                                        pBorder = pBorder,
                                        pSubject = ['feedSubject'],
                                        pIterable = pData['myProjectData'][pPathname]

                                    )

                                ]

                            ),
                            cardFunction(

                                pJoin = 'top',
                                pData = pData,
                                pBorder = pBorder,
                                pComponent = dbc.Row(),
                                pPadding = '5px 10px 1px 0px',
                                pChildren = [

                                    # back <
                                    # update <
                                    # github <
                                    # website <
                                    *badgeIcon(

                                        pData = pData,
                                        isBack = True,
                                        pHref = 'myProject',
                                        pSrc = [pData['badgeData']['viewIcon']],
                                        pWidth = {'order' : 1, 'size' : 'auto'},
                                        pStyle = dict(padding = '0px 12px 0px 5px')

                                    ),
                                    *badgeIcon(

                                        pData = pData,
                                        pWidth = {'order' : 1, 'size' : 'auto'},
                                        pSrc = [pData['badgeData']['updateIcon']]

                                    ),
                                    dbc.Col(

                                        width = {'order' : 1},
                                        children = html.Small(

                                            children = pData['myProjectData'][pPathname]['update'],
                                            style = dict(

                                                color = pData['templateStyle']['gColorWhite'],
                                                fontFamily = pData['templateStyle']['gFontFamily']

                                            )

                                        )

                                    ),
                                    badgeIcon(

                                        pData = pData,
                                        isExternal = True,
                                        pWidth = {'order' : 2, 'size' : 'auto'},
                                        pHref = feed['link'] if ('link' in feed.keys()) else None,
                                        pSrc = [pData['badgeData']['linkIcon']] if ('link' in feed.keys()) else None

                                    )[0] if (feed['link']) else None,
                                    *badgeIcon(

                                        pData = pData,
                                        isExternal = True,
                                        pWidth = {'order' : 2, 'size' : 'auto'},
                                        pSrc = [pData['badgeData']['githubIcon']],
                                        pHref = pData['myProjectData'][pPathname]['projectLink']

                                    )

                                    # >

                                ]

                            )

                            # >

                        ]

                    )

                ]

            )

            # >

        ]

    )
