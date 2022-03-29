from rest_framework.routers import Route, SimpleRouter


class CustomFollowRouter(SimpleRouter):

    routes = [
        Route(
            url=r'^{prefix}/$',
            mapping={'get': 'list', 'post': 'create'},
            name='{basename}',
            detail=False,
            initkwargs={'suffix': ''},
        ),
    ]
