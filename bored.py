import requests
import pprint 
import pandas as pd
import sqlalchemy as db

baseURL = "http://www.boredapi.com/api/activity?"
attributes = ['type', 'price Range', 'accessibility', 'participants']

def get_type():
    types = ["education", "recreational", "social", "diy", "charity", "cooking", "relaxation", "music", "busywork"]
    print("\nChoose one of the following types: ")
    for item in types:
        print(item)
    selectedType = input().lower()

    if selectedType in types:
        typeURL = "type=" + selectedType
        get_activity(typeURL)
    
def get_price_range():
    # check that requests is valid especially with price ranges past 0.6
    priceRange = "(0.00 being free and 1.00 being the most expensive)" 

    print("\nWhat is your minimum price range for an activity?" + priceRange)
    selectedMin = input().lower()

    print("\nWhat is your maximum price range for an activity?" + priceRange)
    selectedMax = input().lower()

    priceURL = "minprice=" + selectedMin + "&maxprice=" + selectedMax
    get_activity(priceURL)

def get_accessibility():
    accesibilityRating = "(0.0 being the least accessible and 1.0 being the most accessible)"

    print("\nWhat is your desired accesibility rating for an activity? " + accesibilityRating)
    selectedAR = input().lower()

    accessbilityURL = "accessibility=" + selectedAR
    get_activity(accessbilityURL)

def get_participants():
    participantRange = "(You can choose between 1-8 participants)"

    print("\nWhat is your desired number of participants? " +participantRange)
    selectedParticipantNum = input().lower()

    participantURL = "participants=" + selectedParticipantNum
    get_activity(participantURL)

def get_activity(url):
    response = requests.get(baseURL + url)
    if "error" in f"{response}": 
        print("\nSorry, we do not have an activity the meets these requests.")
    else:
        message = response.json()
        display_response(message)

def get_opinion():
    print("\nWould you like another? (Yes or No)")
    likeResponse = input().lower()

    if likeResponse not in ["yes", "no"]:
        get_opinion()

    if likeResponse == "yes":
        return False
    else:
        return True 


#Displaying Dataframe 
def display_response(message):
    df = pd.DataFrame.from_dict(message, orient= 'index')
    pprint.pprint(df)

    # print(f"\nActivity: {message['activity']}")
    # print(f"Type: {message['type']}")
    # print(f"Accessibility: {message['accessibility']}")
    # print(f"Participants: {message['participants']}")
    # print(f"Price: {message['price']}")   
    
def call_attribute(attr): 
    if attr == "type": 
        get_type()
    elif attr == "price range": 
        get_price_range()
    elif attr == "accessibility":
        get_accessibility()
    elif attr == "participants":
        get_participants()

print(f"\nWhat attributes do you care about the most? {attributes}.")
attr = input().lower()
end = False 

while not end: 
    if attr in attributes:
        call_attribute(attr)

        end = get_opinion()
    
        if end == False:
            print("\n\nWould you like to stay in this same category or switch to a different one? (Stay or Switch)")
            categoryResponse = input().lower()               
            if categoryResponse == "Stay":
                call_attribute(attr) 
                
            else:
                print(f"\nWhat attributes do you care about the most? {attributes}")
                attr = input().lower()
                call_attribute(attr)


    else:
        print("\nInput a valid attribute: (Type, Price Range, Accessibility, Participants)")
        attr = input().lower()
        call_attribute(attr)
