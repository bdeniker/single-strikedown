from django.conf.urls.defaults import *
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    # Example:
    # (r'^test_project/', include('test_project.foo.urls')),

    ('^admin/', include(admin.site.urls)),
)
