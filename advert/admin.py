from django.contrib import admin
from .models import Advert, Category, Reply

# Register your models here.
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
        list_display = ('name', 'id')
        #list_display_links = ('name')
        prepopulated_fields = { "slug" : ("name",) }



@admin.register(Advert)
class AdvertAdmin(admin.ModelAdmin):
    list_display = ('id',
                    'user',
                    "category",
                    "subject",
                    "description",
                    "created"


                    )
    prepopulated_fields = {"slug": ("subject",)}

@admin.register(Reply)
class ReplyAdmin(admin.ModelAdmin):

    list_display = ('id','user_reply', 'created')
     #
     #prepopulated_fields = {"slug": ("user_reply",)}