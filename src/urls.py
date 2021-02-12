from django.conf import settings
from django.contrib import admin
from django.urls import include, path
from graphene_django.views import GraphQLView

urlpatterns = [
    path('graphql/', GraphQLView.as_view(graphiql=True)),
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns.append(path('admin/', admin.site.urls))
    urlpatterns.append(path('__debug__/', include(debug_toolbar.urls)))

