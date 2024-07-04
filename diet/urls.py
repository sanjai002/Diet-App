from django.urls import path

from . import views


urlpatterns=[
    path('',views.index,name='index'),
    path('register',views.register,name="register"),
    path('login',views.user_login,name='login'),
    path('details',views.details,name='details'),
    path('food/food_view',views.foodview,name='food_track'),
    path('food/add_food/<int:food_id>',views.add_food,name='add_food'),
    path('food/delete_food/<int:food_id>',views.delete_food,name='delete_food'),
    path('logout_view',views.logout_view,name='logout_view'),
    path('foods/food_list/', views.food_list, name='food_list'),
    path('foods/food_list/search_food/',views.search_food,name='search_food'),
    path('blood_list/',views.blood_list,name="blood_list"),
    path('blood_register/',views.blood_register,name="blood_register"),
    path('food_details/<int:food_id>/',views.food_details_view,name="food_details"),
    path('foods/foods_list/calorie_view',views.food_consumption, name='calorie_view'),
    path('disease',views.disease_prediction,name='disease_prediction'),
    path('disease/diabetics_prediction',views.diabetes_detection,name='diabetics_prediction'),
    path('disease/heart_disease_prediction',views.predict_heart_disease,name='heart_disease_prediction'),
    path('disease/malnutrition_prediction',views.predict_image,name='malnutrition_prediction'),
    path('articles',views.article,name="article"),
    path('article/<int:article_id>/', views.article_detail, name='article_detail'),
    path('chatbot',views.chatbot,name='chatbot'),
    path('generate/', views.generate_text, name='generate_text'),
    path('profile/',views.update_profile,name='profile'),
    path('change-password/', views.change_password, name='change_password'),




]