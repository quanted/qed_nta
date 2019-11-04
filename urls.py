# Django 2.0 url import
from django.urls import include, path

print('qed.urls')
#appends to the list of url patterns to check against
urlpatterns = [
    path('', include('splash_app.urls')),
    path('nta/', include('nta_app.urls')),
]


handler404 = 'splash_app.views.landing.page_404'
handler500 = 'splash_app.views.landing.page_404'
handler403 = 'splash_app.views.landing.page_404'
