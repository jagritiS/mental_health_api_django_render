from rest_framework.decorators import api_view
from rest_framework.response import Response

responses = {
    "sad": "It's okay to feel sad sometimes. You are not alone.",
    "stress": "Try taking deep breaths and short breaks.",
    "anxious": "Focus on breathing slowly. Things will get better.",
    "lonely": "Try connecting with a friend or loved one."
}


@api_view(["POST"])
def chat(request):
    message = request.data.get("message", "").lower()

    reply = "I'm here to listen. Tell me more."

    for keyword in responses:
        if keyword in message:
            reply = responses[keyword]
            break

    return Response({
        "user_message": message,
        "reply": reply
    })


@api_view(["GET"])
def moods(request):
    return Response({
        "supported_moods": list(responses.keys())
    })


from django.shortcuts import render

# Create your views here.
