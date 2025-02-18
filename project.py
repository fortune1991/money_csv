import csv, datetime, os
from project_classes import User, Vault, Pot, Transaction
from project_functions import submit_transaction, print_slow, int_validator, collect_date, convert_date, summary, create_pot, create_user, create_vault, create_profile, instructions, re_vaults, re_pots, re_transactions
from time import sleep

def main():
    vaults = {}
    pots = {}
    transactions = {}
    
    file_exists = os.path.isfile("database/users.csv")
    if not file_exists:
        
        print_slow("""
Welcome to Money Pots, your savings and budgeting calculator.
        """)
        print_slow(instructions())
        
        user, vaults, pots = create_profile()
    
    if file_exists:
        while True:
            print_slow("""
Welcome to Money Pots, your savings and budgeting calculator. Let me help you to login and view your profile. What's your username?
    """)
            print()
            login = input().strip() # Remove trailing white space
            user_exists = False
            with open("database/users.csv", newline="") as f:
                user_reader = csv.DictReader(f)

                for row in user_reader:
                    if row['username'] == login:
                        user_exists = True
                        name = row['username']
                        
                if user_exists == True:
                    #reinstantiate user
                    user = create_user(name)

                    #reinstantiate vaults 
                    vaults, vault_ids = re_vaults(name, user)
                    
                    #reinstantiate pots
                    pots, pot_ids = re_pots(vaults, vault_ids)

                    #reinstantiate transactions
                    transactions, transaction_ids = re_transactions(pots, pot_ids)

                    # Update Pots and Vaults values

                    for pot in pots.values():
                        pot.pot_value()
                    
                    for vault in vaults.values():
                        vault.vault_value()

                    break

                else:
                    print()
                    print("User doesn't exist. Respond 'Try again' 'New user' or 'Exit'")    
                    print()

                    response = input()

                    if response == "New user":
                        print()
                        print("Excellent. Please answer the following questions to create a new user profile")
                        user, vaults, pots = create_profile()
                        break
                    elif response == "Try again":
                        continue
                    elif response == "Exit":
                        exit()
                    else:
                        print("Unknown Command. Please try to login again")                
     
     # Loop until exit

    while True:
        print_slow('Now, I await your commands to proceed. Please type: \n\n "Transaction" to submit a new transaction, \n "Summary" to get a report of vault/pot values, or \n "Instructions" to get a further information on how to use Money Pots \n "Exit" to terminate the programme')
        print()
        print()
        action = input()

        if action == "Transaction":
    
        # Submit Transactions

            print_slow("Excellent. Now, let me help you create a new transaction.")
            print()
            transactions = {}
            no_transactions = 1
            
            while True:
                try:
                    for x in range(no_transactions):
                        print(f"Transaction {x+1}")
                        print()
                        
                        while True: 
                            print_slow("What pot should this pot be assigned to?: ")
                            pot_input = input()

                            # Find the pot using a simple loop
                            selected_pot = None
                            for pot in pots.values():
                                if pot.pot_name == pot_input:
                                    selected_pot = pot
                                    break

                            if selected_pot:
                                transactions[f"transaction_{x+1}"] = submit_transaction(x+1, selected_pot)
                                selected_pot.pot_value()
                                break
                            else:
                                print(f"pot '{vault_input}' not found. Please enter a valid vault name.")
                                print()
                    break
                
                except ValueError as e:  
                    print(f"Error: {e}")
                    print()

                except Exception as e:  
                    print(f"An unexpected error occurred: {e}")
                    print()
            
            print()

        # Print Summary

        elif action == "Summary":

            summary(vaults, pots)
            print()

        elif action == "Instructions":
            print_slow(instructions())

        # Exit

        elif action == "Exit":
            print_slow("OK, the program will now terminate. See final values of the vaults and pots below. Thanks for using Money Pots!")
            print()
            summary(vaults, pots)
            print()
            exit()

        else:
            print_slow("Invalid command. Please try again")
            print()
        
        

if __name__ == "__main__":
    main()