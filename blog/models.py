from django.db import models

class Blogpost(models.Model):
    post_id = models.AutoField(primary_key= True)
    title = models.CharField(max_length=150)
    head0 = models.CharField(max_length=5100, default="")
    chead0 = models.CharField(max_length=55000, default="")
    head1 = models.CharField(max_length=5500, default="")
    chead1 = models.CharField(max_length=555000, default="")
    head2 = models.CharField(max_length=1500, default="")
    chead2 = models.CharField(max_length=555000, default="")
    pub_date = models.DateField()
    thumbnail = models.ImageField(upload_to='blog/static', default="")

    def __str__(self):
        return self.title

