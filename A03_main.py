"""
Description: A client program written to verify implementation 
of the Observer Pattern.
"""
__author__ = "ACE Faculty"
__version__ = "1.0.0"
__credits__ = "Dylan Kaspick"

# 1.  Import all BankAccount types using the bank_account package
#     Import date
#     Import Client

import bank_account
from datetime import date
from client.client import Client

# 2. Create a Client object with data of your choice.

client = Client(12345, "Dylan", "Kaspick", "dylan@rrc.ca")

# 3a. Create a ChequingAccount object with data of your choice, using the client_number 
# of the client created in step 2.
# 3b. Create a SavingsAccount object with data of your choice, using the client_number 
# of the client created in step 2.

chequing_account = bank_account.ChequingAccount(22, 12345, 500.0, date.today(), -100.0, 0.05)

savings_account = bank_account.SavingsAccount(24, 12345, 1200.0, date.today(), 200.0)

# 4 The ChequingAccount and SavingsAccount objects are 'Subject' objects.
# The Client object is an 'Observer' object.  
# 4a.  Attach the Client object (created in step 1) to the ChequingAccount object (created in step 2).
# 4a.  Attach the Client object (created in step 1) to the SavingsAccount object (created in step 2).

chequing_account.attach(client)
savings_account.attach(client)

# 5a. Create a second Client object with data of your choice.
# 5b. Create a SavingsAccount object with data of your choice, using the client_number 
# of the client created in this step.

beta_client = Client(321, "Jon", "Wick", "wickj@rrc.ca")

beta_savings_account = bank_account.SavingsAccount(64, 321, 10000.0, date.today(), 200.0)

# 6. Use the ChequingAccount and SavingsAccount objects created 
# in steps 3 and 5 above to perform transactions (deposits and withdraws) 
# which would cause the Subject (BankAccount) to notify the Observer 
# (Client) as well as transactions that would not 
# cause the Subject to notify the Observer.  Ensure each 
# BankAccount object performs at least 3 transactions.
# REMINDER: the deposit() and withdraw() methods can raise exceptions
# ensure the methods are invoked using proper exception handling such 
# that any exception messages are printed to the console.

chequing_account.deposit(12000)
chequing_account.withdraw(12451)
chequing_account.deposit(50)

savings_account.deposit(12000)
savings_account.withdraw(13190)
savings_account.deposit(50)

beta_savings_account.deposit(1200000)
beta_savings_account.withdraw(100000)
beta_savings_account.deposit(50)
