from django.shortcuts import render
from app.models import EventSchedule
from rest_framework.decorators import api_view
from rest_framework.response import Response
from vtf_server import settings
from .auth.auth import token_required
from .models import EventSchedule, format_data, Speaker
from .CustomCode import validator, string_generator, password_functions

import json
from decouple import config
import datetime
import jwt
import requests

# Create your views here.


# Landing page
@api_view(["GET"])
def index(request):
    return_data = {"success": True, "status": 200,
                   "message": "Welcome to VTF Server home page"}
    return Response(return_data)

# Testing the Authentication module


@api_view(["POST"])
@token_required
def test_auth(request, payload):
    return_data = {
        "success": True,
        "payload": payload,
        "status": 200,
    }
    return Response(return_data)

# isaca event schedule get api


@api_view(["GET"])
def isaca_events(request):
    # get today's date
    today = datetime.date.today()
    try:
        # fetch events that are still ongoing
        events = EventSchedule.objects.filter(day__gte=today)
        return_data = {"success": True, "status": 200,
                       "events": format_data(events)}
    except Exception as e:
        return_data = {"success": False, "status": 500, "message": str(e)}
    return Response(return_data)

# vtf_speaker signup api


@api_view(["POST"])
def speaker_signup(request):
    # get firstname and remove empty spaces
    firstName = request.data.get("firstname", None).replace(
        " ", "")
    # get lastname and remove empty spaces
    lastName = request.data.get("lastname", None).replace(
        " ", "")

    # get email, remove empty spaces and convert to lowercase
    email = request.data.get("email", None).replace(" ", "").lower()
    # get password
    password = request.data.get("password", None)
    reg_field = [firstName, lastName, email, password]
    try:
        if not None in reg_field and not "" in reg_field:
            if (Speaker.objects.filter(email=email).exists()):
                return_data = {
                    "success": False,
                    "status": 422,  # Not Processable
                    "message": "User Exists",
                }
            else:
                # encrypt password
                encryped_password = password_functions.generate_password_hash(
                    password)
                # Add speaker_data
                new_speaker = Speaker(
                    firstname=firstName,
                    lastname=lastName,
                    email=email,
                    password=encryped_password,
                )
                # Save new speaker data
                new_speaker.save()
                if new_speaker:
                    return_data = {"success": True, "status": 201,
                                   "message": "The registration was successful."}
    except Exception as e:
        return_data = {"success": False, "status": 500, "message": str(e)}
    return Response(return_data)
