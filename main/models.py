from django.db import models
from django.contrib.auth.models import User

#model for Home Page
class HomeSlider(models.Model):
    author = models.ForeignKey(User, on_delete= models.CASCADE)
    image = models.ImageField(upload_to = 'images/')

    #create property for product url if image not exists
    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url


class Home(models.Model):
    author = models.ForeignKey(User, on_delete= models.CASCADE)
    objective = models.TextField()
    mission = models.TextField()
    donate = models.TextField()
    getinvolved = models.TextField()


#HomeSlider Text
class HomeSliderText(models.Model):
    home_slider = models.ForeignKey(HomeSlider, on_delete=models.CASCADE)
    home_slider_text = models.TextField()


#Kids Dream model
class KidsDream(models.Model):
    author = models.ForeignKey(User, on_delete= models.CASCADE)
    image = models.ImageField(upload_to = 'kidsdream/')

    #create property for product url if image not exists
    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url


class KidsDreamTextSlider(models.Model):
    kids_dream = models.ForeignKey(KidsDream, on_delete=models.CASCADE)
    kids_dream_text_slider = models.TextField()


class KidsDreamText(models.Model):
    author = models.ForeignKey(User, on_delete= models.CASCADE)
    kids_dream_text = models.TextField()


#wishlist models
class WishListSlider(models.Model):
    author = models.ForeignKey(User, on_delete= models.CASCADE)
    image = models.ImageField(upload_to = 'wishlist/')

    #create property for product url if image not exists
    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url


class WishListSliderText(models.Model):
    wish_list_slider = models.ForeignKey(WishListSlider, on_delete=models.CASCADE)
    wish_list_slider_text = models.CharField(max_length=500,)


class WishListText(models.Model):
    author = models.ForeignKey(User, on_delete= models.CASCADE)
    wish_list_text = models.TextField()


#donate
class DonateSlider(models.Model):
    author = models.ForeignKey(User, on_delete= models.CASCADE)
    image = models.ImageField(upload_to = 'donate/')

    #create property for product url if image not exists
    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url


class DonateSliderText(models.Model):
    donate_slider = models.ForeignKey(DonateSlider, on_delete=models.CASCADE)
    donate_slider_text = models.TextField()



class DonateText(models.Model):
    author = models.ForeignKey(User, on_delete= models.CASCADE)
    donate_text = models.TextField()
