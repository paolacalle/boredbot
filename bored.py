import requests
import pprint
import pandas as pd
import sqlalchemy as db

baseURL = "http://www.boredapi.com/api/activity?"
attributes = ['type', 'price range', 'accessibility', 'participants']

# Database connection
engine = db.create_engine('sqlite:///activities.db')
connection = engine.connect()
metadata = db.MetaData()

# Define the table structure
activities_table = db.Table('activities', metadata,
                            db.Column('id', db.Integer(), primary_key=True),
                            db.Column('activity', db.String(255)),
                            db.Column('type', db.String(255)),
                            db.Column('price_range', db.String(255)),
                            db.Column('accessibility', db.Float()),
                            db.Column('participants', db.Integer())
                            )
metadata.create_all(engine)
insert_query = activities_table.insert()


def save_activity(activity):
    ins = insert_query.values(
        activity=activity['activity'],
        type=activity['type'],
        price_range=activity['price'],
        accessibility=activity['accessibility'],
        participants=activity['participants']
    )
    connection.execute(ins)


def get_type():
    types = ["education",
             "recreational",
             "social",
             "diy",
             "charity",
             "cooking",
             "relaxation",
             "music",
             "busywork"]
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
            print(f"\nSorry, but {selectedType} is an Invalid input!")


def get_price_range():
    foundMin = False
    foundMax = False

    priceRange = "\nNote: 0 being free and 1 being the most expensive."

    while foundMin is False:
        print("\nWhat is your minimum price range for an activity?")
        selectedMin = int(input())

        if 0 <= selectedMin <= 1:
            foundMin = True
        else:
            print("\nInvalid Input, range is 0-1.")

    while foundMax is False:
        print("\nWhat is your maximum price range for an activity?")
        selectedMax = int(input())

        if selectedMax < selectedMin:
            print("\nMax cannot be smaller than min.")
        elif 0 <= selectedMax <= 1:
            foundMax = True
        else:
            print("\nInvalid Input, range is 0-1.")

    priceURL = f"minprice={selectedMin}&maxprice={selectedMax}"
    return priceURL


def get_accessibility():
    valid = False
    print("\nRange 0-1, where 0 is least accessible and 1 is most accessible)")

    while valid is False:
        print("\nWhat is your desired accessibility rating for an activity?")
        selectedAR = int(input())

        if 0 <= selectedAR <= 1:
            accessibilityURL = f"accessibility={selectedAR}"
            return accessibilityURL
        else:
            print(f"\nInput {selectedAR} is out of the range 0-1.")


def get_participants():
    valid = False
    while valid is False:
        print("\nWhat is your desired number of participants? ")
        selectedParticipantNum = int(input())

        if selectedParticipantNum <= 0:
            print("\nYou need at least one participant.")
        else:
            participantURL = f"participants={selectedParticipantNum}"
            return participantURL


# Displaying DataFrame
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
    validResponse = False
    while validResponse is False:
        print("\n\nWould you like to stay in this same category "
              "or switch to a different one? (Stay or Switch)")
        print("\nType \"display\" to see previous activities.\n")
        categoryResponse = input().lower()

        if categoryResponse == "stay":
            return False
        elif categoryResponse == "switch":
            return True
        elif categoryResponse == "display":
            display_activities()
        else:
            print("\nInvalid input.")


def display_activities():
    select_query = db.select(activities_table)
    result_set = connection.execute(select_query)
    activities = result_set.fetchall()

    if activities:
        print(f"\n\n{pd.DataFrame(activities).to_string(index=False)}\n\n")
    else:
        print("\nNo previous activities found.\n")


def call_attribute(attr):
    if attr == "type":
        return get_type()
    elif attr == "price range":
        return get_price_range()
    elif attr == "accessibility":
        return get_accessibility()
    elif attr == "participants":
        return get_participants()


def run_program():
    end = False
    get_new_attr = True
    attr = ""

    while not end:
        if get_new_attr:
            print(f"\nWhat attributes do you care about the most?"
                  f"\n\n{attributes}.\n\n")
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
                        save_activity(activity_dic)
                        get_new_attr = stay_switch()

                else:
                    print("\nSorry, we are unable to find an activity "
                          "that matches this preference.")

            else:
                print("\nUnable to find an activity\
                        that matches this preference.")

        else:
            print("\n\nInput a valid attribute")

    print("\n\nThank you for chatting with me. Activities:\n\n")
    display_activities()


if __name__ == "__main__":
    run_program()
