# Libraries
import random

# Login 
def login():
  pin = input("Enter your password: ")
  # pin
  if pin == "arunabha":  
    return True
  else:
    print("Invalid pin. Access denied.")
    return False

# login
if login():
  print("Welcome to First-Aid Assistant!")
  while True:
    # menu
    print("\nFirst Aid Chart")
    print("1. Guide to First Aid")
    print("2. References")
    print("3. Emergency Contact")
    print("4. Exit")
    choice = input("Enter your choice (1-4): ")

    # choice=1
    if choice == "1":
      procedures = {
          "1": "CPR",
          "2": "Choking",
          "3": "Bleeding Control Prevention",
          "4": "Burns",
          "5": "Sprains and Strains",
          "6": "Allergic Reactions"
          # can Add more procedures
      }
      print("\nSteps and Procedures:")
      for key, value in procedures.items():
        print(f"{key}. {value}")
      choice = input("Enter procedure number ('B' or 'b' to go back): ")
      if choice.lower() == 'b':
          continue
      elif choice.lower()=='B':
          continue
      elif choice in procedures:
        print(f"\n{procedures[choice]} Procedure:")
        # procedure choice
        print("Recovering steps for", procedures[choice])
        # steps
        steps = [
            "Step 1: Access the situation and ensure safety.",
            "Step 2: Follow the guidance for ",procedures[choice],
            "Step 3: Search for medical help locally."
        ]
        for step in steps:
          print(step)
      else:
        print("Invalid choice. Please try again.")
    #choice=2
    elif choice == "2":
      # firstaid points reference
      print("\nQuick Reference:")
      points = {
          "1": "Vital Signs (pulse, respiration)",
          "2": "Signs and Symptoms of Shock",
          "3": "Poisioning",
          "4": "Head Injuries",
      }
      print("Choose a topic for more info:")
      for key, value in points.items():
        print(f"{key}. {value}")
      usr_choice = input("Enter choice number ('B' or 'b' to go back): ")
      if usr_choice.lower() == 'b':
        continue
      elif choice.lower()=='B':
          continue
      elif usr_choice in points:
        print(f"\nSummary of {points[usr_choice]}")
        # sumary of the topics
        print("A summary of", points[usr_choice], "will be shown")
      else:
        print("Invalid choice. Please try again.")
    #choice=3
    elif choice == "3":
      # emergency contact
      print("\nEmergency Contact:")
       #emergency number
      emergency_number = "101" 
      print(f"Emergency Services Number: {emergency_number}")
      # Hospital names
      hospitals = ["Health World Hospital", "Mission Hospital","Vivekananda Hospital"]
      hospital_choice = random.choice(hospitals)
      print(f"Nearest Hospital: {hospital_choice}")
    #choice=4
    elif choice == "4":
      print("Exiting First Aid Asistance.")
      break

    else:
      print("Invalid choice. Please try again.")

else:
  print("Access Denied.")
