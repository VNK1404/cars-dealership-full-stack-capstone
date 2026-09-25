from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    # Dealers
    path("dealers/", views.get_dealers, name="get_dealers"),
    path("dealers", views.get_dealers, name="get_dealers_no_slash"),
    path("fetchDealers", views.get_dealers, name="fetchDealers"),
    path("fetchDealers/", views.get_dealers, name="fetchDealers_slash"),
    path("fetchDealer/<int:dealer_id>", views.get_dealer, name="fetchDealer"),
    path("fetchDealer/<int:dealer_id>/", views.get_dealer, name="fetchDealer_slash"),
    path("djangoapp/get_dealers", views.get_dealers, name="djangoapp_get_dealers"),
    path("djangoapp/get_dealers/", views.get_dealers, name="djangoapp_get_dealers_slash"),
    path("dealer/<int:dealer_id>/", views.get_dealer, name="get_dealer"),
    path("dealer/<int:dealer_id>", views.get_dealer, name="get_dealer_no_slash"),
    path("djangoapp/dealer/<int:dealer_id>", views.get_dealer, name="djangoapp_get_dealer"),
    # Reviews
    path("reviews/dealer/<int:dealer_id>/", views.get_reviews, name="get_reviews"),
    path("reviews/dealer/<int:dealer_id>", views.get_reviews, name="get_reviews_no_slash"),
    path("djangoapp/reviews/dealer/<int:dealer_id>", views.get_reviews, name="djangoapp_get_reviews"),
    path("fetchReviews/dealer/<int:dealer_id>", views.get_reviews, name="fetchReviews_dealer"),
    path("fetchReviews/dealer/<int:dealer_id>/", views.get_reviews, name="fetchReviews_dealer_slash"),
    # States
    path("dealers/<str:state>/", views.dealers_by_state, name="dealers_by_state"),
    path("dealers/<str:state>", views.dealers_by_state, name="dealers_by_state_no_slash"),
    path("djangoapp/get_dealers/<str:state>", views.dealers_by_state, name="djangoapp_get_dealers_state"),
    path("fetchDealers/<str:state>", views.dealers_by_state, name="fetchDealers_state"),
    # Cars
    path("get_cars/", views.get_cars, name="get_cars"),
    path("get_cars", views.get_cars, name="get_cars_no_slash"),
    path("djangoapp/get_cars", views.get_cars, name="djangoapp_get_cars"),
    # Add Review
    path("add_review/", views.add_review, name="add_review"),
    path("add_review", views.add_review, name="add_review_no_slash"),
    path("djangoapp/add_review", views.add_review, name="djangoapp_add_review"),
    # Sentiment Analysis
    path("analyze/", views.analyze_review_sentiment_view, name="analyze_sentiment"),
    path("analyze", views.analyze_review_sentiment_view, name="analyze_sentiment_no_slash"),
    path("djangoapp/analyze", views.analyze_review_sentiment_view, name="djangoapp_analyze"),
    path("analyze/<str:text>", views.analyze_by_text, name="analyze_by_text"),
    path("analyze/<str:text>/", views.analyze_by_text, name="analyze_by_text_slash"),
    # Auth
    path("login/", views.login_user, name="login"),
    path("login", views.login_user, name="login_no_slash"),
    path("djangoapp/login", views.login_user, name="djangoapp_login"),
    path("djangoapp/login/", views.login_user, name="djangoapp_login_slash"),
    path("logout/", views.logout_user, name="logout"),
    path("logout", views.logout_user, name="logout_no_slash"),
    path("djangoapp/logout", views.logout_user, name="djangoapp_logout"),
    path("djangoapp/logout/", views.logout_user, name="djangoapp_logout_slash"),
    path("register/", views.registration, name="register"),
    path("register", views.registration, name="register_no_slash"),
    path("djangoapp/register", views.registration, name="djangoapp_register"),
    path("djangoapp/register/", views.registration, name="djangoapp_register_slash"),
]
