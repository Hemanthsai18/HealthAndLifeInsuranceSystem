from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('index', views.index, name='index'),
    path('about', views.about, name='about'),
    path('blog-single',views.blog_single, name='blog-single'),
    path('blog',views.blog,name='blog'),
    path('general',views.general,name='general'),
    path('heart',views.heart,name='heart'),
    path('cancer',views.cancer,name='cancer'),
    path('term',views.pension,name='term'),
    path('pension',views.pension,name='pension'),
    path('endownment',views.endownment,name='endownment'),
    path('contact',views.contact, name='contact'),
    path('index-2',views.index_2, name='index-2'),
    path('portfolio-details',views.portfolio_details, name='portfolio-details'),
    path('portfolio',views.portfolio, name='portfolio'),
    # path('services',views.services, name='services'),
    path('team', views.team, name='team'),
    path('health',views.health,name='health'),
    path('life',views.life, name='life'),
    path('login',views.login, name='login'),
    path('logout',views.logout, name='logout'),
    path('register',views.register, name='register'),
    path('calculator',views.calculator,name='calculator'),
    path('term_calculation',views.term_calculation,name='term_calculation'),
    path('pension_calculation',views.pension_calculation,name='pension_calculation'),
    path('term_calculation1',views.term_calculation1,name='term_calculation1'),
    path('term_calculation2',views.term_calculation2,name='term_calculation2'),
    path('buy',views.buy,name='buy'),
    path('get_values',views.get_values,name='get_values'),
    path('profile2',views.profile2,name='profile2'),
     path('profile',views.profile,name='profile'),
]