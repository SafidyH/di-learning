from gameh import views

urlpatterns = [
    # Autres URLs de l'application...
    path('signup/', views.signup, name='signup'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
]