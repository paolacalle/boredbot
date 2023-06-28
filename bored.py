import requests
import pprint
import pandas as pd
import sqlalchemy as db

baseURL = "http://www.boredapi.com/api/activity?"
attributes = ['type', 'price range', 'accessibility', 'participants']


def get_type():
    types = [
        "education",
        "recreational",
        "social",
        "diy",
        "charity",
        "cooking",
        "relaxation",
        "music",
        "busywork"
    ]
    foundType = False
    while foundType is False:
        print("\nChoose one of the following types:\n")

        for item in types:
            print(f"{item}")
        print()

        selectedType = input().lower()

        if selectedType in types:
            typeURL = "type=" + selectedType
            return typeURL
        else:
            print(f"\nSorry, but {selectedType} is an Invaild input!")


def get_price_range():
    foundMin = False
    foundMax = False
    selectedMin = -1
    selectedMax = -1

    priceRange = "\nNote: 0 being free and 1 being the most expensive." 

    while foundMin is False:
        print("\nWhat is your minimum price range for an activity?")
        selectedMin = int(input())

        if 0 <= selectedMin <= 1: 
            foundMin = True
        else: 
            print("\nInvaild Input, range is 0-1.")

    while foundMax is False:
        print("\nWhat is your maximum price range for an activity?")
        selectedMax = int(input())

        if selectedMax < selectedMin:
            print("\nMax can not be smaller then min.")
        elif 0 <= selectedMax <= 1: 
            foundMax = True
        else:
            print("\nInvaild Input, range is 0-1.")

    priceURL = f"minprice={selectedMin}&maxprice={selectedMax}"
    return priceURL


def get_accessibility():
    vaild = False
    print("\nRange 0-1, where 0 is least accessible and 1 is most accessible)")

    while vaild is False:
        print("\nWhat is your desired accesibility rating for an activity?")
        selectedAR = int(input())

        if 0 <= selectedAR <= 1:
            accessbilityURL = f"accessibility={selectedAR}"
            return accessbilityURL
        else: 
            print(f"\nInput {selectedAR} is out of the range 0-1.")


def get_participants():
    print("\nWhat is your desired number of participants? ")
    selectedParticipantNum = input().lower()
    participantURL = "participants=" + selectedParticipantNum
    return participantURL


# Displaying Dataframe 
def display_response(message):
    df = pd.DataFrame.from_dict(message, orient='index')
    pprint.pprint(df)


def get_opinion():
    print("\nWould you like another? (Yes or No)")
    likeResponse = input().lower()

    if likeResponse not in ["yes", "no"]:
        get_opinion()

    if likeResponse == "yes":
        return False
    else:
        return True 


def stay_switch():
    vaildRespose = False
    while vaildRespose is False: 
        print("\n\nWould you like to stay in this same "
              "category or switch to a different one? (Stay or Switch)")
        categoryResponse = input().lower()

        if categoryResponse == "stay":
            return False
        elif categoryResponse == "switch": 
            return True 
        else: 
            print(f"\nInvaild stay/switch input: {categoryResponse}")


def call_attribute(attr): 
    if attr == "type": 
        return get_type()
    elif attr == "price range": 
        return get_price_range()
    elif attr == "accessibility":
        return get_accessibility()
    elif attr == "participants":
        return get_participants()


end = False 
get_new_attr = True 
atrr = ""


while not end: 
    if get_new_attr:
        print(f"\nWhat attributes do you care about the most?\
        \n\n{attributes}.\n\n")
        attr = input().lower()

    if attr in attributes:
        url = call_attribute(attr)
        if url: 
            response = requests.get(baseURL + url)
            activity_dic = response.json()

            if "error" not in activity_dic: 
                display_response(activity_dic)
                end = get_opinion()

                if end is False:
                    get_new_attr = stay_switch()

            else: 
                print("\nSorry, we are unable to find an activity "
                      "that matches this preference.")

        else: 
            print("\nUnable to find an activity that matches this preference.")

    else:
        print("\n\nInput a valid attribute")
