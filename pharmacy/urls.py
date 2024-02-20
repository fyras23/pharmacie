from django.urls import path
from . import views
""" app_name = 'pharmacy', """
urlpatterns = [
#<--------------------------------for the med------------------------------------------------->
 path('medicaments', views.index, name='medicaments'),
path('del_med/<int:id>', views.del_med, name='del_med'),
path('update_med/<int:id>', views.update_med,name='update_med'),
path('update_med/update_med_aplly/<int:id>',views.update_med_aplly, name='update_med_aplly'),
path('addNew/', views.add, name='add'),
path('addNew/add_med/', views.add_med, name='add_med'),
#<---------------------------------------------------------------------------------------------------->     



#<--------------------------------for the type-------------------------------------------------------->
path('type/',views.skills,name='type' ),
path('type/del_type/<int:id>', views.del_type, name='del_type'),
path('type/update_type/<int:id>', views.update_type,name='update_type'),
path('type/update_type/update_type_aplly/<int:id>',views.update_type_aplly, name='update_type_aplly'),
path('type/addType/', views.addType, name='addType'),
path('type/addType/add_type/', views.add_type, name='add_type'),
#<------------------------------------------------------------------------------------------------------>     


     
#<-------------------------------for the user--------------------------------------------------------->
path('users/', views.list_users, name='users'),
path('users/createUser/', views.create_compte, name='create_compte'),
path('users/createUser/add_user_action/', views.create_user_action,name='create_user_action'),
path('users/del_user/<int:id>', views.del_user, name='del_user'),
#<------------------------------------------------------------------------------------------------------>


#<-----------------------------------for login----------------------------------------------------------->
path('', views.connect, name='connect'),
path('login/', views.signIn, name='signIn'),
path('login/login/', views.signIn, name='signIn'),
path('disconnect/', views.signOut, name='disconnect'),





path('change_history', views.change_history, name='change_history'),


]