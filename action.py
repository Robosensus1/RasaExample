from __future__ import absolute_import
from __future__ import division
from __future__ import unicode_literals
import requests
import json
from twilio.rest import Client
from random import randint

from rasa_core_sdk import Action
from rasa_core_sdk.events import SlotSet
from typing import Dict, Text, Any, List, Union

from rasa_core_sdk import ActionExecutionRejection
from rasa_core_sdk import Tracker
from rasa_core_sdk.events import SlotSet
from rasa_core_sdk.executor import CollectingDispatcher
from rasa_core_sdk.forms import FormAction, REQUESTED_SLOT


class insuranceform(FormAction):
	def name(self):
		return 'insurance_form'

	@staticmethod
	def required_slots(tracker):
		return ["name","gender","dob","email","contact","address","city","state","zipcode","SSN"]

	def validate(self, dispatcher, tracker, domain):
		slot_values = self.extract_other_slots(dispatcher, tracker, domain)

		#if slot_to_fill:
		#  dispatcher.utter_message("Enter your {}".format(slot_to_fill))
		#dispatcher.utter_message("Enter your {}".format(tracker.get_slot(REQUESTED_SLOT)))
		#dispatcher.utter_message("Enter your {}".format(tracker.current_slot_values))
		#dispatcher.utter_message("Enter your {}".format(tracker.current_state))
		slot_to_fill = tracker.get_slot(REQUESTED_SLOT)
		if slot_to_fill:
			slot_values.update(self.extract_requested_slot(dispatcher, tracker, domain))
		#response1 = "HELLOHELLO "
		#dispatcher.utter_message(response1)
		return [SlotSet(slot, value) for slot, value in slot_values.items()]

	def submit(self, dispatcher, tracker, domain):
		#response1 = "HELLOHELLOaa "
		#dispatcher.utter_message(response1)
		name=tracker.get_slot("name")
		gender=tracker.get_slot("gender")
		dob=tracker.get_slot("dob")
		email=tracker.get_slot("email")
		contact=tracker.get_slot("contact")
		address=tracker.get_slot("address")
		city=tracker.get_slot("city")
		state=tracker.get_slot("state")
		zipcode=tracker.get_slot("zipcode")
		SSN=tracker.get_slot("SSN")
		dispatcher.utter_message("You have entered:")
		dispatcher.utter_message("Name : {} ".format(name))
		dispatcher.utter_message("Gender : {} ".format(gender))
		dispatcher.utter_message("DOB : {} ".format(dob))
		dispatcher.utter_message("Email : {} ".format(email))
		dispatcher.utter_message("Contact : {} ".format(contact))
		dispatcher.utter_message("Address : {} ".format(address))
		dispatcher.utter_message("City : {} ".format(city))
		dispatcher.utter_message("state : {} ".format(state))
		dispatcher.utter_message("Zip code : {} ".format(zipcode))
		dispatcher.utter_message("SSN : {} ".format(SSN))
		#dispatcher.utter_message("height is {} ".format(hgt))
		#dispatcher.utter_message(slot_values[weight])
		#dispatcher.utter_message(slot_values[height])
		#dispatcher.utter_message(bmi)
		return []

	def slot_mappings(self):
		return {"name": self.from_text(),
				"gender": self.from_text(),
				"dob": self.from_text(),
				"email": self.from_text(),
				"contact": self.from_text(),
				"address": self.from_text(),
				"city": self.from_text(),
				"state": self.from_text(),
				"zipcode": self.from_text(),
				"SSN": self.from_text()
				}




