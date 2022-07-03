from django.urls import path
from . import views
from MovingWebApp import settings
from django.contrib.staticfiles.urls import static

urlpatterns = [
      # Path Converters
      # int: numbers
      # str: strings
      # path: whole urls /
      # slug: hyphen-and_underscores_stuff
      # UUID: universally unique identifier

      path('', views.home, name="home"),
      path('create_box', views.create_box, name="create-box"),
      path('box_list', views.box_list, name="box-list"),
      path('edit_box/<box_id>', views.edit_box, name="edit-box"),
      path('delete_box/<box_id>', views.delete_box, name="delete-box"),
      path('add_item/<box_id>', views.add_item, name="add-item"),
      path('edit_item/<item_id>', views.edit_item, name="edit-item"),
      path('delete_item/<item_id>', views.delete_item, name="delete-item"),
      path('search_boxes', views.search_boxes, name="search-boxes"),
      path('print_pdf', views.print_pdf, name="print-pdf"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)