# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

# from typing import Any, Text, Dict, List
#
# from rasa_sdk import Action, Tracker
# from rasa_sdk.executor import CollectingDispatcher
#
#
# class ActionHelloWorld(Action):
#
#     def name(self) -> Text:
#         return "action_hello_world"
#
#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#
#         dispatcher.utter_message(text="Hello World!")
#
#         return []

#from typing import Any, Text, Dict, List
#from rasa_sdk import Action, Tracker
#from rasa_sdk.executor import CollectingDispatcher
#from rasa_sdk.events import SlotSet

#class ActionSignIn(Action):
#    def name(self) -> Text:
#        return "action_sign_in"

#    def run(self, dispatcher: CollectingDispatcher,
#            tracker: Tracker,
#            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#        email = tracker.get_slot("email")
#        password = tracker.get_slot("password")
#        # Implement sign-in logic here, and return appropriate message
#        dispatcher.utter_message(text=f"Signed in as {email}")
#        return []

#class ActionFindNearestBranch(Action):
#    def name(self) -> Text:
#        return "action_find_nearest_branch"

#def run(self, dispatcher: CollectingDispatcher,
#           tracker: Tracker,
#            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#        location = tracker.get_slot("location")
#        # Implement logic to find nearest branch based on location
#        dispatcher.utter_message(text=f"Nearest branch to {location} found.")
#        return []
