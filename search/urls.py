from django.urls import path
from . import views

urlpatterns = [
    path("list", views.ParagraphView.as_view(), name="para_view"),
    path(
        "list/<int:paragraph_id>", views.ParagraphDelete.as_view(), name="para_delete"
    ),
    path("search/<slug:word>", views.ParagraphSreach.as_view(), name="para_search"),
]
