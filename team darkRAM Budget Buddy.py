# SheHacks+ 7 Challenge #2: Python
# Team: darkRAM
# Team Members: Denny, Anna, Raisa, Kalpi

print("--------Hi! Welcome to Budget Buddy!---------")

# -------- PART 1: SETTING BUDGETS --------
# The first part of the code allows the user to set their budgets for Food, Entertainment, and Transportation categories. Users are also given the option to edit any previously set budget.

# User sets the budget for each category.
foodBudget = int(input("Please set a budget for Food Spending (EXAMPLE -- 100): "))

if type(foodBudget) == int:
    entertBudget = int(input("\nPlease set a budget for Entertainment Spending (EXAMPLE -- 100): "))

if type(entertBudget) == int:
    transportBudget = input("\nPlease set a budget for Transportation Spending (EXAMPLE -- 100): ")

# Print current set budgets.
print("\nFood: " + "$" + str(foodBudget))
print("Entertainment: " + "$" + str(entertBudget))
print("Transportation: " + "$" + str(transportBudget))

# Ask user if they want to continue or edit any budgets.
editQ = input("\nIf this looks correct and you would like to continue, enter \"Y\". If you would like to edit a category, enter \"N\". ").upper()

# If user wants to edit, run while loop.
while editQ != "Y":
    if editQ == "N":
      # Let user pick which category to reset budget for.
        editCat = input("\nWhich category would you like to edit? Food, Entertainment, or Transportation? ").upper()
        if editCat == "FOOD":
            editFood = int(input("\nPlease set a budget for Food Spending (EXAMPLE -- 100): "))
            foodBudget = editFood
            print("\nFood: " + "$" + str(foodBudget))
            print("Entertainment: " + "$" + str(entertBudget))
            print("Transportation: " + "$" + str(transportBudget))

            # Verify if user wants to continue or edit again.
            editQ = input(
              "\nIf this looks correct and you would like to continue, enter \"Y\". If you would like to edit a category, enter \"N\". ").upper()
        elif editCat == "ENTERTAINMENT":
            editEntert = int(input("\nPlease set a budget for Entertainment Spending (EXAMPLE -- 100): "))
            entertBudget = editEntert
            print("\nFood: " + "$" + str(foodBudget))
            print("Entertainment: " + "$" + str(entertBudget))
            print("Transportation: " + "$" + str(transportBudget))
            # Verify if user wants to continue or edit again.

            editQ = input(
              "\nIf this looks correct and you would like to continue, enter \"Y\". If you would like to edit a category, enter \"N\".").upper()
        elif editCat == "TRANSPORTATION":
            editTransport = int(input("\nPlease set a budget for Transportation Spending (EXAMPLE -- 100): "))
            transportBudget = editTransport
            print("\nFood: " + "$" + str(foodBudget))
            print("Entertainment: " + "$" + str(entertBudget))
            print("Transportation: " + "$" + str(transportBudget))

            # Verify if user wants to continue or edit again.
            editQ = input(
              "\nIf this looks correct and you would like to continue, enter \"Y\". If you would like to edit a category, enter \"N\". ").upper()
        # Error message or unexpected entry.
        else:
            print("Invalid entry. Please try again.")
            editQ = input("\nIf you would like to continue, enter \"Y\". If you would like to edit a category, enter \"N\". ").upper()
    # Error message or unexpected entry.
    else:
        print("\nInvalid entry. Please enter \"Y\" or \"N\".")
        editQ = input("\nIf you would like to continue, enter \"Y\". If you would like to edit a category, enter \"N\". ").upper()

# -------- PART 2: ENTERING PURCHASES --------
# This part asks user to input categories and purchases. Uses the inputted data to store and return how much the user spent in each category.

# Initializes 3 variables that store the total purchases in each of the three categories the user can input to track their budgeting
foodPurchases = 0
entertPurchases = 0
transportPurchases = 0

#Asks user for what catagories they want to calculate spending for
inputting = True
while inputting:
  totalPurchases = 0
  category = input("\nWhat category would you like to enter your purchases for? ")

# If user inputs food (in any case), asks user for the purchases in that category and totals the expenditure
  if category.upper() == "FOOD":
    purchase = input("\nPlease input a purchase amount. If you have entered all of your purchases, press 'enter': ")
    while purchase != "":
      totalPurchases += int(purchase)
      purchase = input("\nPlease input a purchase amount. If you have entered all of your purchases, press 'enter': ")
      foodPurchases = totalPurchases
    print("\nYou spent $%d on %s" % (totalPurchases, category))
    
  # If user inputs food (in any case), asks user for the purchases in that category and totals the expenditure
  elif category.upper() == "ENTERTAINMENT":
    purchase = input("\nPlease input a purchase amount. If you have entered all of your purchases, press 'enter': ")
    while purchase != "":
      totalPurchases += int(purchase)
      purchase = input("\nPlease input a purchase amount. If you have entered all of your purchases, press 'enter': ")
      entertPurchases = totalPurchases
    print("\nYou spent $%d on %s" % (totalPurchases, category))
  # If user inputs food (in any case), asks user for the purchases in that category and totals the expenditure    
  elif category.upper() == "TRANSPORTATION":
    purchase = input("\nPlease input a purchase amount. If you have entered all of your purchases, press 'enter': ")
    while purchase != "":
      totalPurchases += int(purchase)
      purchase = input("\nPlease input a purchase amount. If you have entered all of your purchases, press 'enter': ")
      transportPurchases = totalPurchases
    print("\nYou spent $%d on %s" % (totalPurchases, category))
# Asks user if they want to continue entering purchases in which case the loop repeats 
  done = input("\nAre you done entering purchases for all your categories? \"Yes or \"No\": ")
  if done.upper() == "YES":
    inputting = False

totalSpending = foodPurchases + entertPurchases + transportPurchases
print("\nTotal Spending = %d " %totalSpending)


# -------- PART 3: TOTAL SPENDING & OVER/UNDER CALCULATIONS--------

# Determine if a category’s spending is over or under budget. Calculate the amount that is over/under budget and print out results.
if foodBudget > foodPurchases:  # money left over!
    surplusFood = foodBudget - foodPurchases
    print("\nYou have " + str(surplusFood) + " left in your Food Budget!")
else:
    excessFood = foodPurchases - foodBudget  # went over budget!
    print("You exceeded your Food Budget by " + str(excessFood) + "!")

if entertBudget > entertPurchases: # money left over!
    surplusEntert = entertBudget - entertPurchases
    print("You have " + str(surplusEntert) + " left in your Entertainment Budget!")
else:
    excessEntert = entertPurchases - entertBudget  # went over budget!
    print("You exceeded your Entertainment Budget by " + str(excessEntert) + "!")

if int(transportBudget) > int(transportPurchases):  # money left over!
    surplusTransport = int(transportBudget) - int(transportPurchases)
    print("You have " + str(surplusTransport) + " left in your Transportation Budget!")
else:
    excessTransport = int(transportPurchases) - int(transportBudget)  # went over budget!
    print("\nYou exceeded your Transportation Budget by " + str(excessTransport) + "!")

# ------------------------------------------------------------------------
# :)