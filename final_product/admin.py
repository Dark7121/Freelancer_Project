from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(CustomeUser)
admin.site.register(Student)
admin.site.register(Course)
admin.site.register(Enrollment)
admin.site.register(MentorshipRequest)
admin.site.register(QuestionPaper)


admin.site.register(Week)
admin.site.register(Topic)

admin.site.register(Ticket)

admin.site.register(Profile)

admin.site.register(WorkExperience)
admin.site.register(Education)
admin.site.register(Project)
admin.site.register(NotificationSettings)
admin.site.register(PrivacySettings)
admin.site.register(Referral)
admin.site.register(PaymentHistory)


admin.site.register(Note)
admin.site.register(Message)
admin.site.register(CareerGuidanceMessage)
admin.site.register(Resource)

admin.site.register(BlogPost)
admin.site.register(BlogComment)


admin.site.register(Certificate)
admin.site.register(Discussion)

admin.site.register(Post)
admin.site.register(Comment)

admin.site.register(WeekPost)
admin.site.register(WeekComment)


class ChatMessageAdmin(admin.ModelAdmin):
    list_display = ('user', 'message', 'timestamp', 'is_admin')
    search_fields = ('user__user__email', 'message')
    readonly_fields = ('timestamp',)

    def save_model(self, request, obj, form, change):
        if not obj.pk:  # if creating a new message
            obj.is_admin = True
        super().save_model(request, obj, form, change)


admin.site.register(ChatMessage, ChatMessageAdmin)




class QuestionInline(admin.TabularInline):
    model = QuizQuestion
    extra = 1  # Start with one extra form
    show_change_link = True

@admin.register(Quiz)
class QuizAdmin(admin.ModelAdmin):
    inlines = [QuestionInline]

admin.site.register(QuizResult)
admin.site.register(Grade)
admin.site.register(Bundle)

admin.site.register(Admin_ReferralProgram)
admin.site.register(Admin_Voucher)

admin.site.register(Admin_Payment)

admin.site.register(Admin_ChatMessage)
admin.site.register(Admin_Mentorship)
admin.site.register(Admin_Mentor)
admin.site.register(Admin_AffiliateMarketer)
admin.site.register(Admin_EnrolledUser)
admin.site.register(Admin_Sale)
admin.site.register(Admin_AffiliateAccount)
admin.site.register(Admin_CourseProvider)










