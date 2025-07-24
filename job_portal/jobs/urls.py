from django.urls import path 
from . import views 
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', views.job_list, name='job_list'),
    path('<int:job_id>/', views.job_detail, name='job_detail'),
    path('post/', views.job_post, name='job_post'),
    path('edit-profile/', views.edit_profile, name='edit_profile'),
    path('job/<int:job_id>/applications/', views.job_applications_view, name='job_applications'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)