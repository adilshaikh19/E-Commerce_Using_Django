
import site
from django.contrib import admin
from django.urls import path ,include
admin.site.site_header="PrimeMart"

urlpatterns = [
    
    path('admin/', admin.site.urls),
    path('',include('app.urls')),
    # path('jet/', include('jet.urls', 'jet'))
]
