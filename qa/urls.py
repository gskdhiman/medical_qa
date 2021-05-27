from django.urls import path

from qa.views import QaView, get_answer_json, get_training

urlpatterns = [
    # for method 1
    path('qa/', QaView.as_view(), name='QA View'),
    path('qa/get_answer_json', get_answer_json, name='Get answer json'),
    # path('qa/train', get_training, name='Get answer json'),
]