from django.conf import settings
from django.contrib import admin
from django.urls import include, path
from graphql_extensions.views import GraphQLView
from graphql_jwt.decorators import jwt_cookie
from django.conf.urls.static import static

from apps.products.views import image

urlpatterns = [
    path('graphql-web/', jwt_cookie(GraphQLView.as_view(graphiql=True))),
    path('image', image)
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns.append(path('admin/', admin.site.urls))
    urlpatterns.append(path('__debug__/', include(debug_toolbar.urls)))
