from django import forms
from .models import *
from django.utils import timezone
from django.contrib.auth.forms import PasswordChangeForm
from django.core.exceptions import ValidationError


class LoginForm(forms.Form):
    email = forms.EmailField(max_length=255, widget=forms.TextInput(
        attrs={'placeholder': 'Email'}))
    password = forms.CharField(max_length=255, widget=forms.PasswordInput(
        attrs={'placeholder': 'Password'}))


class UserForm(forms.ModelForm):
    class Meta:
        models = CustomeUser
        fields = ['username', 'email', 'password', 'user_type']  # Add or remove fields as needed

        labels = {
            'username': 'Username',
            'email': 'Email',
            'password': 'Password',
            'user_type': 'User Type',
        }
        widgets = {
            'password': forms.PasswordInput(),
        }


class AdminForm(forms.ModelForm):
    password1 = forms.CharField(max_length=255, widget=forms.PasswordInput(
        attrs={'placeholder': 'Create Password'}))
    password2 = forms.CharField(max_length=255, widget=forms.PasswordInput(
        attrs={'placeholder': 'Re-enter Password'}))
    DOB = forms.DateField(widget=forms.DateInput(
        attrs={'type': 'date'}))  # Ensure proper widget for DOB FIELD

    class Meta:
        model = Student
        fields = ['Full_Name', 'Mobile_no', 'EmailID',
                  'DOB', 'Gender', 'password1', 'password2']

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords do not match")
        return password2


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['bio', 'profile_picture', 'mobile_number', 'language', 'linkedin_profile', 'twitter_profile',
                  'facebook_profile']


class EmailChangeForm(forms.ModelForm):
    class Meta:
        model = CustomeUser
        fields = ['email']

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if CustomeUser.objects.exclude(pk=self.instance.pk).filter(email=email).exists():
            raise ValidationError("Email already exists.")
        return email


class CustomPasswordChangeForm(PasswordChangeForm):
    def __init__(self, *args, **kwargs):
        super(CustomPasswordChangeForm, self).__init__(*args, **kwargs)
        for fieldname in ['old_password', 'new_password1', 'new_password2']:
            self.fields[fieldname].help_text = None


class WorkExperienceForm(forms.ModelForm):
    start_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    end_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))

    class Meta:
        model = WorkExperience
        fields = ['company_name', 'position', 'start_date', 'end_date', 'description']


class EducationForm(forms.ModelForm):
    start_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    end_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))

    class Meta:
        model = Education
        fields = ['institution_name', 'degree', 'field_of_study', 'start_date', 'end_date']


class ProjectForm(forms.ModelForm):
    start_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    end_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))

    class Meta:
        model = Project
        fields = ['title', 'description', 'start_date', 'end_date', 'url']


class PrivacySettingsForm(forms.ModelForm):
    class Meta:
        model = PrivacySettings
        fields = [
            'show_profile_to_logged_in_users',
            'show_courses_on_profile'
        ]
        labels = {
            'show_profile_to_logged_in_users': 'Show your profile page to logged-in users',
            'show_courses_on_profile': 'Show courses you\'re taking on your profile page'
        }


class NotificationSettingsForm(forms.ModelForm):
    class Meta:
        model = NotificationSettings
        fields = ['promotion', 'helpful_resources', 'no_promotional_email']
        labels = {
            'promotion': 'Receive promotions and special offers',
            'helpful_resources': 'Receive helpful resources and course recommendations',
            'no_promotional_email': 'Do not send me any promotional emails'
        }


class ReferralForm(forms.ModelForm):
    class Meta:
        model = Referral
        fields = ['friend_email']
        labels = {
            'friend_email': 'Friend\'s Email'
        }



class BlogPostForm(forms.ModelForm):
    class Meta:
        model = BlogPost
        fields = ['title', 'content', 'tags'] ##, 'image'


class BlogCommentForm(forms.ModelForm):
    class Meta:
        model = BlogComment
        fields = ['content']



######################################################################################################################################
#-------------------------------------------------------------------------------------------------------------------------------------
#COURSE PROVIDER FORMS
#-------------------------------------------------------------------------------------------------------------------------------------
######################################################################################################################################



class AssignQuizForm(forms.ModelForm):
    course = forms.ModelChoiceField(queryset=Course.objects.all(), label="Select Course")
    quiz = forms.ModelChoiceField(queryset=Quiz.objects.all(), label="Select Quiz")

class ResultForm(forms.ModelForm):
    class Meta:
        model = ResultByProvider
        fields = ['student', 'quiz', 'score']

class AssignmentResultForm(forms.ModelForm):
    class Meta:
        model = AssignmentResultByProvider
        fields = ['student', 'assignment', 'score']

class PayoutStatementForm(forms.ModelForm):
    class Meta:
        model = PayoutStatementByProvider
        fields = ['payment_details', 'image']




######################################################################################################################################
#-------------------------------------------------------------------------------------------------------------------------------------
#ADMIN FORMS
#-------------------------------------------------------------------------------------------------------------------------------------
######################################################################################################################################



from .models import *
from django.forms.models import inlineformset_factory
from django import forms
from django.contrib.auth import get_user_model
from ckeditor.widgets import CKEditorWidget
from django.utils import timezone
from django.conf import settings


class Admin_LoginForm(forms.Form):
    email = forms.EmailField(max_length=255, widget=forms.TextInput(
        attrs={'placeholder': 'Email'}))
    password = forms.CharField(max_length=255, widget=forms.PasswordInput(
        attrs={'placeholder': 'Password'}))


class Admin_EnrollmentForm(forms.ModelForm):
    class Meta:
        model = Enrollment
        fields = ['user', 'course']
        exclude = ['enrollment_date']
        widgets = {
            'user': forms.Select(attrs={'class': 'form-control'}),
            'course': forms.Select(attrs={'class': 'form-control'}),
        }


class Admin_OrderForm(forms.ModelForm):
    class Meta:
        model = Admin_Order
        fields = ['student', 'course', 'price']
        exclude = ['date']


class Admin_studentForm(forms.ModelForm):
    class Meta:
        model = CustomeUser
        fields = ['username', 'email', 'password', 'user_type', 'is_active']  # Add or remove fields as needed

        labels = {
            'username': 'Username',
            'email': 'Email',
            'password': 'Password',
            'user_type': 'User Type',
        }
        widgets = {
            'password': forms.PasswordInput()
        }


class Admin_ChangeCourseForm(forms.Form):
    student = forms.ModelChoiceField(queryset=CustomeUser.objects.filter(user_type=2, is_active=True),
                                     label="Select Student")
    course = forms.ModelChoiceField(queryset=Course.objects.all(), label="Select New Course")


class Admin_AdminForm(forms.ModelForm):
    password1 = forms.CharField(max_length=255, widget=forms.PasswordInput(
        attrs={'placeholder': 'Create Password'}))
    password2 = forms.CharField(max_length=255, widget=forms.PasswordInput(
        attrs={'placeholder': 'Re-enter Password'}))
    DOB = forms.DateField(widget=forms.DateInput(
        attrs={'type': 'date'}))  # Ensure proper widget for DOB FIELD

    class Meta:
        model = Admin_Admin
        fields = ['Full_Name', 'Mobile_no', 'EmailID',
                  'DOB', 'Gender', 'password1', 'password2']

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords do not match")
        return password2


class Admin_CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ['title', 'category_type', 'price', 'image', 'video']
        widgets = {
            'title': forms.TextInput(attrs={'placeholder': 'Enter course name'}),
            'category_type': forms.Select(attrs={'class': 'form-control'}),
            'price': forms.NumberInput(attrs={'placeholder': 'Enter course price'}),
            'image': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'video': forms.ClearableFileInput(attrs={'class': 'form-control'}), 
        }



class Admin_QuizForm(forms.ModelForm):
    class Meta:
        model = Admin_Quiz
        fields = ['title', 'description', 'course']


class Admin_QuestionForm(forms.ModelForm):
    class Meta:
        model = Admin_Question
        fields = '__all__'


OptionFormSet = forms.inlineformset_factory(
    Admin_Question,  # Parent model
    Admin_Choice,  # Child model
    fields=['choice_text', 'is_correct'],  # Add other fields as needed
    extra=0,  # Number of extra forms to display
    can_delete=True,  # Allow deletion of existing options
    min_num=4,  # Minimum number of forms required
    validate_min=True,  # Validate minimum forms
)


class Admin_AnswerForm(forms.ModelForm):
    class Meta:
        model = Admin_Answer
        fields = ['choice']
        widgets = {
            'choice': forms.RadioSelect,  # Assuming single choice for each question
        }


class Admin_OptionForm(forms.ModelForm):
    class Meta:
        model = Admin_Choice
        fields = "__all__"


class Admin_AssignmentForm(forms.ModelForm):
    due_date = forms.DateTimeField(
        widget=forms.DateTimeInput(attrs={'type': 'datetime-local'}))

    class Meta:
        model = Admin_Assignment
        fields = ['title', 'description', 'due_date']

    def clean_due_date(self):
        due_date = self.cleaned_data['due_date']
        if due_date < timezone.now():
            raise forms.ValidationError("Due date must be in the future.")
        return due_date


class Admin_AssignmentSubmissionForm(forms.ModelForm):
    class Meta:
        model = Admin_StudentAssignment
        fields = ['student', 'assignment', 'submission']

    def clean_submission(self):
        submission = self.cleaned_data['submission']
        if submission.size > 1024 * 1024 * 10:
            raise forms.ValidationError("File size must be less than 10MB.")
        return submission


class Admin_AssignmentFeedbackForm(forms.ModelForm):
    class Meta:
        model = Admin_AssignmentFeedback
        fields = ['feedback']


class Admin_QuizResultForm(forms.ModelForm):
    class Meta:
        model = Admin_Quiz_Result
        fields = ['student', 'quiz', 'score']

    def clean_score(self):
        score = self.cleaned_data['score']
        if score < 0 or score > 100:
            raise forms.ValidationError("Score must be between 0 and 100.")
        return score


class Admin_FeedbackForm(forms.Form):
    feedback = forms.CharField(widget=forms.Textarea)
    marks = forms.FloatField()


class Admin_VoucherForm(forms.ModelForm):
    class Meta:
        model = Admin_Voucher

        fields = ['code', 'discount', 'expiration_date', 'courses']  #Added Course here

        widgets = {
            'code': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter voucher code'}),
            'discount': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter discount'}),
            'expiration_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
           'courses': forms.ModelMultipleChoiceField(queryset=Course.objects.all(), widget=forms.SelectMultiple(attrs={'class': 'form-control'}), required=False),  # Use ModelMultipleChoiceField and SelectMultiple
        }

        labels = {
            'code': 'Voucher Code',
            'discount': 'Discount',
            'expiration_date': 'Expiration Date',
            'courses': 'Applicable Courses',
        }

        help_texts = {
            'code': 'Unique code for the voucher.',
            'discount': 'Discount percentage or amount.',
            'expiration_date': 'Expiration date of the voucher.',
            #'courses': 'Select courses this voucher applies to.',
        }

    def clean(self):
        cleaned_data = super().clean()

        code = cleaned_data.get('code')
        if Admin_Voucher.objects.filter(code=code).exists():
            self.add_error('code', 'A voucher with this code already exists.')

        return cleaned_data


class Admin_AffiliateMarketerForm(forms.ModelForm):
    class Meta:
        model = Admin_AffiliateMarketer
        fields = ['email', 'name', 'commission_percentage', 'is_frozen']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'commission_percentage': forms.NumberInput(attrs={'class': 'form-control'}),
            'is_frozen': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }


class Admin_AffiliateAccountForm(forms.ModelForm):
    class Meta:
        model = Admin_AffiliateAccount
        fields = ['marketer']
        widgets = {
            'marketer': forms.Select(attrs={'class': 'form-control'}),
        }


CustomUser = get_user_model()


class Admin_CourseProviderForm(forms.ModelForm):
    password1 = forms.CharField(widget=forms.PasswordInput)
    password2 = forms.CharField(widget=forms.PasswordInput)
    gender = forms.ChoiceField(choices=CustomeUser.GENDER_CHOICES, required=True)
    courses = forms.ModelMultipleChoiceField(queryset=Course.objects.all(), widget=forms.CheckboxSelectMultiple, required=False)
    account_name = forms.CharField(max_length=100)
    bank_name = forms.CharField(max_length=100)
    account_type = forms.CharField(max_length=50)
    account_number = forms.CharField(max_length=20)
    ifsc_code = forms.CharField(max_length=11)

    class Meta:
        model = CustomeUser
        fields = [
            'first_name', 'last_name', 'email', 'phone_number', 'gender',
            'account_name', 'bank_name', 'account_type', 'account_number', 'ifsc_code', 'courses'
        ]

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don't match")
        return password2

    def save(self, commit=True):
        user = super(Admin_CourseProviderForm, self).save(commit=False)
        user.set_password(self.cleaned_data['password1'])
        user.user_type = 3 
        if commit:
            user.save()
        return user


class Admin_PayoutDetailForm(forms.ModelForm):
    class Meta:
        model = Admin_PayoutDetail
        fields = ['course_provider', 'amount', 'payout_date', 'payout_method', 'transaction_id', 'payment_status']
        # exclude=['course_provider']


class Admin_PayoutBillForm(forms.ModelForm):
    class Meta:
        model = Admin_PayoutBill
        fields = ['payout_detail', 'image', 'bill_date', 'description']


class Admin_CourseOwnerEarningsForm(forms.ModelForm):
    class Meta:
        model = Admin_CourseOwnerEarnings
        fields = ['course_provider', 'total_earnings', 'previous_month_earnings']


class Admin_VoucherForm(forms.ModelForm):
    class Meta:
        model = Admin_Voucher
        fields = [
            'code', 'discount', 'discount_type', 'discount_limit', 'start_date', 'end_date', 'min_amount',
            'num_courses', 'courses', 'expiration_date'
        ]
        widgets = {
            'courses': forms.CheckboxSelectMultiple,
            'start_date': forms.DateInput(attrs={'type': 'date'}),
            'end_date': forms.DateInput(attrs={'type': 'date'}),
            'expiration_date': forms.DateInput(attrs={'type': 'date'}),
        }


class Admin_CreateVoucherForm(forms.ModelForm):
    courses = forms.ModelMultipleChoiceField(queryset=Course.objects.all(), widget=forms.CheckboxSelectMultiple)

    class Meta:
        model = Admin_Voucher
        fields = [
            'code', 'discount', 'discount_type', 'discount_limit', 'start_date', 'end_date', 'min_amount',
            'num_courses', 'courses', 'expiration_date'
        ]
        widgets = {
            'start_date': forms.DateInput(attrs={'type': 'date'}),
            'end_date': forms.DateInput(attrs={'type': 'date'}),
            'expiration_date': forms.DateInput(attrs={'type': 'date'}),
        }


class Admin_BlogForm(forms.ModelForm):
    class Meta:
        model = BlogPost
        fields = ['title', 'content', 'thumbnail', 'cover_pic', 'content', 'tags', 'category', 'trending', 'related_courses']
        widgets = {
            'content': forms.Textarea(attrs={'class': 'richtext'}),
            'tags': forms.TextInput(attrs={'placeholder': 'Add tags separated by commas'}),
            'related_courses': forms.CheckboxSelectMultiple(),
            'category': forms.Select(),
        }
        exclude = ['author', 'created_at', 'updated_at']


class Admin_BlogEditForm(Admin_BlogForm):
    class Meta(Admin_BlogForm.Meta):
        pass


class Admin_SettingsForm(forms.Form):
    enrollment_bonus = forms.IntegerField(initial=getattr(settings, 'ENROLLMENT_BONUS', 250))
    coin_conversion_rate = forms.DecimalField(initial=getattr(settings, 'COIN_CONVERSION_RATE', 25))


class Admin_ReferralForm(forms.Form):
    referred_email = forms.EmailField(label='Referred Student Email')


class Admin_TicketForm(forms.ModelForm):
    category = forms.ModelChoiceField(queryset=Admin_Category.objects.all(), required=True, label='Category')
    subcategory = forms.ModelChoiceField(queryset=Admin_Subcategory.objects.all(), required=True, label='Subcategory')
    reason = forms.CharField(widget=forms.Textarea, required=True, label='Reason')

    class Meta:
        model = Ticket
        fields = ['category', 'subcategory', 'reason']

    def __init__(self, *args, **kwargs):
        super(Admin_TicketForm, self).__init__(*args, **kwargs)
        self.fields['category'].queryset = Admin_Category.objects.all()
        self.fields['subcategory'].queryset = Admin_Subcategory.objects.all()

    def clean(self):
        cleaned_data = super().clean()
        category = cleaned_data.get('category')
        subcategory = cleaned_data.get('subcategory')

        if subcategory and subcategory.category != category:
            raise forms.ValidationError("Selected subcategory does not belong to the selected category.")

        return cleaned_data


class Admin_ChatMessageForm(forms.ModelForm):
    message = forms.CharField(widget=forms.Textarea(attrs={'rows': 3}), required=False, label='Message')
    attachment = forms.FileField(required=False, label='Attachment')

    class Meta:
        model = Admin_ChatMessage
        fields = ['message', 'attachment']

    def clean_attachment(self):
        attachment = self.cleaned_data.get('attachment')
        if attachment:
            if attachment.size > 10 * 1024 * 1024:  # 10MB
                raise forms.ValidationError("The maximum file size that can be uploaded is 10MB.")
            if not attachment.content_type in ['image/jpeg', 'image/png', 'application/pdf']:
                raise forms.ValidationError("Only JPEG, PNG images and PDF files are allowed.")
        return attachment


# Form for creating/editing Feedback Forms
class Admin_FormFeedbackForm(forms.ModelForm):
    class Meta:
        model = Admin_FormFeedback
        fields = ['title', 'description']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 3}),
        }


# Form for creating/editing Feedback Questions
class Admin_FeedbackQuestionForm(forms.ModelForm):
    class Meta:
        model = Admin_FeedbackQuestion
        fields = ['question_type', 'text']
        widgets = {
            'text': forms.Textarea(attrs={'rows': 3}),
        }


# Form for creating/editing Multiple Choice Options
class Admin_MultipleChoiceOptionForm(forms.ModelForm):
    class Meta:
        model = Admin_MultipleChoiceOption
        fields = ['option_text', 'is_correct']


# Formset for Multiple Choice Options within Feedback Question form
MultipleChoiceOptionFormSet = inlineformset_factory(
    Admin_FeedbackQuestion,
    Admin_MultipleChoiceOption,
    form=Admin_MultipleChoiceOptionForm,
    extra=1,
    can_delete=True
)


# Form for capturing Feedback Responses
class Admin_FeedbackResponseForm(forms.ModelForm):
    class Meta:
        model = Admin_FeedbackResponse
        fields = []  # No fields here, as we'll dynamically add answers for each question

    def __init__(self, *args, **kwargs):
        feedback_form = kwargs.pop('feedback_form')
        super().__init__(*args, **kwargs)

        # Dynamically add form fields for each question in the feedback form
        for question in feedback_form.questions.all():
            if question.question_type == 'text':
                self.fields[f'question_{question.id}'] = forms.CharField(label=question.text,
                                                                         widget=forms.Textarea(attrs={'rows': 3}))
            elif question.question_type == 'choice':
                choices = [(option.id, option.option_text) for option in question.options.all()]
                self.fields[f'question_{question.id}'] = forms.ChoiceField(label=question.text, choices=choices,
                                                                           widget=forms.RadioSelect)

    def save_answers(self, response):
        for field_name, value in self.cleaned_data.items():
            if field_name.startswith('question_'):
                question_id = int(field_name.split('_')[1])
                question = Admin_FeedbackQuestion.objects.get(id=question_id)

                if question.question_type == 'text':
                    Admin_FeedbackAnswer.objects.create(response=response, question=question, text_answer=value)
                elif question.question_type == 'choice':
                    choice_option = Admin_MultipleChoiceOption.objects.get(id=value)
                    Admin_FeedbackAnswer.objects.create(response=response, question=question, choice_answer=choice_option)


################################################################################################################################################################################################################
# User Management

CustomUser = get_user_model()


class Admin_StudentForm(forms.ModelForm):
    user = forms.ModelChoiceField(queryset=CustomUser.objects.all(), required=True)
    Full_Name = forms.CharField(max_length=20, required=True)
    Mobile_no = forms.CharField(max_length=10, required=True)
    EmailID = forms.EmailField(max_length=255, required=True)
    DOB = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}), required=True)
    Gender = forms.ChoiceField(choices=Student.Gender_choices, required=True)
    cart = forms.ModelMultipleChoiceField(queryset=Course.objects.all(), required=False,
                                          widget=forms.CheckboxSelectMultiple)
    wishlist = forms.ModelMultipleChoiceField(queryset=Course.objects.all(), required=False,
                                              widget=forms.CheckboxSelectMultiple)
    ongoing_courses = forms.ModelMultipleChoiceField(queryset=Course.objects.all(), required=False,
                                                     widget=forms.CheckboxSelectMultiple)
    completed_courses = forms.ModelMultipleChoiceField(queryset=Course.objects.all(), required=False,
                                                       widget=forms.CheckboxSelectMultiple)

    class Meta:
        model = Student
        fields = [
            'user', 'Full_Name', 'Mobile_no', 'EmailID', 'DOB', 'Gender',
            'cart', 'wishlist', 'ongoing_courses', 'completed_courses'
        ]

