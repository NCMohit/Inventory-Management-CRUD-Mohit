from django.urls import path, include
from .views import IndexView, CreateView, DeleteView, UpdateView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',IndexView.as_view(),name="crudindex"),
    path('create/',CreateView.as_view(),name='crudcreate'),
    path('delete/<int:entry_id>/',DeleteView.as_view(),name="cruddelete"),
    path('update/<int:entry_id>/',UpdateView.as_view(),name="crudupdate"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)