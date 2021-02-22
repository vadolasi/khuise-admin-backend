from django.conf import settings
from django.contrib import admin
from django.urls import include, path
from graphene_file_upload.django import FileUploadGraphQLView as GraphQLView
from graphql_jwt.decorators import jwt_cookie

urlpatterns = [
    path('graphql-web/', jwt_cookie(GraphQLView.as_view(graphiql=True))),
    path('graphql-mobile/', GraphQLView.as_view())
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns.append(path('admin/', admin.site.urls))
    urlpatterns.append(path('__debug__/', include(debug_toolbar.urls)))

