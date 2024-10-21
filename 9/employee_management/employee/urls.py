from django.urls import path

from . import views

urlpatterns = [
    path("", views.EmployeeView.as_view(), name='employee'),
    path("position/", views.PositionView.as_view(), name='position'),
    path("project/", views.ProjectView.as_view(), name='project'),
    path("projectdelete/<int:project_id>/", views.ProjectView.as_view(), name='projectdelete'),
    path("projectdetail/<int:project_id>/", views.ProjectDetailView.as_view(), name='projectdetail'),
    path("addstaff/<int:project_id>/<int:staff_id>/", views.ProjectDetailView.as_view(), name='addstaff'),
    path("deletestaff/<int:project_id>/<int:staff_id>/", views.ProjectDetailView.as_view(), name='deletestaff'),

    path("employee_form/", views.Employee_FormView.as_view(), name='employee_form'),
    path("project_form/", views.Project_FormView.as_view(), name="project_form"),
    path("project_form_edit/<int:project_id>", views.Edit_Project_FormView.as_view(), name="project_form_edit")
]