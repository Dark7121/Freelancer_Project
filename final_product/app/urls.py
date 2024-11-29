from django.urls import path, include
from.views import *
from django.contrib.auth import views as auth_views


urlpatterns = [

     path('course_payment/<int:course_id>/', course_payment, name='course_payment'),

     path('add-to-cart/<int:course_id>/', add_to_cart, name='add_to_cart'),
     # path('view-cart/', view_cart, name='view_cart'),
     path('remove-from-cart/<int:course_id>/', remove_from_cart, name='remove_from_cart'),

     path('add-to-wishlist/<int:course_id>/', add_to_wishlist, name='add_to_wishlist'),
     path('wishlist/', wishlist, name='wishlist'),
     path('wishlist/remove/<int:course_id>/', remove_from_wishlist, name='remove_from_wishlist'),



     path('update-profile/', update_profile, name='update_profile'),

     path('question-paper/<str:pk>/download/', download_question_paper, name='download_question_paper'),
     # path('course/<int:course_id>/topic/<int:topic_id>/', watch_topic, name='watch_topic'),
     path('quiz/<int:quiz_id>/', display_quiz, name='display_quiz'),
     path('quiz/<int:quiz_id>/result/', quiz_results, name='quiz_results'),

     path('blog/<int:post_id>/edit/', blog_update, name='blog_update'),
     path('blog/<int:post_id>/delete/', blog_delete, name='blog_delete'),


     path('weekly_platform/<int:week_number>/', weekly_platform, name='weekly_platform'),
     path('weekly_platform/add_week_post/<int:week_number>/', add_week_post, name='add_week_post'),
     path('weekly_platform/add_week_comment/<int:week_number>/<int:week_post_id>/', add_week_comment, name='add_week_comment'),

     path('like_week_post/<int:week_post_id>/', like_week_post, name='like_week_post'),
     path('dislike_week_post/<int:week_post_id>/', dislike_week_post, name='dislike_week_post'),
     path('like_week_comment/<int:week_comment_id>/', like_week_comment, name='like_week_comment'),
     path('dislike_week_comment/<int:week_comment_id>/', dislike_week_comment, name='dislike_week_comment'),


     # Front urls
     path('landing_page/', landing_page, name='landing_page'),
     path('', landing_page_before_login, name='landing_page_before_login'),
     path('about_us', about_us, name='about_us'),
     path('contact_us', contact_us, name='contact_us'),
     path('course/', course, name='course'),
     path('common_discussion_forum', common_discussion_forum, name='common_discussion_forum'),
     path('single_post_discussion_forum', single_post_discussion_forum, name='single_post_discussion_forum'),
     path('week_basis_discussion_forum', week_basis_discussion_forum, name='week_basis_discussion_forum'),
     path('my_learnings', my_learnings, name='my_learnings'),
     path('cart', cart, name='cart'),
     path('search_page', search_page, name='search_page'),
     path('course_after_login', course_after_login, name='course_after_login'),
     path('roadmap_after_pg', roadmap_after_pg, name='roadmap_after_pg'),
     path('roadmap_after_pg_in_comm', roadmap_after_pg_in_comm, name='roadmap_after_pg_in_comm'),
     path('roadmap_after_pg_in_elec', roadmap_after_pg_in_elec, name='roadmap_after_pg_in_elec'),
     path('roadmap_after_pg_in_hm', roadmap_after_pg_in_hm, name='roadmap_after_pg_in_hm'),
     path('notes', notes, name='notes'),
     path('download_pdf', download_pdf, name='download_pdf'),
     path('module', module, name='module'),
     path('my_course', my_course, name='my_course'),
     path('course_material/<int:id>/', course_material, name='course_material'),
     path('payment', payment, name='payment'),
     path('reply_to_post', reply_to_post, name='reply_to_post'),
     path('course_video/<int:course_id>/<int:week_id>/<int:topic_id>/', course_video, name='course_video'),
     path('course_overview', course_overview, name='course_overview'),

     path('quiz_page/<int:id>/', quiz_page, name='quiz_page'),

     path('assignment_page', assignment_page, name='assignment_page'),
     # path('quiz_questions', quiz_questions, name='quiz_questions'),
     path('assessment_questions', assessment_questions, name='assessment_questions'),
     path('result', result, name='result'),
     path('quiz_result', quiz_result, name='quiz_result'),
     path('assessment_result', assessment_result, name='assessment_result'),
     path('certificate', certificate, name='certificate'),
     path('single_certificate/<int:course_id>', single_certificate, name='single_certificate'),
     path('ticket', ticket, name='ticket'),
     path('referral', referrals, name='referral'),
     path('payment_history', payment_history, name='payment_history'),
     path('profile_page', profile_page, name='profile_page'),
     path('bundle/<int:bundle_id>/', bundle_detail, name='bundle_detail'),
     path('referral_progress', referral_progress, name='referral_progress'),
     path('tech_courses', tech_courses, name='tech_courses'),
     path('ncert_courses', ncert_courses, name='ncert_courses'),
     path('question_papers', question_papers, name='question_papers'),
     path('grade_wise_courses', grade_wise_courses, name='grade_wise_courses'),
     path('roadmap', roadmap, name='roadmap'),
     path('blog_details/<int:post_id>/', blog_details, name='blog_details'),
     path('blog', blog, name='blog'),
     path('faq', faq, name='faq'),
     path('chat_box', chat_box, name='chat_box'),
     path('login',do_login,name='login'),
     path('student-signup/',student_signup,name='student-signup'),
     path('verify-otp',verify_otp,name='verify_otp'),
     path('logout/', logout_user, name='logout'),

     path('course_catalog', course_catalog, name='course_catalog'),
     path('career_roadmap', career_roadmap, name='career_roadmap'),

     path('mentorship_page/', homepage, name='mentorship_page'),
     path('paymenthandler/', paymenthandler, name='paymenthandler'),
     path('course/<int:course_id>/', view_course_details, name='view_course_details'),
     path('enroll-course/<int:course_id>/', enroll_course, name='enroll_course'),
     path('course_payment/<int:course_id>/', course_payment, name='course_payment'),
     path('enrolled-courses/', enrolled_course, name='enrolled_course'),
     path('enrolled-courses/<int:course_id>/start-course', start_course, name='start_course'),
     path('start-course/<int:course_id>/previous_question_papers/', previous_question_papers,name='previous_question_papers'),

     path('community/',community_platform, name='community_platform'),
     path('community/add_post/',add_post, name='add_post'),
     path('community/add_comment/<int:post_id>/',add_comment, name='add_comment'),

     path('like_post/<int:post_id>/',like_post, name='like_post'),
     path('dislike_post/<int:post_id>/',dislike_post, name='dislike_post'),
     path('like_comment/<int:comment_id>/', like_comment, name='like_comment'),
     path('dislike_comment/<int:comment_id>/', dislike_comment, name='dislike_comment'),

     path('courses/<int:course_id>/', courses, name='courses'),
     path('notes/<int:course_id>/', notes_list, name='notes_list'),
     path('download-certificate/<int:certificate_id>/', download_certificate, name='download_certificate'),
     path('chat_history/', get_chat_history, name='get_chat_history'),
     path('send_message/', send_message, name='send_message'),
     path('send_admin_message/', send_admin_message, name='send_admin_message'),
     path('ckeditor/', include('ckeditor_uploader.urls')),
######################################################################################################################################
#-------------------------------------------------------------------------------------------------------------------------------------
#COURSE PROVIDER URLS
#-------------------------------------------------------------------------------------------------------------------------------------
######################################################################################################################################

    path('course_provider/base/', BASE_CP, name='provider_base'),
    #path('accounts/', include('django.contrib.auth.urls')),
    #path('accounts/login/', auth_views.LoginView.as_view(), name='login'),
    #path('course_provider/register', register_CP, name = 'provider_register'),
    #path('doLogin', user_login.DO_LOGIN, name="provider_doLogin"),
    path('course_provider/upload_course/', upload_course_CP, name='provider_upload_course'),  #UPLOAD COURSE
    path('course_provider/course/<int:pk>/detail/', course_detail_CP, name='provider_course_detail'),
    path('course_provider/course/<int:pk>/overview/', course_overview_CP, name='provider_course_overview'),
    path('course_provider/course/<int:course_id>/', quiz_detail_CP, name='provider_quiz_detail'),
    path('course_provider/assign-quiz/', assign_quiz_CP, name='provider_assign_quiz'),
    path('course_provider/upload/', upload_result_CP, name='provider_upload_result'),
    path('course_provider/upload_assignment/', upload_assignment_result_CP, name='provider_upload_assignment_result'),
    path('course_provider/result/<int:student_id>/', view_result_CP, name='provider_view_result'),
    path('course_provider/result/&lt;int:student_id&gt;/', view_result_CP, name='provider_view_result'),
    path('course_provider/student_results/', student_results_CP, name='provider_student_results'),
    path('course_provider/create/', create_payout_statement_CP, name='provider_create_payout_statement'),
    path('course_provider/list/', payout_statement_list_CP, name='provider_payout_statement_list'),

    path('course_provider/',provider_login_CP,name='provider_login'),
    path('course_provider/index/',index_CP,name='provider_index'),
    path('course_provider/profile/',profile_CP,name='provider_profile'),
    path('course_provider/course/',course_CP,name='provider_course'),
    path('course_provider/payout_statement/',payout_statement_CP,name='provider_payout_statement'),
    path('course_provider/settings/',settings_CP,name='provider_settings'),
    path('course_provider/course_detail_sub/<int:id>/',course_detail_sub_CP,name='provider_course_detail_sub'),
    path('course_provider/assignment_result/',assignment_result_CP,name='provider_assignment_result'),
    path('course_provider/quiz_result/', quiz_result_CP,name='provider_quiz_result'),




######################################################################################################################################
#-------------------------------------------------------------------------------------------------------------------------------------
#ADMIN URLS
#-------------------------------------------------------------------------------------------------------------------------------------
######################################################################################################################################



    #path('login',admin_do_login,name='admin_login'),
    #path('admin-signup/',admin_admin_signup,name='admin_admin-signup'),
    #path('verify-otp',admin_verify_otp,name='admin_verify_otp'),
    path('feedback/', admin_feedback_page, name='admin_feedback_page'),
    path('offers/', admin_offers_view, name='admin_offers_page'),
    path('create-vouchers/', admin_create_voucher_view, name='admin_create_voucher'),
    path('affiliate-marketers/', admin_affiliate_market_list, name='admin_affiliate-market-list'),
    path('affiliate-marketers/<int:marketer_id>/', admin_affiliate_market_detail, name='admin_affiliate-market-detail'),
    path('affiliate-marketers/create/', admin_affiliate_market_create, name='admin_affiliate-market-create'),
    path('affiliate-marketers/update/<int:marketer_id>/', admin_affiliate_marketer_update, name='admin_affiliate-marketer-update'),
    path('affiliate-marketers/delete/<int:marketer_id>/', admin_affiliate_market_delete, name='admin_affiliate-market-delete'),
    path('affiliate-accounts/', admin_affiliate_account_list, name='admin_affiliate-account-list'),
    path('affiliate-accounts/<int:account_id>/', admin_affiliate_account_detail, name='admin_affiliate-account-detail'),
    path('affiliate-accounts/create/', admin_affiliate_account_create, name='admin_affiliate-account-create'),
    path('affiliate-accounts/update/<int:account_id>/', admin_affiliate_account_update, name='admin_affiliate-account-update'),
    path('affiliate-marketers/search/', admin_affiliate_marketer_search, name='admin_affiliate-marketer-search'),
    path('affiliate-marketers/freeze/<int:marketer_id>/', admin_affiliate_marketer_freeze, name='admin_affiliate-marketer-freeze'),
    path('affiliate-marketers/reset/<int:marketer_id>/', admin_affiliate_marketer_reset, name='admin_affiliate-marketer-reset'),
    path('affiliate-market', admin_affiliate_market,name='admin_affiliate-market'),
    path('identify-top-performers/', admin_identify_top_performers, name='admin_identify-top-performers'),

    # Course URLs
    path('course/', admin_course_list, name='admin_course_list'),
    path('course/<int:course_id>/', admin_view_course, name='admin_view_course'),
    path('course/create/', admin_create_course, name='admin_create_course'),
    path('course/<int:course_id>/edit/', admin_edit_course, name='admin_edit_course'),
    path('course/<int:course_id>/delete/', admin_Delete_course, name='admin_delete_course'),

    # Assignment URLs
    path('assignment/<int:course_id>/create/', admin_create_assignment, name='admin_create_assignment'),
    path('assignment/<int:assignment_id>/edit/', admin_edit_assignment, name='admin_edit_assignment'),
    path('assignment/<int:assignment_id>/delete/', admin_delete_assignment, name='admin_delete_assignment'),
    path('assignment/<int:assignment_id>/mark/', admin_mark_assignment, name='admin_mark_assignment'),
    path('assignment/submissions/', admin_view_submissions, name='admin_view_submissions'),
    path('assignment/<int:assignment_id>/submit/', admin_submit_assignment, name='admin_submit_assignment'),
    path('assignment-list/', admin_assignment_list,name='admin_assignment_list'),
    path('assignment/<int:assignment_id>/feedback/', admin_view_assignment_feedback, name='admin_view_assignment_feedback'),

    # Quiz URLs
    path('quiz/create/', admin_create_quiz, name='admin_create_quiz'),
    path('quiz/<int:quiz_id>/add/', admin_add_question, name='admin_add-question'),  # URL for adding questions
    path('quiz/<int:quiz_id>/take/', admin_take_quiz, name='admin_take-quiz'),
    path('create-quiz-result/<int:quiz_id>/', admin_create_quiz_result,name='admin_create-quiz-result'),
    path('quiz/<int:quiz_id>/results/', admin_quiz_results, name='admin_quiz-results'),

    path('quiz-list', admin_quiz_list,name='admin_quiz_list'),
    # path('quiz/<int:quiz_id>/edit/', edit_quiz, name='edit-quiz'),

    # # Delete Quiz
    # path('quiz/<int:quiz_id>/delete/', delete_quiz, name='delete-quiz'),

    # Quiz Detail
    path('quiz/<int:quiz_id>/', admin_quiz_detail, name='admin_quiz-detail'),

    # Quiz Results
    # path('quiz/<int:quiz_id>/results/', quiz_results, name='quiz-results'),
    # path('quiz/<int:quiz_id>/edit/', edit_quiz, name='edit_quiz'),
    # path('quiz/<int:quiz_id>/delete/', delete_quiz, name='delete_quiz'),



    ## Marketing and Promotions URL
    path('marketing-promotions/', admin_marketing_promotions, name='admin_marketing_promotions'),
    path('track-clicks/', admin_track_clicks, name='admin_track_clicks'),
    path('course-data/', admin_course_data, name='admin_course_data'),
    path('referral-program/', admin_referral_program, name='admin_referral_program'),


    path('course-provider/', admin_create_course_provider_management,name='admin_create-course-provider-management'),

    # URL patterns for adding, editing, and deleting payout details
    path('payout-details/add/', admin_add_payout_detail, name='admin_add_payout_detail'),
    path('payout-details/<int:payout_detail_id>/edit/', admin_edit_payout_detail, name='admin_edit_payout_detail'),
    path('payout-details/<int:payout_detail_id>/delete/', admin_delete_payout_detail, name='admin_delete_payout_detail'),




    # Miscellaneaous URLs
    # path('course/<int:course_id>/assignments/', view_assignments, name='view_assignments'),


    path('Super-panel', admin_Super_panel,name='admin_super-panel'),
    path('content-management', admin_content_management,name='admin_content-management'),
    path('user-management', admin_User_Management,name='admin_user-management'),
    path('course-management', admin_course_provider_management,name='admin_course-provider-management'),

     #Static frontend pages
    #path('', admin_landing_page,name='admin_landing_page'),
    #path('login_page', admin_login_page,name='admin_login_page'),
    path('teachers', admin_teachers, name='admin_teachers'),
    path('begin_class_dashboard_container', admin_begin_class_dashboard_container,name='admin_begin_class_dashboard_container'),
    path('main_dashboard', admin_main_dashboard,name='admin_main_dashboard'),
    path('student_management/<int:pk>/', admin_student_management,name='admin_student_management'),
    #path('signup', admin_signup,name='admin_signup'),
    path('student_management_course_enroll', admin_student_management_course_enroll,name='admin_student_management_course_enroll'),
    path('student_management_referral_detail', admin_student_management_referral_detail,name='admin_student_management_referral_detail'),
    path('student_management_payment_details', admin_student_management_payment_details,name='admin_student_management_payment_details'),
    path('provider_management', admin_provider_management,name='admin_provider_management'),
    path('provider_management_dashboard', admin_provider_management_dashboard,name='admin_provider_management_dashboard'),
    path('provider_management_payment', admin_provider_management_payment,name='admin_provider_management_payment'),
    path('provider_management_payment_view', admin_provider_management_payment_view,name='admin_provider_management_payment_view'),
    path('provider_management_payment_pay', admin_provider_management_payment_pay,name='admin_provider_management_payment_pay'),
    path('dashboard_support_panel_chat', admin_dashboard_support_panel_chat,name='admin_dashboard_support_panel_chat'),
    path('dashboard_analytics', admin_dashboard_analytics,name='admin_dashboard_analytics'),
    path('course_manage_add_course', admin_course_manage_add_course,name='admin_course_manage_add_course'),
    path('course_provider_database', admin_course_provider_database,name='admin_course_provider_database'),
    path('course_provider_create_account_form', admin_course_provider_create_account_form,name='admin_course_provider_create_account_form'),
    # path('dashboard_feedback',dashboard_feedback.as_view(), name='formfeedback_list'),
    path('dashboard_create_feedback', admin_dashboard_create_feedback,name='admin_dashboard_create_feedback'),
    path('dashboard_feedback_view', admin_dashboard_feedback_view,name='admin_dashboard_feedback_view'),
    path('affiliate_marketing_main_page', admin_affiliate_marketing_main_page,name='admin_affiliate_marketing_main_page'),
    path('marketing_promotion_referal', admin_marketing_promotion_referal,name='admin_marketing_promotion_referal'),
    path('marketing_promotion_view_bills', admin_marketing_promotion_view_bills,name='admin_marketing_promotion_view_bills'),
    path('offers_voucher', admin_offers_voucher,name='admin_offers_voucher'),
    path('about_us', admin_about_us,name='admin_about_us'),
    path('provider_management_payment_page', admin_provider_management_payment_page,name='admin_provider_management_payment_page'),
    path('course_manage_main_page', admin_course_manage_main_page,name='admin_course_manage_main_page'),
    path('affiliate_marketing_payments', admin_affiliate_marketing_payments,name='admin_affiliate_marketing_payments'),
    path('affiliate_marketing_payments_pay', admin_affiliate_marketing_payments_pay,name='admin_affiliate_marketing_payments_pay'),
    path('affiliate_marketing_create_account', admin_affiliate_marketing_create_account,name='admin_affiliate_marketing_create_account'),
    path('course_manage_bulk_course', admin_course_manage_bulk_course,name='admin_course_manage_bulk_course'),
    path('course_manage_bulk_course_sub', admin_course_manage_bulk_course_sub,name='admin_course_manage_bulk_course_sub'),
    path('1_to_1_Mentorship', admin_one_to_one_Mentorship,name='admin_one_to_one_Mentorship'),
    path('student_management_database', admin_student_management_database,name='admin_student_management_database'),
    path('course_details_page', admin_course_details_page,name='admin_course_details_page'),
    path('course_details_quiz', admin_course_details_quiz,name='admin_course_details_quiz'),
    path('course_details_assignments', admin_course_details_assignments,name='admin_course_details_assignments'),
    path('course_details_main_quiz', admin_course_details_main_quiz,name='admin_course_details_main_quiz'),
    path('blog', admin_blog,name='admin_blog'),
    path('blog_add', admin_blog_add,name='admin_blog_add'),
    path('blog_edit/<int:pk>/', admin_edit_blog, name='admin_edit_blog'),
    path('blog_delete/<int:pk>/', admin_delete_blog, name='admin_delete_blog'),
    path('blog_create/', admin_create_blog, name='admin_create_blog'),

     # Other Student Management Views
    path('students/', admin_student_list, name='admin_student-list'),
    path('students/add/', admin_add_student, name='admin_add-student'),
    path('students/edit/<int:pk>/', admin_edit_student, name='admin_edit-student'),
    path('students/delete/<int:pk>/', admin_delete_student, name='admin_delete-student'),
    path('students/suspend/<int:pk>/', admin_suspend_student, name='admin_suspend-student'),
    path('students/<int:pk>/', admin_student_detail, name='admin_student-detail'),

    # path('offers/', offer_list, name='offer_list'),
    path('offers/create/', admin_create_voucher, name='admin_create_voucher'),
    path('offers/edit/<int:voucher_id>/', admin_edit_voucher, name='admin_edit_voucher'),
    path('offers/pause/<int:voucher_id>/', admin_pause_voucher, name='admin_pause_voucher'),
    path('offers/unpause/<int:voucher_id>/', admin_unpause_voucher, name='admin_unpause_voucher'),  # Add this line
    path('offers/stop/<int:voucher_id>/', admin_stop_voucher, name='admin_stop_voucher'),
    path('offers/use/<str:voucher_code>/', admin_use_voucher, name='admin_use_voucher'),
    path('offers/', admin_offers_page, name='admin_offers_page'),

    path('FeedbackPortal/', FormFeedbackListView.as_view(), name='admin_formfeedback_list'),
    path('FeedbackPortal/form/new/', FormFeedbackCreateView.as_view(), name='admin_formfeedback_create'),
    path('FeedbackPortal/form/<int:pk>/edit/', FormFeedbackUpdateView.as_view(), name='admin_formfeedback_update'),
    path('FeedbackPortal/form/<int:pk>/delete/', FormFeedbackDeleteView.as_view(), name='admin_formfeedback_delete'),
    # path('FeedbackPortal/form/<int:formfeedback_id>/question/add/', add_question, name='add_question'),
    # path('FeedbackPortal/question/<int:question_id>/options/', manage_options, name='manage_options'),
    path('FeedbackPortal/form/<int:formfeedback_id>/submit/', admin_submit_feedback, name='admin_submit_feedback'),
    # path('FeedbackPortal/course_feedback_link/new/', CourseFeedbackLinkCreateView.as_view(), name='course_feedback_link_create'),
    # path('FeedbackPortal/course_feedback_link/<int:pk>/delete/', CourseFeedbackLinkDeleteView.as_view(), name='course_feedback_link_delete'),
    path('tickets/<int:ticket_id>/', admin_ticket_detail, name='admin_ticket_detail'),
]
