"""
URL configuration for farmersproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from django.conf import settings
from django.conf.urls.static import static

from farmerapp import views as farmerviews
from govtapp import views as govtviews
from adminapp import views as adminviews
from expertapp import views as expertviews

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',farmerviews.index,name="index"),
    path('about/',farmerviews.about,name="about"),
    path('admin-login/',farmerviews.adminlogin,name="adminlogin"),
    path('farmer-login/',farmerviews.farmerlogin,name="farmerlogin"), 
    path('farmer-register/',farmerviews.farmerregister,name="farmerregister"),
    path('govt-officer-register/',farmerviews.govtlogin,name="govtlogin"),
    path('agriculture-experts/',farmerviews.expertlogin,name="expertlogin"),
    path('contact/',farmerviews.contact,name="contact"),



    path('farmer-dashboard/',farmerviews.dashboard,name="dashboard"),
    path('crop-disease-detection/',farmerviews.cropdisease,name="cropdisease"),
    path('profile/',farmerviews.profile,name="profile"),
    path('farmer-appointments/',farmerviews.appointments,name="farmer_appointments"),
    path('farmer-request-appiontment/',farmerviews.askappiontment,name="askappiontment"),
    path('farmer-feedback/',farmerviews.feedback,name="farmer_feedback"),
    path('logout/',farmerviews.user_logout,name="log_out"),
    path('chatbot/',farmerviews.chatbot,name="chatbot"),
    path('helpdesk/',farmerviews.helpdesk,name="helpdesk"),
    path('helpdesk-hindi/',farmerviews.helpdesk_hin,name="helpdesk_hin"),
    path('helpdesk-telugu/',farmerviews.helpdesk_tel,name="helpdesk_tel"),








    path('govt-officer',govtviews.index,name="govt_dashboard"),
    path('all-users/', govtviews.all_users, name='all_users'),
    path('pending-users/', govtviews.pending_users, name='pending_users'),
    path('feedback/', govtviews.feedback, name='feedback'),
    path('sentiment/', govtviews.sentiment, name='sentiment'),
    path('govt-graph/', govtviews.graph, name='govt_graph'),

    path('accept-user/<int:user_id>/', govtviews.accept_user, name='accept_user'),
    path('reject-user/<int:user_id>/', govtviews.reject_user, name='reject_user'),
    path('delete-user/<int:user_id>/', govtviews.delete_user, name='delete_user'),





    path("admin-dashboard/",adminviews.admin_index,name="admin_dashboard"),
    path("farmer-details/",adminviews.farmer_details,name="farmer_details"),
    path('view-farmer-details/<int:farmer_id>/', adminviews.view_farmer_details, name='view_farmer_details'),
    path("upload-dataset/",adminviews.upload_dataset,name="upload_dataset"),
    path("model-training/",adminviews.model_train,name="model_train"),
    path("admin-graph/",adminviews.graph,name="graph"),
    path("admin-feedback/",adminviews.feedback,name="admin_feedback"),
    path("admin-sentiment/",adminviews.sentiment,name="admin_sentiment"),
    path("admin-sentiment-graph/",adminviews.sentiment_graph,name="admin_sentiment_graph"),
    path('feedback/delete/<int:feedback_id>/', adminviews.delete_feedback, name='delete_feedback'),
     path('feedback/reply/<int:feedback_id>/', adminviews.reply_feedback, name='reply_feedback'),



    path("expert-dashboard/",expertviews.index,name="expert_dashboard"),
    path("expert-helpdesk/",expertviews.helpdesk,name="expert_helpdesk"),
    path("expert-helpdesk-queries/<int:query_id>/",expertviews.view_queries,name="view_queries"),
    path("expert-helpdesk-queries-respond",expertviews.view_queries_respond,name="view_queries_respond"),
    path("expert-pending-appionments",expertviews.pending_appionments,name="pending_appionments"),
    path("expert-view-appionments",expertviews.view_appiontment,name="view_appiontment"),




    path('accept-appointment/<int:appiontment_id>/',expertviews.accept_appointment, name='accept_appointment'),
    path('delete-appointment/<int:appiontment_id>/', expertviews.delete_appointment, name='delete_appointment'),
    path('cancel-appointment/<int:appointment_id>/', expertviews.cancel_appointment, name='cancel_appointment'),

    path("view-responses/",expertviews.view_responses,name="expert_view_responses"),
    path("edit-responses/<int:response_id>/",expertviews.edit_response,name="edit_response"),














    




    
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)