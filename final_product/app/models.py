from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth import get_user_model
from django.conf import settings
from django.utils import timezone
from datetime import time
from ckeditor_uploader.fields import RichTextUploadingField
from django.contrib.auth.models import User
from django.urls import reverse
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.exceptions import ValidationError
from django.templatetags.static import static

class CustomeUser(AbstractUser):
    email = models.EmailField(unique=True)
    user_type_choices = ((1, 'ADMIN'),
                         (2, 'STUDENT'),
                         (3, 'COURSE PROVIDER'))
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    ]
    user_type = models.IntegerField(choices=user_type_choices, default=1)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']
    phone_number = models.CharField(max_length=15, null=True, blank=True)
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES, default='M')
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.email


class Student(models.Model):
    user = models.OneToOneField(CustomeUser, on_delete=models.CASCADE)
    Full_Name = models.CharField(max_length=20, null=True, blank=True)
    Mobile_no = models.CharField(max_length=10, null=True, blank=True)
    EmailID = models.EmailField(max_length=255, null=True, blank=True)
    DOB = models.DateField(null=True, blank=True)
    Gender_choices = (
        ('M', 'Male'),
        ('F', 'Female'),
       ('O', 'Others')
     )
    Gender = models.CharField(max_length=10, choices=Gender_choices, default='M')
    cart = models.ManyToManyField('Course', related_name='students_in_cart')
    wishlist = models.ManyToManyField('Course', related_name='students_in_wishlist')
    created_at = models.DateTimeField(auto_now_add=True, null=True)  # Add this field
    ongoing_courses = models.ManyToManyField('Course', related_name='ongoing_students')
    completed_courses = models.ManyToManyField('Course', related_name='completed_students')

    def __str__(self) -> str:
        return self.user.email
    

class Course(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    course_name = models.CharField(max_length=255, verbose_name='Course Name')
    name = models.CharField(max_length=255, default='Untitled Course')
    description = models.TextField(default='No description available')
    CATEGORY_CHOICES = [
        ('c1', 'Tech Courses'),
        ('c2', 'Grade 9'),
        ('c3', 'Grade 10'),
        ('c4', 'Grade 11'),
        ('c5', 'Grade 12'),
    ]

    title = models.CharField(max_length=100)
    description = models.TextField()
    what_you_will_learn = models.TextField(null=True, blank=True, verbose_name="What You Will Learn")
    this_course_includes = models.TextField(null=True, blank=True, verbose_name="This Course Includes")
    course_content = models.TextField(null=True, blank=True, verbose_name="Course Content")
    requirement = models.TextField(null=True, blank=True, verbose_name="Requirement")
    instructor = models.CharField(null=True, blank=True, max_length=100, verbose_name="Instructor")
    category_type = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default='c1')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Created At')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Updated At')
    mentor = models.ForeignKey('Admin_Mentor', on_delete=models.SET_NULL, null=True, blank=True)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    category = models.ForeignKey('Admin_CourseCategory', on_delete=models.SET_NULL, null=True, blank=True)
    image = models.ImageField(upload_to='course_images_ad/', null=True, blank=True)
    video = models.FileField(upload_to='course_videos_ad/', null=True, blank=True)
    skills_you_will_gain = models.TextField(default='No details provided')
    is_active = models.BooleanField(default=True)
    provider = models.ForeignKey('Admin_CourseProvider', on_delete=models.CASCADE,
                                 default=1,null=True,blank=True)

    def __str__(self):
        return self.title
    
    def image_url(self):
        if self.image:
            return self.image.url
        return static('default_user.jpeg')


class Week(models.Model):
    course = models.ForeignKey(Course, related_name='weeks', on_delete=models.CASCADE)
    number = models.PositiveIntegerField()
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"Week {self.number}: {self.title}"

class Topic(models.Model):
    week = models.ForeignKey(Week, related_name='topics', on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    video_file = models.FileField(upload_to='staticfiles/topic_videos/', null=True, blank=True)
    video_link = models.URLField(null=True, blank=True)
    watched_by_users = models.ManyToManyField(Student, blank=True)

    def __str__(self):
        return self.title

    def has_video(self):
        return bool(self.video_file or self.video_link)

    def get_video_url(self):
        if self.video_file:
            return self.video_file.url
        elif self.video_link:
            return self.video_link
        else:
            return None



class Quiz(models.Model):
    course = models.ForeignKey(Course, related_name='quizzes', on_delete=models.CASCADE)
    topic = models.ForeignKey(Topic, related_name='quizzes', on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    weight = models.FloatField(default=0)
    description = models.TextField(blank=True, null=True)
    due_date = models.DateTimeField(default=timezone.now)
    time_limit = models.TimeField(default=time(0, 30))
    

    def __str__(self):
        return self.title

class QuizQuestion(models.Model):
    quiz = models.ForeignKey(Quiz, related_name='quiz_questions', on_delete=models.CASCADE)
    question_no = models.IntegerField()
    question_text = models.TextField(max_length=255)
    option1 = models.CharField(max_length=255)
    option2 = models.CharField(max_length=255)
    option3 = models.CharField(max_length=255)
    option4 = models.CharField(max_length=255)
    correct_option = models.CharField(
        max_length=2,
        choices=[
            ('1', 'Option 1'),
            ('2', 'Option 2'),
            ('3', 'Option 3'),
            ('4', 'Option 4')
        ]
    )
    reason = models.TextField()

    def __str__(self):
        return f"{self.quiz.course} - {self.quiz.topic}"


class QuizResult(models.Model):
    student = models.ForeignKey(Student, related_name='quiz_results', on_delete=models.CASCADE)
    quiz = models.ForeignKey(Quiz, related_name='results', on_delete=models.CASCADE)
    score = models.FloatField()
    total_questions = models.IntegerField()
    completed_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.student.user.username} - {self.quiz.title} - {self.score}/{self.total_questions}"

class SelectedAnswer(models.Model):
    student = models.ForeignKey(Student, related_name='selected_answers', on_delete=models.CASCADE)
    quiz = models.ForeignKey(Quiz, related_name='selected_answers', on_delete=models.CASCADE)
    question = models.ForeignKey(QuizQuestion, related_name='selected_answers', on_delete=models.CASCADE)
    selected_option = models.CharField(max_length=2, null=True)

    def __str__(self):
        return f"{self.student.user.username} - {self.quiz.title} - Question {self.question.question_no} - Option {self.selected_option}"

class StudentCourseProgress(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    completed_weeks = models.ManyToManyField(Week, blank=True)


class Certificate(models.Model):
    user = models.ForeignKey(Student, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    completion_date = models.DateTimeField(auto_now_add=True)
    certificate_image = models.ImageField(upload_to='staticfiles/certificates/')

    def __str__(self):
        return f"{self.user.Full_Name}'s Certificate for {self.course.title}"

class Grade(models.Model):
    certificate = models.ForeignKey(Certificate, on_delete=models.CASCADE)
    grade = models.CharField(max_length=2)

    def __str__(self):
        return f"{self.certificate.course} - {self.grade}"


class Enrollment(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='enrollements')
    user = models.ForeignKey(Student, on_delete=models.CASCADE, limit_choices_to={'user__user_type': 2})
    enrollment_date = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return f"{self.user.user} enrolled in {self.course.title}"

'''
class Ticket(models.Model):
    REASON_CHOICES = [
        ('Payment Methods', 'Payment Methods'),
        ('Refund a Course', 'Refund a Course'),
        ('Troubleshoot Payment Failure', 'Troubleshoot Payment Failure'),
        ('Download Course Resources', 'Download Course Resources'),
        ('Enrollment', 'Enrollment'),
        ('Grades & Assignments', 'Grades & Assignments'),
        ('Video Library', 'Video Library'),
        ('Trust & Safety', 'Trust & Safety'),
        ('Find a missing course', 'Find a missing course'),
        ('Other', 'Other'),
    ]
    STATUS_CHOICES = [
        ('open', 'Open'),
        ('closed', 'Closed'),
    ]

    user = models.ForeignKey(CustomeUser, related_name='tickets', on_delete=models.CASCADE)
    category = models.ForeignKey(Admin_Category, on_delete=models.SET_NULL, null=True)
    subcategory = models.ForeignKey(Admin_Subcategory, on_delete=models.SET_NULL, null=True)
    reason = models.TextField(max_length=500, choices=REASON_CHOICES)
    description = models.TextField()
    attachment = models.FileField(upload_to='tickets/', null=True, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='open')

    def __str__(self):
        return f"Ticket #{self.id} - {self.user.email}"
    
    def __str__(self):
        return f"Ticket {self.unique_id} by {self.user.username}"

    def save(self, *args, **kwargs):
        if not self.unique_id:
            self.unique_id = self.generate_unique_id()
        super(Admin_Ticket, self).save(*args, **kwargs)

    def generate_unique_id(self):
        return str(uuid.uuid4())
'''

class Profile(models.Model):
    user = models.OneToOneField(get_user_model(), on_delete=models.CASCADE)
    bio = models.TextField(blank=True)
    profile_picture = models.ImageField(upload_to='staticfiles/profile_pics/', blank=True)
    mobile_number = models.CharField(max_length=15, blank=True)
    language = models.CharField(max_length=50, blank=True)
    linkedin_profile = models.URLField(blank=True)
    twitter_profile = models.URLField(blank=True)
    facebook_profile = models.URLField(blank=True)

    def __str__(self):
        return f"Profile of {self.user.username}"

class WorkExperience(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    company_name = models.CharField(max_length=255)
    position = models.CharField(max_length=255)
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)
    description = models.TextField()


class Mentorship(models.Model):
    user = models.ForeignKey(Student, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=100, null=True)
    email = models.EmailField(null=True)
    reason = models.TextField()
    phone_number = models.CharField(max_length=15)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='mentorship_request')  # Assuming each mentorship is associated with a course
    timestamp = models.DateTimeField(auto_now_add=True)
    status = models.CharField(
        max_length=20,
        choices=[('Pending', 'Pending'), ('Accepted', 'Accepted'), ('Rejected', 'Rejected')],
        default='Pending'
    )  # Add mentorship status

    def __str__(self):
        return f"Mentorship for {self.user.username}"

class Education(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    institution_name = models.CharField(max_length=255)
    degree = models.CharField(max_length=255)
    field_of_study = models.CharField(max_length=255)
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)

class Project(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)
    url = models.URLField(null=True, blank=True)


class PrivacySettings(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    show_profile_to_logged_in_users = models.BooleanField(default=True)
    show_courses_on_profile = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.user.username}'s Privacy Settings"

class NotificationSettings(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    promotion = models.BooleanField(default=True)
    helpful_resources = models.BooleanField(default=True)
    no_promotional_email = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.user.username}'s Notification Settings"

class Referral(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    friend_email = models.EmailField()
    date_referred = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} referred {self.friend_email}"


class PaymentHistory(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    course_title = models.CharField(max_length=255)
    date = models.DateTimeField(auto_now_add=True)
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    payment_type = models.CharField(max_length=50)
    receipt_invoice = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.user.username} - {self.course_title} - {self.date}"


class Note(models.Model):
    course = models.ForeignKey(Course, related_name='notes', on_delete=models.CASCADE)
    student = models.ForeignKey(Student, related_name='notes', on_delete=models.CASCADE, null=True, blank=True)
    content = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"Note by {self.student.user.email} on {self.course.title}"


class Message(models.Model):
    course = models.ForeignKey(Course, related_name='messages', on_delete=models.CASCADE, null=True, blank=True)
    content = models.TextField()

    def __str__(self):
        return f"Message for {self.course.title}"

class CareerGuidanceMessage(models.Model):
    course = models.ForeignKey(Course, related_name='guidance_messages', on_delete=models.CASCADE, null=True, blank=True)
    content = RichTextUploadingField()

    def __str__(self):
        return f"Career Guidance for {self.course.title if self.course else 'No Course'}"


class Resource(models.Model):
    week = models.ForeignKey(Week, related_name='resources', on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    pdf_file = models.FileField(upload_to='staticfiles/week_resources/', null=True, blank=True)

    def __str__(self):
        return f"Resource '{self.title}' for Week {self.week.number}"




class QuestionPaper(models.Model):
    title = models.CharField(max_length=200)
    year = models.IntegerField()
    subject = models.CharField(max_length=100)
    file = models.FileField(upload_to='question_papers/')
    course = models.ForeignKey(Course, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

class BlogPost(models.Model):
    ART = "Art & Design"
    BUSINESS = "Business"
    DS = "Data Science"
    DEV = "Development"
    FINANCE = "Finance"
    HF = "Health & Fitness"
    LS = "Lifestyle"
    CATEGORY_CHOICES = [
        (ART, 'Art & Design'),
        (BUSINESS, 'Business'),
        (DS, 'Data Science'),
        (DEV, 'Development'),
        (FINANCE, 'Finance'),
        (HF, 'Health & Fitness'),
        (LS, 'Lifestyle'),
    ]
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='blog_posts')
    title = models.CharField(max_length=200)
    content = models.TextField()
    category = models.CharField(max_length=100, choices=CATEGORY_CHOICES, default=DEV)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    published_at = models.DateTimeField(default=timezone.now)
    tags = models.CharField(max_length=100, blank=True, null=True)
    trending = models.BooleanField(default=False)
    thumbnail = models.ImageField(upload_to='admin_thumbnails/', blank=True)
    cover_pic = models.ImageField(upload_to='admin_covers/', blank=True)
    related_courses = models.ManyToManyField(Course)

    def __str__(self):
        return self.title


class BlogComment(models.Model):
    post = models.ForeignKey(BlogPost, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='blog_comments')
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Comment by {self.author} on {self.post}"


class Discussion(models.Model):
    course = models.ForeignKey(Course, related_name='discussions', on_delete=models.CASCADE)
    title = models.CharField(max_length=200, null=True, blank=True)
    user = models.ForeignKey(get_user_model(), related_name='discussions', on_delete=models.CASCADE, null=True,
                             blank=True)  # Added user field
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)




class Post(models.Model):
    user = models.ForeignKey(Student, on_delete=models.CASCADE, null=True, blank=True)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    likes = models.IntegerField(default=0)
    dislikes = models.IntegerField(default=0)


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(Student, on_delete=models.CASCADE, null=True, blank=True)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    likes = models.IntegerField(default=0)
    dislikes = models.IntegerField(default=0)

class WeekPost(models.Model):
    user = models.ForeignKey(Student, on_delete=models.CASCADE, null=True, blank=True)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    likes = models.IntegerField(default=0)
    dislikes = models.IntegerField(default=0)
    week_number = models.IntegerField(Week, null=True, blank=True)


class WeekComment(models.Model):
    week_post = models.ForeignKey(WeekPost, on_delete=models.CASCADE)
    user = models.ForeignKey(Student, on_delete=models.CASCADE, null=True, blank=True)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    likes = models.IntegerField(default=0)
    dislikes = models.IntegerField(default=0)


class MentorshipRequest(models.Model):
    user = models.ForeignKey(get_user_model(), related_name='mentorship_requests', on_delete=models.CASCADE)
    course = models.ForeignKey(Course, related_name='mentorship_requests', on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    reason = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.email} - Course: {self.course.title}"


class ChatMessage(models.Model):
    user = models.ForeignKey(Student, on_delete=models.CASCADE, null=True, blank=True)
    message = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    is_admin = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.user.user} ({'Admin' if self.is_admin else 'User'}): {self.message[:50]}"

class Bundle(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
    courses = models.ManyToManyField(Course, related_name='bundles')
    image = models.ImageField(upload_to='staticfiles/bundle_images/', null=True, blank=True)
    note = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.title
    

######################################################################################################################################
#-------------------------------------------------------------------------------------------------------------------------------------
#COURSE PROVIDER MODELS
#-------------------------------------------------------------------------------------------------------------------------------------
######################################################################################################################################


class CourseByProvider(models.Model):
    code = models.CharField(max_length=100, unique=True)
    title = models.CharField(max_length=200)
    description = models.TextField()
    category = models.CharField(max_length=100, choices=(
        ('programming', 'Programming'),
        ('design', 'Design'),
        ('marketing', 'Marketing'),
        ('business', 'Business'),
        # Add more categories as needed
    ))
    duration = models.IntegerField()  # Duration in hours
    level = models.CharField(max_length=100, choices=(
        ('beginner', 'Beginner'),
        ('intermediate', 'Intermediate'),
        ('advanced', 'Advanced'),
    ))
    price = models.IntegerField(default=0)
    image = models.ImageField(upload_to='course_images_by_provider/')
    # video = models.FileField(upload_to='course_videos/')
    created_at = models.DateTimeField(auto_now_add=True)
    students = models.ManyToManyField('Student', related_name='courses', blank=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('course_detail', kwargs={'pk': self.pk})

class CourseVideoByProvider(models.Model):
    course = models.ForeignKey(CourseByProvider, related_name='videos', on_delete=models.CASCADE)
    video = models.FileField(upload_to='course_videos_by_provider/')

class MaterialByProvider(models.Model):
    course = models.ForeignKey(CourseByProvider, related_name='materials', on_delete=models.CASCADE)
    file = models.FileField(upload_to='course_materials_by_provider/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

class QuizByProvider(models.Model):
    title = models.CharField(max_length=100, default="Title")
    total_score = models.IntegerField(default=10)
    course = models.ForeignKey(CourseByProvider, related_name='quizzes', on_delete=models.CASCADE)
    file = models.FileField(upload_to='course_quizzes_by_provider/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class AssignmentByProvider(models.Model):
    title = models.CharField(max_length=100, default="Title")
    total_score = models.IntegerField(default=100)
    course = models.ForeignKey(CourseByProvider, related_name='assignments', on_delete=models.CASCADE)
    file = models.FileField(upload_to='course_assignments_by_provider/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

'''
class StudentByProvider(models.Model):
    name = models.CharField(max_length=100, default="abc")

    def __str__(self):
        return self.name
'''

class ResultByProvider(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    quiz = models.ForeignKey(QuizByProvider, on_delete=models.CASCADE)
    score = models.IntegerField()

    def __str__(self):
        return f'{self.student.name} - {self.quiz.title} - {self.score}'

class AssignmentResultByProvider(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    assignment = models.ForeignKey(AssignmentByProvider, on_delete=models.CASCADE)
    score = models.IntegerField()
    comment = models.TextField(blank=True)

    def __str__(self):
        return f'{self.student.name} - {self.assignment.title} - {self.score}'

class PayoutStatementByProvider(models.Model):
    payment_details = models.CharField(max_length=200)
    image = models.ImageField(upload_to='payout_images_by_provider/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.payment_details




######################################################################################################################################
#-------------------------------------------------------------------------------------------------------------------------------------
#ADMIN MODELS
#-------------------------------------------------------------------------------------------------------------------------------------
######################################################################################################################################





from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission
from django.conf import settings
from django.db import models
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _
from django.conf import settings
from django.db import models
from django.conf import settings
from django.utils import timezone
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
from django.db import models
from django.urls import reverse
import uuid
from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User


# Create your models here.
'''
class Admin_CustomeUser(AbstractUser):
    email = models.EmailField(unique=True)
    user_type_choices = ((1, 'ADMIN'),
                         (2, 'STUDENT'),
                         (3, 'COURSE PROVIDER'))
    user_type = models.IntegerField(choices=user_type_choices, default=1)

    is_active = models.BooleanField(default=True)  # Attribute to represent if the account is active or suspended

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    ]

    phone_number = models.CharField(max_length=15, null=True, blank=True)
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES, default='M')

    def __str__(self):
        return self.email
'''

class Admin_Admin(models.Model):
    user = models.OneToOneField(CustomeUser, on_delete=models.CASCADE)
    Full_Name = models.CharField(max_length=20)
    Mobile_no = models.CharField(max_length=10)
    EmailID = models.EmailField(max_length=255)
    DOB = models.DateField(null=True, blank=True)
    Gender_choices = (
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Others')
    )
    Gender = models.CharField(max_length=10, choices=Gender_choices, default='M')

    def __str__(self) -> str:
        return self.Full_Name


# Model for Mentor
class Admin_Mentor(models.Model):
    name = models.CharField(max_length=255)
    bio = models.TextField(blank=True)

    def __str__(self):
        return self.name


# Model for CourseCategory
class Admin_CourseCategory(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name

'''
# Model for Course
class Admin_Course(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    course_name = models.CharField(max_length=255, verbose_name='Course Name')
    name = models.CharField(max_length=255, default='Untitled Course')
    description = models.TextField(default='No description available')
    CATEGORY_CHOICES = [
        ('c1', 'Tech Courses'),
        ('c2', 'Grade 9'),
        ('c3', 'Grade 10'),
        ('c4', 'Grade 11'),
        ('c5', 'Grade 12'),
    ]
    price = models.DecimalField(max_digits=8, decimal_places=2)
    image = models.ImageField(upload_to='admin_course_images/', null=True, blank=True)
    video = models.FileField(upload_to='admin_course_videos/', null=True, blank=True)
    category_type = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default='c1')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Created At')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Updated At')
    mentor = models.ForeignKey('Admin_Mentor', on_delete=models.SET_NULL, null=True, blank=True)
    category = models.ForeignKey('Admin_CourseCategory', on_delete=models.SET_NULL, null=True, blank=True)
    what_you_will_learn = models.TextField(default='No details provided')
    skills_you_will_gain = models.TextField(default='No details provided')
    is_active = models.BooleanField(default=True)
    provider = models.ForeignKey('Admin_CourseProvider', on_delete=models.CASCADE,
                                 default=1,null=True,blank=True)  # Update the default value to the ID of the created provider

    def __str__(self):
        return self.course_name


# links students to courses
class Admin_Enrollement(models.Model):
    student = models.ForeignKey(CustomeUser, on_delete=models.CASCADE, limit_choices_to={'user_type': 2})
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='enrollements')  # Changed related_name
    enrollment_date = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return f"{self.student.email} enrolled in {self.course.course_name}"
'''

# To track course purchase by students
class Admin_Order(models.Model):
    student = models.ForeignKey(CustomeUser, on_delete=models.CASCADE, limit_choices_to={'user_type': 2})
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Order {self.id} by {self.student.username} for {self.course.name}"


# Model for Assignment Content
class Admin_Assignment(models.Model):
    title = models.CharField(max_length=100, verbose_name='Assignment Title')
    course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name='Course')
    description = models.TextField(verbose_name='Description')
    due_date = models.DateTimeField(verbose_name='Due Date')

    def __str__(self):
        return self.title


class Admin_StudentAssignment(models.Model):
    assignment = models.ForeignKey(Admin_Assignment, on_delete=models.CASCADE)
    student = models.ForeignKey(CustomeUser, on_delete=models.CASCADE)
    submission = models.FileField(upload_to='admin_assignment_submissions/')
    marked = models.BooleanField(default=False)


class Admin_AssignmentFeedback(models.Model):
    assignment = models.ForeignKey(Admin_Assignment, on_delete=models.CASCADE)
    student = models.ForeignKey(CustomeUser, on_delete=models.CASCADE)
    feedback = models.TextField()
    marks = models.FloatField()


## Model for Quiz Content
class Admin_Quiz(models.Model):
    title = models.CharField(max_length=100)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    description = models.TextField()
    number_of_questions = models.IntegerField(default=10)
    time_limit_hours = models.IntegerField(default=1)

    def __str__(self):
        return self.title


class Admin_Question(models.Model):
    quiz = models.ForeignKey(Admin_Quiz, on_delete=models.CASCADE)
    question_text = models.CharField(max_length=255)

    # Add other fields for question details

    def __str__(self):
        return self.question_text


class Admin_Choice(models.Model):
    question = models.ForeignKey(Admin_Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=255)
    is_correct = models.BooleanField(default=False)

    # Add other fields for choice details

    def __str__(self):
        return self.choice_text


class Admin_Answer(models.Model):
    question = models.ForeignKey(Admin_Question, on_delete=models.CASCADE)
    user = models.ForeignKey(CustomeUser, on_delete=models.CASCADE)
    choice = models.ForeignKey(Admin_Choice, on_delete=models.CASCADE)

    def __str__(self):
        return f"Answer for Question: {self.question.question_text} by {self.user.username}"


class Admin_Quiz_Result(models.Model):
    quiz = models.ForeignKey(Admin_Quiz, on_delete=models.CASCADE)
    student = models.ForeignKey(CustomeUser, on_delete=models.CASCADE)
    score = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return f"{self.quiz.title} - {self.student.username} Result"


class Admin_Voucher(models.Model):
    student = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, default=1)

    code = models.CharField(max_length=100, unique=True, help_text="Unique code for the voucher")
    discount = models.DecimalField(max_digits=10, decimal_places=2,
                                   help_text="Discount value (percentage or flat amount)")
    expiration_date = models.DateField(help_text="Expiration date of the voucher", null=True,
                                       blank=True)  # Make this field optional
    start_date = models.DateField(help_text="Start date of the voucher", null=True, blank=True)
    end_date = models.DateField(help_text="End date of the voucher", null=True, blank=True)
    min_amount = models.DecimalField(max_digits=10, decimal_places=2,
                                     help_text="Minimum amount for the voucher to be applicable", null=True, blank=True)
    num_courses = models.PositiveIntegerField(help_text="Number of courses required for the voucher to be applicable",
                                              null=True, blank=True)
    courses = models.ManyToManyField('Course', help_text="Courses that this voucher applies to", blank=True)
    discount_type_choices = [
        ('flat', 'Flat amount'),
        ('percentage', 'Percentage with limit'),
    ]
    discount_type = models.CharField(max_length=20, choices=discount_type_choices, default='flat')
    discount_limit = models.DecimalField(max_digits=10, decimal_places=2,
                                         help_text="Maximum discount limit (for percentage discounts)", null=True,
                                         blank=True)

    used_count = models.PositiveIntegerField(default=0, help_text="Number of times the voucher has been used")
    is_active = models.BooleanField(default=True, help_text="Whether the voucher is currently active")

    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='vouchers',
                                   help_text="User who created the voucher")
    created_at = models.DateTimeField(auto_now_add=True, help_text="Creation timestamp")
    updated_at = models.DateTimeField(auto_now=True, help_text="Last updated timestamp")

    def __str__(self):
        return f"{self.code} - {self.discount} {'%' if self.discount_type == 'percentage' else ''} off"

    class Meta:
        ordering = ['-created_at']
        verbose_name = "Voucher"
        verbose_name_plural = "Vouchers"


class Admin_AffiliateMarketer(models.Model):
    email = models.EmailField(unique=True)
    name = models.CharField(max_length=100)
    student = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, default=1)
    commission_percentage = models.DecimalField(max_digits=5, decimal_places=2, default=0.0)
    is_frozen = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class Admin_EnrolledUser(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    marketer = models.ForeignKey(Admin_AffiliateMarketer, related_name='enrolled_users', on_delete=models.CASCADE)
    enrollment_date = models.DateTimeField(null=True, blank=True)  # Temporarily make it nullable


class Admin_Sale(models.Model):
    sale_amount = models.DecimalField(max_digits=10, decimal_places=2)
    marketer = models.ForeignKey(Admin_AffiliateMarketer, related_name='sales', on_delete=models.CASCADE)
    enrolled_user = models.ForeignKey(Admin_EnrolledUser, related_name='sales', on_delete=models.CASCADE)
    invoice_id = models.CharField(max_length=100, unique=True, blank=True, null=True)  # Add this
    sale_date = models.DateTimeField(null=True, blank=True)  # Temporarily allow null values


class Admin_AffiliateAccount(models.Model):
    marketer = models.OneToOneField(Admin_AffiliateMarketer, on_delete=models.CASCADE)
    # Add additional fields for account details


from django.db import models
from django.utils.translation import gettext_lazy as _


class Admin_CourseProvider(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='course_provider')
    first_name = models.CharField(max_length=100, default='')  # Added default here
    last_name = models.CharField(max_length=100, default='')  # Added default here
    email = models.EmailField(default='')  # Added default here
    phone_number = models.CharField(max_length=15, default='')  # Added default here
    gender = models.CharField(max_length=10, choices=[('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other')],
                              default='')  # Added default here
    account_name = models.CharField(max_length=100, default='')  # Added default here
    bank_name = models.CharField(max_length=100, default='')  # Added default here
    account_type = models.CharField(max_length=50, default='')  # Added default here
    account_number = models.CharField(max_length=50, default='')  # Added default here
    ifsc_code = models.CharField(max_length=20, default='')  # Added default here
    courses = models.ManyToManyField(Course)  # Many-to-many relationship with Course

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Admin_CourseProviderCourse(models.Model):
    course_provider = models.ForeignKey(Admin_CourseProvider, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.course_provider.full_name} - {self.course.course_name}'


class Admin_PayoutDetail(models.Model):
    course_provider = models.ForeignKey(Admin_CourseProvider, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='payout_details', blank=True, null=True)  # Ensure this exists
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    payout_date = models.DateField()
    payout_method = models.CharField(max_length=50)
    transaction_id = models.CharField(max_length=100, blank=True, null=True)

    # Add payment_status if needed
    payment_status = models.CharField(
        max_length=20,
        choices=[('pending', 'Pending'), ('completed', 'Completed')],
        default='pending'
    )

    def __str__(self):
        return f"Payout for {self.course_provider} - {self.amount} on {self.payout_date}"

class Admin_PayoutBill(models.Model):
    payout_detail = models.ForeignKey(Admin_PayoutDetail, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='payout_bills/')
    bill_date = models.DateField(_('Bill Date'))
    description = models.TextField(_('Description'))

    def __str__(self):
        return f"Payout Bill for {self.payout_detail} ({self.bill_date})"


class Admin_CourseOwnerEarnings(models.Model):
    course_provider = models.ForeignKey(Admin_CourseProvider, on_delete=models.CASCADE)
    total_earnings = models.DecimalField(max_digits=10, decimal_places=2, verbose_name=_('Total Earnings'))
    previous_month_earnings = models.DecimalField(max_digits=10, decimal_places=2,
                                                  verbose_name=_('Previous Month Earnings'))

    # Add other fields like custom date range earnings, etc.

    def __str__(self):
        return f"Earnings of {self.course_provider.user.username}"

'''
class Admin_Student(models.Model):
    user = models.OneToOneField(CustomeUser, on_delete=models.CASCADE)
    Full_Name = models.CharField(max_length=20, null=True, blank=True)
    Mobile_no = models.CharField(max_length=10, null=True, blank=True)
    EmailID = models.EmailField(max_length=255, null=True, blank=True)
    DOB = models.DateField(null=True, blank=True)
    Gender_choices = (
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Others')
    )
    Gender = models.CharField(max_length=10, choices=Gender_choices, default='M')
    cart = models.ManyToManyField('Course', related_name='students_in_cart')
    wishlist = models.ManyToManyField('Course', related_name='students_in_wishlist')
    created_at = models.DateTimeField(auto_now_add=True, null=True)  # Add this field
    ongoing_courses = models.ManyToManyField('Course', related_name='ongoing_students')
    completed_courses = models.ManyToManyField('Course', related_name='completed_students')

    def __str__(self) -> str:
        return self.Full_Name
'''

class Admin_Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Admin_Blog(models.Model):
    title = models.CharField(max_length=200)
    thumbnail = models.ImageField(upload_to='admin_thumbnails/')
    cover_pic = models.ImageField(upload_to='admin_covers/')
    content = models.TextField()
    tags = models.CharField(max_length=200)  # Can be a many-to-many field for advanced use
    category = models.ForeignKey(Admin_Category, on_delete=models.SET_NULL, null=True)
    trending = models.BooleanField(default=False)
    related_courses = models.ManyToManyField(Course)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class Admin_AboutUs(models.Model):
    who_we_are = RichTextField(default='About Us content here.')
    our_vision = RichTextField(default='Our vision content here.')
    our_mission = RichTextField(default='Our mission content here.')
    our_values = RichTextField(default='Our values content here.')
    meet_the_team = RichTextField(default='Meet the team content here.')
    our_story = RichTextField(default='Our story content here.')

    def __str__(self):
        return "About Us"


class Admin_ClickTracking(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.course.course_name}"


class Admin_ReferralProgram(models.Model):
    partner_name = models.CharField(max_length=200)
    email = models.EmailField()
    code = models.CharField(max_length=20, default='DEFAULT_CODE')  # Add default value
    referral_count = models.PositiveIntegerField(default=0)
    total_bonus_earned = models.PositiveIntegerField(default=0)


    def __str__(self):
        return self.partner_name


class Admin_ReferralLink(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    referral_link = models.CharField(max_length=255, unique=True,
                                     default=uuid.uuid4().hex)  # Generate a unique default value
    is_active = models.BooleanField(default=False)
    enrollments_count = models.PositiveIntegerField(default=0)
    bonus_coins = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"Referral Link for {self.user.username}"

    def activate(self):
        self.is_active = True
        self.save()

    def get_share_link(self):
        return reverse('enroll_via_referral', kwargs={'referral_link': self.referral_link})


class Admin_Settings(models.Model):
    coins_per_enrollment = models.PositiveIntegerField(default=250)
    conversion_rate = models.DecimalField(max_digits=5, decimal_places=2, default=25.0)

    def __str__(self):
        return "Settings"


class Admin_Enrollment(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='enrollments')
    course = models.ForeignKey(Course, on_delete=models.CASCADE,
                               related_name='course_enrollments')  # Changed related_name
    enrollment_date = models.DateTimeField(auto_now_add=True)
    is_completed = models.BooleanField(default=False)
    referral = models.ForeignKey('Admin_Referral', on_delete=models.SET_NULL, null=True, blank=True)
    affiliate = models.ForeignKey('Admin_AffiliateMarketer', on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f"{self.student.user.username} enrolled in {self.course.course_name}"


def redeem_coins_submit(request):
    if request.method == 'POST':
        coins_to_redeem = int(request.POST.get('coins', 0))  # Get coins from form, default to 0 if not provided

        # Retrieve current redeemable coins from session
        redeemable_coins = request.session.get('redeemable_coins', 0)

        if coins_to_redeem <= 0:
            return HttpResponse('Please enter a valid number of coins.')

        if coins_to_redeem > redeemable_coins:
            return HttpResponse('Not enough redeemable coins.')

        # Deduct coins from redeemable_coins session
        request.session['redeemable_coins'] -= coins_to_redeem

        # Return success message
        return HttpResponse(f'{coins_to_redeem} coins redeemed successfully.')

    # Initialize redeemable coins in session if not already set
    if 'redeemable_coins' not in request.session:
        request.session['redeemable_coins'] = 1000  # Example initial value

    # Render the redeem_coins.html template with current redeemable coins
    return render(request, 'redeem_coins.html', {'redeemable_coins': request.session['redeemable_coins']})


class Admin_RedeemableCoins(models.Model):
    coins = models.IntegerField(default=0)

    def __str__(self):
        return f'Redeemable Coins: {self.coins}'


class Admin_Subcategory(models.Model):
    name = models.CharField(max_length=100)
    category = models.ForeignKey(Admin_Category, related_name='subcategories', on_delete=models.CASCADE)

    def __str__(self):
        return self.name

'''
class Admin_Ticket(models.Model):
    STATUS_CHOICES = [
        ('open', 'Open'),
        ('closed', 'Closed'),
    ]

    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='tickets', on_delete=models.CASCADE)
    category = models.ForeignKey(Admin_Category, on_delete=models.SET_NULL, null=True)
    subcategory = models.ForeignKey(Admin_Subcategory, on_delete=models.SET_NULL, null=True)
    reason = models.TextField()
    unique_id = models.CharField(max_length=100, unique=True, editable=False)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='open')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Ticket {self.unique_id} by {self.user.username}"

    def save(self, *args, **kwargs):
        if not self.unique_id:
            self.unique_id = self.generate_unique_id()
        super(Admin_Ticket, self).save(*args, **kwargs)

    def generate_unique_id(self):
        return str(uuid.uuid4())
'''
class Ticket(models.Model):
    REASON_CHOICES = [
        ('Payment Methods', 'Payment Methods'),
        ('Refund a Course', 'Refund a Course'),
        ('Troubleshoot Payment Failure', 'Troubleshoot Payment Failure'),
        ('Download Course Resources', 'Download Course Resources'),
        ('Enrollment', 'Enrollment'),
        ('Grades & Assignments', 'Grades & Assignments'),
        ('Video Library', 'Video Library'),
        ('Trust & Safety', 'Trust & Safety'),
        ('Find a missing course', 'Find a missing course'),
        ('Other', 'Other'),
    ]
    STATUS_CHOICES = [
        ('open', 'Open'),
        ('closed', 'Closed'),
    ]

    user = models.ForeignKey(CustomeUser, related_name='tickets', on_delete=models.CASCADE)
    category = models.ForeignKey(Admin_Category, on_delete=models.SET_NULL, null=True, blank=True)
    subcategory = models.ForeignKey(Admin_Subcategory, on_delete=models.SET_NULL, null=True, blank=True)
    reason = models.TextField(max_length=500, choices=REASON_CHOICES)
    description = models.TextField()
    attachment = models.FileField(upload_to='tickets/', null=True, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='open')
    unique_id = models.CharField(max_length=36, unique=True, blank=True, editable=False) #Added  this line
    
    def __str__(self):
        return f"Ticket {self.unique_id} by {self.user.email}"

    def save(self, *args, **kwargs):
        if not self.unique_id:
            self.unique_id = self.generate_unique_id()
        super(Ticket, self).save(*args, **kwargs)

    def generate_unique_id(self):
        return str(uuid.uuid4())
    

class Admin_ChatMessage(models.Model):
    ticket = models.ForeignKey(Ticket, related_name='chat_messages', on_delete=models.CASCADE)
    sender = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='sent_messages', on_delete=models.CASCADE)
    message = models.TextField(blank=True)
    attachment = models.FileField(upload_to='attachments/', blank=True, null=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Message by {self.sender.username} in Ticket {self.ticket.unique_id}"


# Model for Feedback Forms
class Admin_FormFeedback(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.title


# Model for Feedback Questions
class Admin_FeedbackQuestion(models.Model):
    TEXT = 'text'
    MULTIPLE_CHOICE = 'choice'

    QUESTION_TYPES = [
        (TEXT, 'Text'),
        (MULTIPLE_CHOICE, 'Multiple Choice'),
    ]

    form = models.ForeignKey(Admin_FormFeedback, on_delete=models.CASCADE, related_name='questions')
    question_type = models.CharField(max_length=20, choices=QUESTION_TYPES, default=TEXT)
    text = models.TextField()

    def __str__(self):
        return self.text


# Model for Multiple Choice Options
class Admin_MultipleChoiceOption(models.Model):
    question = models.ForeignKey(Admin_FeedbackQuestion, on_delete=models.CASCADE, related_name='options')
    option_text = models.CharField(max_length=200)
    is_correct = models.BooleanField(default=False)

    def __str__(self):
        return self.option_text


# Model for Responses to Feedback Forms
class Admin_FeedbackResponse(models.Model):
    form = models.ForeignKey(Admin_FormFeedback, on_delete=models.CASCADE, related_name='responses')
    respondent = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Response by {self.respondent.username} on {self.submitted_at}"


# Model for Answers to Questions
class Admin_FeedbackAnswer(models.Model):
    response = models.ForeignKey(Admin_FeedbackResponse, on_delete=models.CASCADE, related_name='answers')
    question = models.ForeignKey(Admin_FeedbackQuestion, on_delete=models.CASCADE)
    text_answer = models.TextField(blank=True, null=True)
    choice_answer = models.ForeignKey(Admin_MultipleChoiceOption, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return f"Answer to '{self.question.text}'"


# Model for linking Feedback Forms to Courses
class Admin_CourseFeedbackLink(models.Model):
    feedback_form = models.ForeignKey(Admin_FormFeedback, on_delete=models.CASCADE)
    course_id = models.CharField(max_length=100)  # Example: Could be the course ID or slug

    def __str__(self):
        return f"Feedback form '{self.feedback_form.title}' linked to Course ID: {self.course_id}"


################################################################################################################################################################################################################
# User Management


class Admin_Referral(models.Model):
    referrer = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='referrals_made')
    referred_student = models.OneToOneField(Student, on_delete=models.CASCADE, related_name='referred_by')
    total_bonus_earned = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    def __str__(self):
        return f"{self.referrer.user.username} referred {self.referred_student.user.username}"


class Admin_Cart(models.Model):
    student = models.OneToOneField(Student, on_delete=models.CASCADE, related_name='cart_instance')
    courses = models.ManyToManyField(Course, related_name='carts')

    def __str__(self):
        return f"{self.student.user.username}'s Cart"


class Admin_BulkCourse(models.Model):
    title = models.CharField(max_length=50)
    common_description = models.TextField(max_length=200)
    courses = models.ManyToManyField(Course, related_name='bulk_courses')
    amount = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.title


################################################################################################################################################################################################################
# Content Management

# Model for Week
'''
class Admin_Week(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='weeks')
    title = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return f"{self.title} - {self.course.course_name}"
'''

# Model for Module
class Admin_Module(models.Model):
    week = models.ForeignKey(Week, on_delete=models.CASCADE, related_name='modules')
    name = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.name} - {self.week.title}"


# Abstract Base Model for Content
class Admin_Content(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()

    class Meta:
        abstract = True


# Model for Article Content
class Admin_Article(Admin_Content):
    module = models.ForeignKey(Admin_Module, on_delete=models.CASCADE, related_name='articles')

    def __str__(self):
        return f"Article - {self.title}"


# Model for Video Content
class Admin_Video(Admin_Content):
    module = models.ForeignKey(Admin_Module, on_delete=models.CASCADE, related_name='videos')
    video_file = models.FileField(upload_to='videos/', blank=True)

    def __str__(self):
        return f"Video - {self.title}"


# Model for Message (Optional Feature)
class Admin_Message(models.Model):
    course = models.OneToOneField(Course, on_delete=models.CASCADE, related_name='message', blank=True, null=True)
    content = models.TextField()

    def __str__(self):
        return f"Message for {self.course.course_name}" if self.course else "General Message"


# Model for Resource (Optional Feature)
class Admin_Resource(models.Model):
    week = models.OneToOneField(Week, on_delete=models.CASCADE, related_name='resource', blank=True, null=True)
    content = models.TextField()

    def __str__(self):
        return f"Resource for {self.week.title}" if self.week else "General Resource"


# Model for Career Guidance (Optional Feature)
class Admin_CareerGuidance(models.Model):
    course = models.OneToOneField(Course, on_delete=models.CASCADE, related_name='career_guidance', blank=True,
                                  null=True)
    description = models.TextField()
    image = models.ImageField(upload_to='career_guidance/', blank=True, null=True)
    related_blogs = models.TextField(blank=True)

    def __str__(self):
        return f"Career Guidance for {self.course.course_name}" if self.course else "General Career Guidance"


# Model for Previous Q/P & Ans (Optional Feature)
class Admin_PreviousQP(models.Model):
    course = models.OneToOneField(Course, on_delete=models.CASCADE, related_name='previous_qp', blank=True, null=True)
    title = models.CharField(max_length=255)
    question_paper = models.FileField(upload_to='question_papers/', blank=True)
    answer_sheet = models.FileField(upload_to='answer_sheets/', blank=True)

    def __str__(self):
        return f"Previous Q/P for {self.course.course_name}" if self.course else "General Previous Q/P"


# Model for 1-1 Mentorship (Optional Feature)
class Admin_Mentorship(models.Model):
    course = models.OneToOneField(
        Course, on_delete=models.CASCADE, related_name='mentorship', blank=True, null=True
    )
    mentor = models.ForeignKey(
        Admin_Mentor, on_delete=models.SET_NULL, null=True, blank=True, related_name='mentorships'
    )
    is_enabled = models.BooleanField(default=False)
    session_amount = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    request_date = models.DateTimeField(auto_now_add=True, null=True, blank=True)  # Add the request date
    status = models.CharField(
        max_length=20,
        choices=[('Pending', 'Pending'), ('Accepted', 'Accepted'), ('Rejected', 'Rejected')],
        default='Pending'
    )

    def __str__(self):
        return f"Mentorship for {self.course.course_name}" if self.course else "General Mentorship"


# Model for Discussion Forum
class Admin_DiscussionForum(models.Model):
    course = models.OneToOneField(Course, on_delete=models.CASCADE, related_name='discussion_forum')
    common_forum_enabled = models.BooleanField(default=False)

    def __str__(self):
        return f"Discussion Forum for {self.course.course_name}"


########COURSE PROVIDER MANAGEMENT####################################################################################################################################################################################


class Admin_CourseEnrollment(models.Model):
    student = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, related_name='enrollments', on_delete=models.CASCADE)
    enrollment_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "Course Enrollments"

    def __str__(self):
        return f"{self.course} - {self.enrollment_date}"


class Admin_Payment(models.Model):
    PAYMENT_METHOD_CHOICES = [
        ('credit_card', 'Credit Card'),
        ('paypal', 'PayPal'),
        ('bank_transfer', 'Bank Transfer'),
        ('other', 'Other'),
    ]

    STATUS_CHOICES = [
        ('completed', 'Completed'),
        ('pending', 'Pending'),
        ('failed', 'Failed'),
    ]

    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='payments')
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='payments')
    enrollment = models.ForeignKey('Enrollment', on_delete=models.CASCADE, related_name='admin_payment', blank=True, null=True)
    amount_paid = models.DecimalField(max_digits=10, decimal_places=2)
    date_of_payment = models.DateTimeField(auto_now_add=True)
    invoice_id = models.CharField(max_length=100, unique=True)
    payment_method = models.CharField(max_length=20, choices=PAYMENT_METHOD_CHOICES, default='credit_card')
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    transaction_id = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return f"Invoice {self.invoice_id} - {self.student.user.username} - {self.course.course_name}"
    
