from django.urls import path
from post.views import home , postDetail , tags , category , Contact , ContactSuccess

urlpatterns = [
    path('', home ,name= 'home'),
    path('category/<slug:category_slug>', category ,name= 'categories'),
    path('tag/<slug:tag_slug>', tags ,name= 'tags'),
    path('<slug:post_slug>', postDetail ,name= 'postDetail'),
    path('contact/', Contact , name = 'contact'),
    path('contact/success/',ContactSuccess, name = 'contactsuccess'),
]
