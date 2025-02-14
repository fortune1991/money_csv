import datetime
from project_classes import User, Vault, Pot, Transaction
from project_functions import submit_transaction, print_slow, int_validator, collect_date, summary, create_pot, create_user, create_vault
from time import sleep

def main():

    print_slow("""

Welcome to Money Pots, your savings and budgeting calculator.

In this program, your savings are organized into two categories: Vaults and Pots.

- A Vault is a collection of Pots, each assigned a specific time frame.
- A Pot represents an individual budget within a Vault.

For example, between 17/03/25 and 17/01/26, you might create a 'Travelling' Vault
to manage your holiday expenses. This Vault could contain multiple Pots, each
representing a budget for a different destination.

Once you've set up your Vaults and Pots, the program will enter an infinite loop
where you can choose from three options:

1. Submit a transaction – Transactions are linked to a specific Pot and either 
increase or decrease its balance, depending on the selected type.
2. View a summary – This provides an updated overview of your Vaults and Pots, 
reflecting any transactions you've made.
3. Exit the program – A final summary of your balances will be displayed before 
the program closes.

Please note: This program does not store data permanently. Once you exit, all 
Vault and Pot data will be lost.

We hope you enjoy using Money Pots!
    """)
    
    # Create a User object
    print()
    user = create_user()

    # Create a Vault object with valid data
    print_slow(f"Hi {user.username}, let me help you create some vaults. How many do you want to create?: ")
    no_vaults = int_validator()
    vaults = {}
    
    try:
        for x in range(0, no_vaults):
            print(f"Vault {x+1}")
            vaults["vault_{0}".format(x)] = create_vault(x, user)
    
    except ValueError as e:  
        print(f"Error: {e}")

    except Exception as e:  
        print(f"An unexpected error occurred: {e}")

    # Create Pot objects with valid data
    print_slow("Now, let me help you create some pots. How many do you want to create?: ")
    no_pots = int_validator()
    pots = {}
    
    while True:
        try:
            for x in range(0, no_pots):
                print(f"Pot {x+1}")
                print()
                
                while True: 
                    print_slow("What vault should this pot be assigned to?: ")
                    vault_input = input()

                    # Find the vault using a simple loop
                    selected_vault = None
                    for vault in vaults.values():
                        if vault.vault_name == vault_input:
                            selected_vault = vault
                            break

                    if selected_vault:
                        pots[f"pot_{x}"] = create_pot(x, selected_vault)
                        break
                    else:
                        print(f"Vault '{vault_input}' not found. Please enter a valid vault name.")
                        print()
            break
        
        except ValueError as e:  
            print(f"Error: {e}")
            print()

        except Exception as e:  
            print(f"An unexpected error occurred: {e}")
            print()

    # Summary of the vaults and pots values
    print_slow("See below list of vaults and their summed values")
    print()
    summary(vaults, pots)
    print()
    
     # Loop until exit

    while True:
        print_slow('Now, I await your commands to proceed. Please type: \n\n "Transaction" to submit a new transaction, \n "Summary" to get a report of vault/pot values, or \n "Exit" to terminate the programme')
        print()
        print()
        action = input()
        print()

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

        # Exit

        elif action == "Exit":
            print_slow("OK, the program will now terminate. See final values of the vaults and pots below. Thanks for using Money Pots!")
            print()
            summary(vaults,pots)
            print()
            exit()

        else:
            print_slow("Invalid command. Please try again")
            print()
        
        

if __name__ == "__main__":
    main()