# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
import requests

SERVER_URL = 'http://172.105.38.177'

class ActionGreet(Action):

    def name(self) -> Text:
        return "action_greet"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        buttons = []
        buttons.append({"title": "Connect to Knowledge Base", "payload": "Knowledge Base"})

        dispatcher.utter_message(text="Hi! My name is Chirpy and I am a NLU Demo Bot built by Lilchirp Team.")
        dispatcher.utter_message(text="I can perform Complex Question and Answering using Knowledge Bases.")
        dispatcher.utter_message(text="Do you want to connect to knowledge base (KB).", buttons=buttons)

        return []


class ActionGoodBye(Action):

    def name(self) -> Text:
        return "action_goodbye"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        buttons = []
        buttons.append({"title": "Connect to KB", "payload": "Knowledge Base"})

        dispatcher.utter_message(text="Bye. Hope you have a very Good Day.")
        dispatcher.utter_message(text="Just letting you know that i can perform Complex Question and Answering using Knowledge Bases.")
        dispatcher.utter_message(text="Do you want to connect to knowledge base (KB).", buttons=buttons)

        return []

class ActionIamBot(Action):

    def name(self) -> Text:
        return "action_iamabot"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        buttons = []
        buttons.append({"title": "Connect to KB", "payload": "Knowledge Base"})

        dispatcher.utter_message(text="I am a Human-bot, powered by LilChirp NLU Engine 😄.")
        dispatcher.utter_message(text="I can perform Complex Question and Answering using Knowledge Bases.")
        dispatcher.utter_message(text="Do you want to connect to knowledge base (KB).", buttons=buttons)

        return []

class ActionAskAny(Action):

    def name(self) -> Text:
        return "action_ask_anything"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        buttons = []
        buttons.append({"title": "game-of-thrones", "payload": "game-of-thrones"})
        buttons.append({"title": "meditations", "payload": "meditations"})
        buttons.append({"title": "customer care", "payload": "customer-care"})
        dispatcher.utter_message(text="Good Choice. Please choose the name of NLU Engine you want to talk to.", buttons=buttons)

        return []



class ActionNameKB(Action):

    def name(self) -> Text:
        return "action_name_kb"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        # buttons = []
        # buttons.append({"title": "Connect to KB", "payload": "Knowledge Base"})

        name_kb = tracker.get_slot("name_kb")
        dispatcher.utter_message(text="Perfect 😄.")
        dispatcher.utter_message(text="I m ready to answer anything about {}. ".format(name_kb))
        return []

class ActionKB(Action):

    def name(self) -> Text:
        return "action_kb"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        # buttons = []
        # buttons.append({"title": "Connect to KB", "payload": "Knowledge Base"})
        current_state = tracker.current_state()
        msg = str(current_state["latest_message"]["text"])
        print(msg)
        # msg = str(tracker.latest.text)
        name_kb = tracker.get_slot("name_kb").lower()
        if name_kb == "meditations":
            url = "{}:8001/get_query".format(SERVER_URL)
            payload={'q': '{}'.format(msg)}
            files=[

            ]
            headers = {}
            response = requests.request("POST", url, headers=headers, data=payload, files=files)
            response = response.json()
            print(response)
            dispatcher.utter_message(text="Here is your answer 😄.")
            dispatcher.utter_message(text=response['answers'][0]['answer'])
            dispatcher.utter_message(text="The Context of Answer is :")
            dispatcher.utter_message(text=response['answers'][0]['context'])
            
        elif name_kb == "customer-care":
            url = "{}:8002/get_query".format(SERVER_URL)
            payload={'q': '{}'.format(msg)}
            files=[

            ]
            headers = {}
            response = requests.request("POST", url, headers=headers, data=payload, files=files)
            response = response.json()
            print(response)
            dispatcher.utter_message(text="Here is your answer 😄.")
            dispatcher.utter_message(text=response['answers'][0]['answer'])
            dispatcher.utter_message(text="The Context of Answer is :")
            dispatcher.utter_message(text=response['answers'][0]['context'])
            dispatcher.utter_message(text="The score of Answer is : {}".format(response['answers'][0]['score']))
        elif name_kb == "game-of-thrones":
            url = "{}:8000/get_query".format(SERVER_URL)
            payload={'q': '{}'.format(msg)}
            files=[

            ]
            headers = {}
            response = requests.request("POST", url, headers=headers, data=payload, files=files)
            response = response.json()
            print(response)
            dispatcher.utter_message(text="Here is your answer 😄.")
            dispatcher.utter_message(text=response['answers'][0]['answer'])
            dispatcher.utter_message(text="The Context of Answer is :")
            dispatcher.utter_message(text=response['answers'][0]['context'])
            dispatcher.utter_message(text="The score of Answer is : {}".format(response['answers'][0]['score']))
            # dispatcher.utter_message(text=response['context_1'])
        # dispatcher.utter_message(text="I m ready to answer anything about {}. ".format(name_kb))
        return []