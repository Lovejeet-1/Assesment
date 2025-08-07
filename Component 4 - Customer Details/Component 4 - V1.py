""""
Customer Details Form
"""

with open("Customer_details.txt",'w') as file: 
    for i in range (10):
        Full_name = input("What is your full legal name? ").title()
        file.write(Full_name + ", ")
        Location = input("What is your current country of residence? ").title()
        file.write(Location + "\n")
        Location = input("What is your current country of residence? ").title()
        file.write(Location + "\n")
    