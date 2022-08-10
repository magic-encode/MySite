from django.test import TestCase, Client

from myapp.models import GetInfo
from myapp.models import Comments
from myapp.models import AddProject
from myapp.models import ProjectCategory



class ModelsTestCase(TestCase):
    def setUp(self) -> None:
        self.comment = Comments.objects.create(
            name="Abdulla",
            comment="Hello I am Backend developer",
        )
        self.proj_cat = ProjectCategory.objects.create(
            name="Study-Buddy"
        )
        self.my_proj = AddProject.objects.create(
            category=self.proj_cat,
            side="left",
            image="static/images/intro.jpg",
            body="Lorem Ipsum is simply dummy text",
            link="http://www.my-project.com/imagesLoaded"
        )
        
        self.get_in_touch = GetInfo.objects.create(
            fullname="Khalimov Abdulla",
            email="abdulla@gmail.com",
            message="Lorem",
        )
        self.client = Client()
        
    def test_comments_instance(self) -> None:
        """Checks comments created in database."""
        comment = Comments.objects.get(name="Abdulla")
        self.assertEqual(comment.name, "Abdulla")
        self.assertEqual(comment.imageURL,'/media/default.jpeg')
        self.assertEqual(comment.comment, 'Hello I am Backend developer')

    def test_project_instance(self) -> None:
        """Checks project instance in database."""
        category = ProjectCategory.objects.get(name='Study-Buddy')
        self.assertEquals(category.name, 'Study-Buddy')
    
    def test_my_project_instance(self) -> None:
        """Checks my projects instance in database."""
        my_proj = AddProject.objects.get(
            category=self.proj_cat, side="left", link="http://www.my-project.com/imagesLoaded"
        )
        self.assertEquals(my_proj.image, 'static/images/intro.jpg')
        self.assertEquals(my_proj.body, 'Lorem Ipsum is simply dummy text')
    
        
    def test_get_in_touch_instance(self) -> None:
        """Checks my touch instance in database."""
        ticket = GetInfo.objects.get(
            email="abdulla@gmail.com"
        )
        self.assertEquals(ticket.fullname, 'Khalimov Abdulla')
        self.assertEquals(ticket.message, "Lorem")