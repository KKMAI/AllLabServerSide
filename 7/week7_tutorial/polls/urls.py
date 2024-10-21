from django.urls import path

from . import views

# urlpatterns = [
#     # ex: /polls/
#     path("", views.index, name="index"),
#     # ex: /polls/5/
#     path("<int:question_id>/", views.detail, name="detail"),
#     # ex: /polls/5/vote/
#     path("<int:question_id>/vote/", views.vote, name="vote"),
# ]

urlpatterns = [
    # in string is instance , find match from above to below
    # ex: / >> dependence on urls.py in setting
    path("", views.IndexView.as_view(), name="employee"),
    # ex: /5/ : argument
    path("<int:question_id>/", views.PollView.as_view(), name="detail"),
    # ex: /5/vote/
    path("<int:question_id>/vote/", views.VoteView.as_view(), name="vote"),
]

# re_path(r"^articles/(?P<year>[0-9]{4})/$", views.year_archive)
# -- year is expression

# path("articles/<int:year>/<int:month>/", views.month_archive)
# in argument in view the name expression should be the same like year, month but order not serious bc. django will manage