 
from django import urls
from  django.urls import reverse,resolve
from django.test import SimpleTestCase,TestCase
from school.views import adminclick_view, home_view,teacherclick_view,studentclick_view,admin_signup_view,teacher_signup_view,student_signup_view,afterlogin_view,admin_dashboard_view,admin_teacher_view
 
# Create your tests here.

class TestUrls(SimpleTestCase):
    def test_case_home_view_urls(self):
        url=reverse('home')
        self.assertEquals(resolve(url).func,home_view)
        
    def test_case_adminclick_view_urls(self):
        url=reverse('adminclick')
        self.assertEquals(resolve(url).func,adminclick_view)
    
    def test_case_teacherclick_view_urls(self):
        url=reverse('teacherclick')
        self.assertEquals(resolve(url).func,teacherclick_view)
        
    def test_case_studentclick_view_urls(self):
        url=reverse('studentclick')
        self.assertEquals(resolve(url).func,studentclick_view)
        
        
        
      
    def test_case_admin_signup_view_urls(self):
        url=reverse('adminsignup')
        self.assertEquals(resolve(url).func,admin_signup_view)
    
    def test_case_teacher_signup_view_urls(self):
        url=reverse('teachersignup')
        self.assertEquals(resolve(url).func,teacher_signup_view)
        
    def test_case_student_signup_view_urls(self):
        url=reverse('studentsignup')
        self.assertEquals(resolve(url).func,student_signup_view)
        
       
       
       
       
        
        
    def test_case_afterlogin_view_urls(self):
        url=reverse('afterlogin')
        self.assertEquals(resolve(url).func,afterlogin_view)
    
    def test_case_admin_dashboard_view_urls(self):
        url=reverse('admin-dashboard')
        self.assertEquals(resolve(url).func,admin_dashboard_view)
        
    def test_case_admin_teacher_view_urls(self):
        url=reverse('admin-teacher')
        self.assertEquals(resolve(url).func,admin_teacher_view)