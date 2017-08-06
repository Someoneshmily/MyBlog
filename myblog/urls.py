from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^myblog/data/$', views.data),
    url(r'^myblog/formdata/$' ,views.formdata),
    url(r'^myblog/create/$', views.create),
    url(r'^myblog/delete/$', views.delete),
    url(r'^myblog/edit/$', views.edit),
    url(r'^myblog/findAll/$', views.findAll),
    url(r'^myblog/edit_content/(\d+)/$', views.edit_html),
    # url(r'^find_one/(\d+)/$', views.findOne),
    url(r'^myblog/leave_msg/$', views.leave_msg),
    url(r'^myblog/create_msg/$', views.create_msg),
    url(r'^myblog/msg_data/$', views.msg_data),

]