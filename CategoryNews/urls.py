from django.urls import path, include
from .views import *

urlpatterns = [
    path('', home),
    path('alldelete',alldeletenews),
    path('listsports', ListSportsNews.as_view()),
    path('listbusiness', ListBusinessNews.as_view()),
    path('refresh',refresh),
    path('listgeneral', ListGeneralNews.as_view()),
    path('listhealth', ListHealthNews.as_view()),
    path('listentertainment', ListEntertainmnentNews.as_view()),
    path('listtechnology', ListTechonologyNews.as_view()),
    path('listscience', ListScienceNews.as_view()),
    # path('listsports/refresh',sprotsrefresh)

]
