from django.urls import path

from . import views

urlpatterns = [
    # ex: /
    path("", views.IndexView.as_view(), name="index"),
    # ex: /position/
    path("position/", views.PositionView.as_view(), name="position"),
    # ex: /project/
    path("project/", views.ProjectView.as_view(), name="project"),

    path("project/<int:project_id>/", views.ProjectView.as_view(), name="project_delete"),
    # ex: /project/5/ ได้ project_id ตรงนี้มาบอกว่าลบตัวไหน

    path("project/detail/<int:project_id>/", views.ProjectDetailView.as_view(), name="project_detail"),

    path("project/detail/<int:project_id>/<int:employee_id>/", views.ProjectDetailView.as_view(), name="project_delete_emp"),



    # extend week 8

    path("layout/", views.LayoutView.as_view(), name="layout"),

    path("employee2/", views.IndexView2.as_view() , name="index2"),

    path("position2/", views.PositionView2.as_view(), name="position2"),

    path("project2/", views.ProjectView2.as_view(), name="project2"),

    path("project2/<int:project_id>/", views.ProjectView2.as_view(), name="project_delete2"),

    path("project2/detail/<int:project_id>/", views.ProjectDetailView2.as_view(), name="project_detail2"),

    path("project2/detail/<int:project_id>/<int:employee_id>/", views.ProjectDetailView2.as_view(), name="project_delete_emp2"),
]
# ex: /polls/5/vote/