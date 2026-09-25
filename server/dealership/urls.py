from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("dealers/", views.get_dealers, name="get_dealers"),
    path("dealers", views.get_dealers, name="get_dealers_no_slash"),
    path("dealer/<int:dealer_id>/", views.get_dealer, name="get_dealer"),
    path("dealer/<int:dealer_id>", views.get_dealer, name="get_dealer_no_slash"),
    path("reviews/dealer/<int:dealer_id>/", views.get_reviews, name="get_reviews"),
    path("reviews/dealer/<int:dealer_id>", views.get_reviews, name="get_reviews_no_slash"),
    path("dealers/<str:state>/", views.dealers_by_state, name="dealers_by_state"),
    path("dealers/<str:state>", views.dealers_by_state, name="dealers_by_state_no_slash"),
    path("get_cars/", views.get_cars, name="get_cars"),
    path("get_cars", views.get_cars, name="get_cars_no_slash"),
    path("add_review/", views.add_review, name="add_review"),
    path("add_review", views.add_review, name="add_review_no_slash"),
    path("login/", views.login_user, name="login"),
    path("login", views.login_user, name="login_no_slash"),
    path("logout/", views.logout_user, name="logout"),
    path("logout", views.logout_user, name="logout_no_slash"),
    path("register/", views.registration, name="register"),
    path("register", views.registration, name="register_no_slash"),
    path("djangoapp/register", views.registration, name="djangoapp_register"),
]
