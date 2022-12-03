
# from django.conf.urls import path
from django.urls import path, include
from django.contrib import admin

from django.conf.urls import url

from rest_framework.schemas import get_schema_view
from django.urls import path

from rest_framework_simplejwt import views as jwt_views
# from api.views import GoogleLogin

from drf_yasg import openapi
from drf_yasg.views import get_schema_view

from django.conf import settings
from django.conf.urls.static import static


schema_view = get_schema_view(
    openapi.Info(
        #  add your swagger doc title
        title="Showroom API",
        #  version of the swagger doc
        default_version='v1',
        # first line that appears on the top of the doc
        description="Test description",
    ),
    public=True,
)


urlpatterns = [
    path('admin/', admin.site.urls),

    path('api/', include('api.urls')),

    # path('api/token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),

    path('schema', schema_view),
    path('auth/', include('rest_auth.urls')),
    # path('social-login/google/', GoogleLogin.as_view(), name='google_login'),
    path('', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


