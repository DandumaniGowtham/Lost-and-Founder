from datetime import datetime

lost_items = []
found_items = []


# Validate Date
def validate_date(date):
    try:
        datetime.strptime(date, "%Y-%m-%d")
        return True
    except ValueError:
        return False

# Register Lost and Found Item

def register_item(item_type):
    print(f"\n \t \t \t \t --- Register a {item_type} Item ----\n")

    item_id = input("ID: ").strip().lower()
    category = input("Category: ").strip().lower()
    item_name = input("Item Name: ").strip().lower()
    identifier = input("Brand / Company / Author / Bank / Institution: ").strip().lower()
    description = input("Description: ").strip().lower()
    location = input("location: ").strip().lower()
    date = input("Date (YYYY-MM-DD): ").strip()

    if not item_id or not category or not item_name or not identifier or not description or not location:
        print("All Fields are required!")
        return

    if not validate_date(date):
        print("Invalid Date format: ")
        return

    item = {
        "item_id" : item_id,
        "category" : category,
        "item_name" : item_name,
        "identifier" : identifier,
        "description" : description,
        "location" : location,
        "date" : date,
        "status" : "open"
    }

    if item_type == "Lost":
        lost_items.append(item)
    else:
        found_items.append(item)

    print(f"\n{item_type} Item Registered Successfully")


# search items by Category and Location
def search_item():
    print("\n \t \t \t \t --- Seach Item by Category and LOcation --- ")
    cur_category = input("Category of Item: ").strip().lower()
    cur_location = input("Location of Item: ").strip().lower()
    isFound = False

    if not cur_category or not cur_location:
        print("Both fields are required! ")
        return

    for item in lost_items + found_items :
        if item["category"] == cur_category and item["location"] == cur_location:
            isFound = True
            print("\nID:", item["item_id"])
            print("Category:", item["category"])
            print("Item Name:", item["item_name"])
            print("Identifier:", item["identifier"])
            print("Description:", item["description"])
            print("Location:", item["location"])
            print("Date:", item["date"])
            print("Status:", item["status"])

    if not isFound:
        print("No Items found")

# calculate match perfomance score
def calculate_match_score(lost_item, found_item):
    score = 0

    if lost_item["category"] == found_item["category"]:
        score += 20

    if lost_item["item_name"] == found_item["item_name"]:
        score += 20

    if lost_item["identifier"] == found_item["identifier"]:
        score += 10

    if lost_item["location"] == found_item["location"]:
        score += 10

    if lost_item["date"] == found_item["date"]:
        score += 10

    lost_keywords = set(lost_item["description"].split())
    found_keywords = set(found_item["description"].split())

    common_keywords = lost_keywords & found_keywords

    if len(common_keywords) >= 3:
        score += 30
    elif common_keywords:
        score += 10
    else:
        score += 0

    return score



#Suggest possible matches
def suggest_possible_match():
    print("\n \t \t \t \t --- Possible Matches --- \n")
    if not lost_items:
        print("No lost items ")
        return

    if not found_items:
        print("No found items")
        return 
    
    match_found = False

    for lost_item in lost_items:

        if lost_item["status"] == "open":

            for found_item in found_items:

                if found_item["status"] == "open":

                    score =  calculate_match_score(lost_item, found_item)
                    if score >= 50:
                        match_found = True

                        category_match = lost_item["category"] == found_item["category"]
                        item_name_match = lost_item["item_name"] == found_item["item_name"]
                        identifier_match = lost_item["identifier"] == found_item["identifier"]
                        location_match = lost_item["location"] == found_item["location"]
                        date_match = lost_item["date"] == found_item["date"]

                        lost_keywords = set(lost_item["description"].split())
                        found_keywords = set(found_item["description"].split()) 

                        common_words = lost_keywords & found_keywords

                        if lost_keywords == found_keywords:
                            keywords_match = "fully matched"
                        elif common_words :
                            keywords_match = "partially matched"


                        print("\n \t\t\t Possible Match found")

                        print("Lost Report ID: ", lost_item["item_id"])
                        print("Found Report ID: ", found_item["item_id"])

                        if category_match:
                            print("\nLost Item Category: ",lost_item["category"])
                            print("Found Item Category: ",found_item["category"])
                        else:
                            print("No Category match")

                        if item_name_match:
                            print("\nLost Item Name: ",lost_item["item_name"])
                            print("Found Item Name: ",found_item["item_name"])
                        else:
                            print("No Item name match")

                        if identifier_match:
                            print("\nLost Item Identifier: ",lost_item["identifier"])
                            print("Found Item Identifier: ",found_item["identifier"])  
                        else:
                            print("No Identifier match")

                        if location_match:
                            print("\nLost Item Location: ",lost_item["location"])
                            print("Found Item Location: ",found_item["location"]) 
                        else:
                            print("No location match") 

                        if date_match:
                            print("\nLost Item Date: ",lost_item["date"])
                            print("Found Item Date: ",found_item["date"]) 
                        else:
                            print("No date match")  

                        if common_words:
                            print("\nKeyword match: ",keywords_match)
                            print("Lost Item Keywords: ",lost_keywords)
                            print("Found Item Keywords: ",found_keywords)  
                        else:
                            print("No keywords match")    

                        print("\nConfidense Score: ", score)

    if not match_found:
        print("No match found")
        return


# update report status 
def update_report_status():
    print("\n \t \t \t \t --- Update Report Status ---")
    item_id = input("Item report ID: ").strip().lower()
    new_status = input("Status (open / Matched / Returned): ").strip().lower()

    if new_status not in["open", "matched", "returned"]:
        print("Invalid status")
        return
    
    for item in lost_items + found_items:
        if item["item_id"] == item_id:
            item["status"] = new_status
            print("Status updated Successfully ")
            return
        
    print("Invalid Item ID")

                       
# Display all the record with open status
def display_all_open_reports():
    print("\n \t \t \t \t --- All Open Reports  ---")
    found = False

    for item in lost_items + found_items :
        if item["status"] == "open":
            found = True
            print("\nID:", item["item_id"])
            print("Category:", item["category"])
            print("Item Name:", item["item_name"])
            print("Identifier:", item["identifier"])
            print("Description:", item["description"])
            print("Location:", item["location"])
            print("Date:", item["date"])
            print("Status:", item["status"])

    if not found:
        print("No Items found")


# Main Menu
def main():

    while(True):
        print("\n \t \t \t \t ---- LOST and FOUND Matcher ----\n\n ")

        print("1. Register Lost Item")
        print("2. Register Found Item")
        print("3. Search Items")
        print("4. Suggest Possible Matches")
        print("5. Update Status")
        print("6. Display Open Reports")
        print("7. Exit")

        choice = int(input("\nEnter you Choice: ").strip())

        if choice == 1:
            register_item("Lost")
        elif choice == 2:
            register_item("Found")
        elif choice == 3:
            search_item()
        elif choice == 4:
            suggest_possible_match()
        elif choice == 5:
            update_report_status()
        elif choice == 6:
            display_all_open_reports()
        elif choice == 7:
            print("Exited from Lost and Founder")
            break
        else:
            print("Invalid Choice")

main()
    