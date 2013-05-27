from django.conf.urls import patterns, url

from .views import Index


base_patterns = patterns('',  # noqa
    url(r'^$', Index.as_view(), name='index'),
)

api_patterns = patterns('zenircbot.core',  # noqa
    url(r'^api/v1/submit$', 'api.submit', name='submit')
)

urlpatterns = base_patterns + api_patterns