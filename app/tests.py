from django.test import TestCase
from decouple import config
import unittest
import json
import os
import datetime
from app.CustomCode import string_generator, password_functions
import app
import jwt

# Create your tests here.


class MetaCraftTestCase(TestCase):
    def setUp(self):
        return

    def test_home(self):
        """The api index page display accordinging"""
        res = self.client.get("/")
        init = json.dumps(res.data)
        data = json.loads(init)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data["success"], True)
        self.assertEqual(data["message"], "Welcome to VTF Server home page")

    def test_auth(self):  # Generate token
        """Test to see if authenticaton with token works"""
        timeLimit = datetime.datetime.utcnow() + datetime.timedelta(
            minutes=1440
        )  # set duration for token
        payload = {
            "test_id": f"{string_generator.alphanumeric(8)}",
            "exp": timeLimit,
        }
        token = jwt.encode(payload, config("SECRET_KEY"), algorithm="HS256")

        res = self.client.post(
            "/auth",
            HTTP_AUTHORIZATION="Bearer " + str(token),
        )
        init = json.dumps(res.data)
        data = json.loads(init)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data["success"], True)

    def test_isaca_event(self):
        """Testing the isaca event endpoint to display appriopriately"""
        res = self.client.get("/isaca-events")
        init = json.dumps(res.data)
        data = json.loads(init)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data["success"], True)

    def test_speaker_signup(self):
        """Testing the VTF speaker signup endpoint to display appriopriately"""
        new_user = {
            "firstname": "Daniel",
            "lastname": "Testing",
            "email": "todak2000@gmail.com",
            "password": "test123",
        }

        res = self.client.post(
            "/vtf-speaker-signup",
            new_user,
        )
        init = json.dumps(res.data)
        data = json.loads(init)
        # print(data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data["success"], True)
        self.assertEqual(data["message"], "The registration was successful.")
