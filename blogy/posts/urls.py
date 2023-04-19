from django.urls import path

from . import views

app_name = 'posts'

urlpatterns = [
    #     path('', views.home, name='home'),

    # Topics
    path('topics/', views.topics, name='topics'),
    path('topics/add/', views.add_topic, name='add_topic'),
    path('topics/<slug:topic_slug>/',
         views.view_topic, name='view_topic'),
    path('topics/<slug:topic_slug>/update/',
         views.update_topic, name='update_topic'),
    path('topics/<slug:topic_slug>/delete/',
         views.delete_topic, name='delete_topic'),

    # Articles
    path('articles/', views.articles, name='articles'),
    path('articles/<int:page>', views.articles_pages, name='articles_pages'),
    path('articles/add/', views.add_article, name='add_article'),
    path('articles/<slug:article_slug>/',
         views.view_article, name='view_article'),
    path('articles/<slug:article_slug>/update/',
         views.update_article, name='update_article'),
    path('articles/<slug:article_slug>/featured/',
         views.set_as_featured_article, name='set_as_featured_article'),
    path('articles/<slug:article_slug>/delete/',
         views.delete_article, name='delete_article'),

    # Authors
    path('authors/', views.authors, name='authors'),
    path('authors/<slug:username>/',
         views.view_author, name='view_author'),
    path('authors/<slug:username>/delete/',
         views.delete_author, name='delete_author'),

    # Articles
    path('comments/', views.comments, name='comments'),
    path('comments/<int:page>', views.comments_pages, name='comments_pages'),
    path('articles/<slug:article_slug>/comments/add/',
         views.add_comment, name='add_comment'),
    path('comments/<slug:comment_slug>/',
         views.view_comment, name='view_comment'),
    path('comments/<slug:comment_slug>/update/',
         views.update_comment, name='update_comment'),
    path('comments/<slug:comment_slug>/delete/',
         views.delete_comment, name='delete_comment'),

    # Reactions
    path('reactions/', views.reactions, name='reactions'),
    #     path('reactions/add/', views.add_reaction, name='add_reaction'),
    #     path('reactions/<slug:reaction_slug>/',
    #          views.view_reaction, name='view_reaction'),
    #     path('reactions/<slug:reaction_slug>/update/',
    #          views.update_reaction, name='update_reaction'),
    #     path('reactions/<slug:reaction_slug>/delete/',
    #          views.delete_reaction, name='delete_reaction'),


    # # Discounts
    # path('discounts/', views.discounts, name='discounts'),
    # path('discounts/add/', views.add_discount, name='add_discount'),
    # path('discounts/<slug:discount_slug>/',
    #      views.view_discount, name='view_discount'),
    # path('discounts/<slug:discount_slug>/update/',
    #      views.update_discount, name='update_discount'),
    # path('discounts/<slug:discount_slug>/delete/',
    #      views.delete_discount, name='delete_discount'),


    # # Categories
    # path('categories/', views.categories, name='categories'),
    # path('categories/add/', views.add_category, name='add_category'),
    # path('categories/<slug:category_slug>/',
    #      views.view_category, name='view_category'),
    # path('categories/<slug:category_slug>/update/',
    #      views.update_category, name='update_category'),
    # path('categories/<slug:category_slug>/delete/',
    #      views.delete_category, name='delete_category'),


    # # Sub-Categories
    # path('categories/<slug:category_slug>/sub-categories/add/',
    #      views.add_sub_category, name='add_sub_category'),
    # path('categories/<slug:category_slug>/sub-categories/<slug:sub_category_slug>/',
    #      views.view_sub_category, name='view_sub_category'),
    # path('categories/<slug:category_slug>/sub-categories/<slug:sub_category_slug>/update/',
    #      views.update_sub_category, name='update_sub_category'),
    # path('categories/<slug:category_slug>/sub-categories/<slug:sub_category_slug>/delete/',
    #      views.delete_sub_category, name='delete_sub_category'),


    # # Products
    # path('products/', views.products, name='products'),
    # path('products/add/', views.add_product, name='add_product'),
    # path('products/<slug:product_slug>/',
    #      views.view_product, name='view_product'),
    # path('products/<slug:product_slug>/update/',
    #      views.update_product, name='update_product'),
    # path('products/<slug:product_slug>/delete/',
    #      views.delete_product, name='delete_product'),


    # # Product Units
    # path('products/<slug:product_slug>/product-units/add/',
    #      views.add_product_unit, name='add_product_unit'),
    # path('products/<slug:product_slug>/product-units/<slug:product_unit_slug>/',
    #      views.view_product_unit, name='view_product_unit'),
    # path('products/<slug:product_slug>/product-units/<slug:product_unit_slug>/update/',
    #      views.update_product_unit, name='update_product_unit'),
    # path('products/<slug:product_slug>/product-units/<slug:product_unit_slug>/set-is-default/',
    #      views.set_is_default_product_unit, name='set_product_unit_as_default'),
    # path('products/<slug:product_slug>/product-units/<slug:product_unit_slug>/delete/',
    #      views.delete_product_unit, name='delete_product_unit'),


    # # Product Specifications
    # path('products/<slug:product_slug>/product-specifications/add/',
    #      views.add_product_specification, name='add_product_specification'),
    # path('products/<slug:product_slug>/product-specifications/<slug:product_specification_slug>/update/',
    #      views.update_product_specification, name='update_product_specification'),
    # path('products/<slug:product_slug>/product-specifications/<slug:product_specification_slug>/delete/',
    #      views.delete_product_specification, name='delete_product_specification'),


    # # Product Specification Values
    # path('products/<slug:product_slug>/product-units/<slug:product_unit_slug>/product-specifications/<slug:product_specification_slug>/product-specification-values/add/',
    #      views.add_product_specification_value, name='add_product_specification_value'),
    # path('products/<slug:product_slug>/product-units/<slug:product_unit_slug>/product-specifications/<slug:product_specification_slug>/product-specification-values/<slug:product_specification_value_slug>/update/',
    #      views.update_product_specification_value, name='update_product_specification_value'),
    # path('products/<slug:product_slug>/product-units/<slug:product_unit_slug>/product-specifications/<slug:product_specification_slug>/product-specification-values/<slug:product_specification_value_slug>/delete/',
    #      views.delete_product_specification_value, name='delete_product_specification_value'),


    # # Product Reviews
    # path('products/<slug:product_slug>/product-reviews/add/',
    #      views.add_product_review, name='add_product_review'),
    # path('products/<slug:product_slug>/product-reviews/<slug:product_review_slug>/update/',
    #      views.update_product_review, name='update_product_review'),
    # path('products/<slug:product_slug>/product-reviews/<slug:product_review_slug>/delete/',
    #      views.delete_product_review, name='delete_product_review'),


    # # Product Images
    # path('products/<slug:product_slug>/product-units/<slug:product_unit_slug>/product-unit-images/add/',
    #      views.add_product_unit_image, name='add_product_unit_image'),
    # path('products/<slug:product_slug>/product-units/<slug:product_unit_slug>/product-unit-images/<slug:product_unit_image_slug>/update/',
    #      views.update_product_unit_image, name='update_product_unit_image'),
    # path('products/<slug:product_slug>/product-units/<slug:product_unit_slug>/product-unit-images/<slug:product_unit_image_slug>/set-is-featured/',
    #      views.set_default_image_for_product_unit, name='set_default_image_for_product_unit'),
    # path('products/<slug:product_slug>/product-units/<slug:product_unit_slug>/product-unit-images/<slug:product_unit_image_slug>/delete/',
    #      views.delete_product_unit_image, name='delete_product_unit_image')
]