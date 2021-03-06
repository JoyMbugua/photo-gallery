from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField


class Location(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
    def save_loc(self):
        self.save()

    def delete_loc(self):
        self.delete()

    def update_location(self, new_name):
       self.name = new_name


class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
    
    def save_cat(self):
        self.save()

    def delete_cat(self):
        self.delete()

    def update_category(self, new_name):
        self.name = new_name

class Photos(models.Model):
    caption = models.CharField(max_length=200)
    date_posted = models.DateTimeField(auto_now_add=True)
    location = models.ForeignKey(Location, models.SET_NULL, blank=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    image = CloudinaryField('image')

    class Meta:
        ordering = ['id']

    def __unicode__(self):
        try:
            public_id = self.image.public_id
        except AttributeError:
            public_id = ''
        return "Photo <%s:%s>" % (self.title, public_id)

    def __str__(self):
        return self.caption

    def save_image(self):
        self.save()

    def delete_image(self):
        self.delete()

    def update_image(self, caption, location, owner):
        self.caption = caption
        self.location = location

        self.owner = owner
        
    @classmethod
    def filter_by_location(cls, location):
        image = cls.objects.filter(location__name=location)
        return image

    @classmethod
    def search_by_term(cls, search_term):
        photo = cls.objects.filter(category__name=search_term)
        return photo






