from django.urls import path
from WebApp import views


urlpatterns=[
    path('',views.home_page,name="Home"),
    path('About/',views.about_page,name="About"),
    path('Contact/',views.contact_page,name="Contact"),
    path('Our Products/',views.our_products,name="Our Products"),
    path('save_contact/',views.save_contact,name="save_contact"),
    path('filtered_product/<cat_name>/',views.filtered_product,name="filtered_product"),
    path('single_product/<int:prod_id>/',views.single_product,name="single_product"),
    path('registeration_page/',views.registeration_page,name="registeration_page"),
    path('save_registeration/',views.save_registeration,name="save_registeration"),
    path('Userlogin/',views.Userlogin,name="Userlogin"),
    path('userlogout/',views.userlogout,name="userlogout"),
    path('save_cart/',views.save_cart,name="save_cart"),
    path('cart_page/',views.cart_page,name="cart_page"),
    path('delete_cart/<int:p_id>/',views.delete_cart,name="delete_cart"),
    path('userlogin_page/',views.userlogin_page,name="userlogin_page"),
    path('checkout_page/',views.checkout_page,name="checkout_page"),
    path('payment_page/',views.payment_page,name="payment_page"),
    path('save_placeorder/',views.save_placeorder,name="save_placeorder")

]