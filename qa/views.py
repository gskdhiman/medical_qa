# reference: https://www.django-rest-framework.org/api-guide/views/
from django.shortcuts import render
from django.http import JsonResponse
from django.template.loader import render_to_string
from django.views.decorators.csrf import csrf_protect, csrf_exempt
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from qa.get_answer import get_answer
import json
from medical_qa.settings import STATIC_URL


class QaView(APIView):
    def get(self, request):
        # print("STATIC_URL: ",STATIC_URL)
        return render(request, 'index.html')

@csrf_exempt
def get_training(request):
    return render(request, 'train.html')

@csrf_exempt
def get_answer_json(request):
    data = json.loads(request.body)
    context = data.get('context', None)
    question = data.get('question', None)
    # print(f"context: {context}")
    # print(f"question: {question}")
    answer, confidence = get_answer(question, context)

    msg = render_to_string("messages.html", {"tags": "success", "message": "Fetching Answer"})
    data = {"answer": answer,
            "tokens": [str(x) for x in confidence['token']],
            "start": [str(x) for x in confidence['start']],
            "end": [str(x) for x in confidence['end']],
            "msg": msg}
    return JsonResponse(data)
