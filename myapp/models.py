from django.db import models


class ProjectCategory(models.Model):
    name = models.CharField(max_length=200, null=True, blank=False)

    def __str__(self):
        return self.name


class PhotoFor(models.Model):
    image = models.ImageField(null=True, blank=False)
    title = models.CharField(max_length=255, null=True, blank=False)
    link = models.CharField(max_length=255, null=True, blank=False)

    def __str__(self) -> str:
        return self.title


class Comments(models.Model):
    name = models.CharField(max_length=255, null=False, blank=False)
    comment = models.TextField(blank=False)
    image = models.ImageField(
        null=True, upload_to='profile', default='default.jpeg')
    published = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    @property
    def imageURL(self):
        """This function for to fix images url"""
        try:
            url = self.image.url
        except:
            url = ""
        return url


class AddProject(models.Model):

    SIDE_CHOICES = (
        ("left", "left"),
        ("right", "right"),
    )

    category = models.ForeignKey(
        ProjectCategory, on_delete=models.CASCADE, null=True)
    side = models.CharField(blank=False, null=True,
                            choices=SIDE_CHOICES, max_length=5)
    image = models.ImageField(null=True, blank=False)
    title = models.CharField(max_length=27, null=True, blank=False)
    body = models.CharField(max_length=96, null=True, blank=False)
    link = models.CharField(max_length=255, null=True, blank=False)
    published = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['published']


class AddInformation(models.Model):
    title = models.CharField(max_length=300, null=True, blank=False)
    body = models.TextField(null=True, blank=False)

    def __str__(self) -> str:
        return self.title


class AddInformation1(models.Model):
    title = models.CharField(max_length=300, null=True, blank=False)
    body = models.TextField(null=True, blank=False)

    def __str__(self) -> str:
        return self.title


class GetInfo(models.Model):
    fullname = models.CharField(max_length=250, null=True, blank=False)
    email = models.EmailField(max_length=250, null=True, blank=False)
    message = models.TextField(blank=False)

    def __str__(self) -> str:
        return self.fullname
