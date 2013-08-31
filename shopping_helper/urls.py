from django.conf.urls import patterns, include, url
from rest_framework import viewsets, routers
from shopping.models.store import Store
from shopping.models.address import Address
from shopping.models.rating import Rating


# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()


# ViewSets define the view behavior.
class StoreViewSet(viewsets.ModelViewSet):
    model = Store

class AddressViewSet(viewsets.ModelViewSet):
    model = Address

class RatingViewSet(viewsets.ModelViewSet):
    model = Rating

# Routers provide an easy way of automatically determining the URL conf
router = routers.DefaultRouter()
router.register(r'stores', StoreViewSet)
router.register(r'addresses', AddressViewSet)
router.register(r'ratings', RatingViewSet)

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'shopping_helper.views.home', name='home'),
    #url(r'^shopping_helper/', include('shopping_helper.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),

	url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
)
