from django.urls import path

from index import views

urlpatterns = [
    path('', views.index),
    path('sens_item/<slug:slug>', views.sensor_history, name="sens_item"),
    path('sens_item_edit/<pk>', views.sens_item_edit),
    path('sens_item_del/<pk>', views.sens_item_del)
]