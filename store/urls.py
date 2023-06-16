from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views 

urlpatterns = [
    path('',views.home , name = "home"),
    path('profile/<int:id>',views.profile, name = "profile"),
    path('accounts/profile',views.profile,name='profile'),
    path('new/post',views.new_post,name="new_post"),
    
    path('createprofile',views.create_profile,name="create_profile"),
    path('search/',views.search_results,name="search_results"),
    path('image/<int:id>',views.one_image,name='single_image'),
    path('likes/<int:id>', views.likes, name='likes'),





    ]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)