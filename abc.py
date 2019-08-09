from __future__ import absolute_import
from __future__ import division
from __future__ import unicode_literals

from rasa_core_sdk import Action
from rasa_core_sdk.events import SlotSet


class ActionInfraCost(Action):
    def name(self):
        return 'action_infra_cost'

    def run(self, dispatcher, tracker, domain):
        app = tracker.get_slot('app')
        response = "300k is the infra YTD(till April 2019)"
        dispatcher.utter_message(response)
        return []





class ActionPeoplesCost(Action):
    def name(self):
        return 'action_people_cost'

    def run(self, dispatcher, tracker, domain):
        app = tracker.get_slot('app')
        dispatcher.utter_message("400k is the People YTD(till April 2019)")
        return []
