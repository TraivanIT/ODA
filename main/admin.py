from django.contrib import admin
from .models import *
from django_summernote.admin import SummernoteModelAdmin


admin.site.site_header = "odaopportunitiescambodia.org"
admin.site.site_title = "ODA Admin Area"
admin.site.index_title = "Welcome ODA Admin site"

#HomeText
class HomeAdmin(SummernoteModelAdmin):
    summernote_fields = ('objective','mission','donate','getinvolved')


#HomeSliderText
#class HomeSliderTextAdmin(SummernoteModelAdmin):
    #summernote_fields = ('home_slider_text',)
#home model and related
class SliderTextInline(admin.TabularInline):
    model = HomeSliderText


#HomeSlider
class HomeSliderAdmin(admin.ModelAdmin):
    inlines = [SliderTextInline]



#KidsDream
class KidsDreamTextSliderInline(admin.TabularInline):
    model = KidsDreamTextSlider


class KidsDreamAdmin(admin.ModelAdmin):
    inlines = [KidsDreamTextSliderInline]


class KidsDreamTextAdmin(SummernoteModelAdmin):
    summernote_fields = ('kids_dream_text',)


#WishList
class WishListSliderTextInline(admin.TabularInline):
    model = WishListSliderText


class WishListSliderAdmin(admin.ModelAdmin):
    inlines = [WishListSliderTextInline]


class WishListTextAdmin(SummernoteModelAdmin):
    summernote_fields = ('wish_list_text',)

#Donate
class DonateTextAdmin(SummernoteModelAdmin):
    summernote_fields = ('donate_text',)


class DonateSliderTextInline(admin.TabularInline):
    model = DonateSliderText


class DonateSliderAdmin(admin.ModelAdmin):
    inlines = [DonateSliderTextInline]







#home
admin.site.register(Home, HomeAdmin)
admin.site.register(HomeSlider, HomeSliderAdmin)
#KidsDream
admin.site.register(KidsDreamText, KidsDreamTextAdmin)
admin.site.register(KidsDream, KidsDreamAdmin)
#wishlist
admin.site.register(WishListText, WishListTextAdmin)
admin.site.register(WishListSlider, WishListSliderAdmin)
#Doante
admin.site.register(DonateText, DonateTextAdmin)
admin.site.register(DonateSlider, DonateSliderAdmin)
