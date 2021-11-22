from django.contrib import admin
from django.urls import path  , include
from django.conf.urls.static import static
from . import settings

urlpatterns = [
    
    path('account',include('accounts.urls')),
    path('stock/',include('stock.urls')),
    path('admin/', admin.site.urls),
    path('accounts/', include('registration.backends.default.urls')),
    path('' , include('store.urls'))
]
urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
# + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
