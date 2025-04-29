from django.urls import re_path
from  plugins.scripts import views

urlpatterns = [
    re_path(r'^$', views.scripts_manager, name='scripts_manager'),
    re_path(
        r"^transform-abstracts/$",
        views.transform_abstract_view,
        name="transform_abstracts",
    ),
    re_path(
        r"^transform-titles/$",
        views.transform_title_view,
        name="transform_titles",
    ),
]
