from django.conf import settings
from django.contrib import admin
from django.urls import include, path
from graphql_extensions.views import GraphQLView
from graphql_jwt.decorators import jwt_cookie

urlpatterns = [
    path('graphql-web/', jwt_cookie(GraphQLView.as_view(graphiql=True)))
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns.append(path('admin/', admin.site.urls))
    urlpatterns.append(path('__debug__/', include(debug_toolbar.urls)))

