


# Highest score is 120
# This will be the questions that will be asked

# function for some yes no problems
# This function takes the Yes/No options and correctly outputs the numerical that is assoated with the excel sheet
"""
Creation Date:      6/4/2018
Original Author:    Christian Brenner, Matt Salvo, BMCS
Version Author:
Version:            0.4.3
Version Date:
"""


####################
# RETRIVE EXTERNAL #
####################
import os
os.system('cls')
print(">Installing/Verifying Libraries")
os.system('pip install pandas numpy xlsxwriter xlrd')
print(">Installing/Verifying completed")
os.system('cls')


######################
# EXTERNAL LIBRARIES #
######################
# import re
# import pandas as pd
# import numpy as np
# import xlsxwriter


####################
# GLOBAL VARIABLES #
####################
runt = 0
rcount = 1
likelyhood_final = 0
impact_score = 0
xchart = 0
ychart = 0
infoarr = []
a = 1
zero = []
one = []
two = []
three = []
four = []
five = []
six = []
seven = []
eight = []
nine = []
ten = []
eleven = []
twelve = []
thirteen = []
fourteen = []
fifteen = []
sixteen = []
seventeen = []
eighteen = []
nineteen = []
twenty = []
twenty_one = []
twenty_two = []
twenty_three = []
twenty_four = []
save = []
systemlist = []
arr = []
#############
# FUNCTIONS #
#############

###>- CHECK INPUT VALIDATION -<###          INOUT REFERENCE / OUTPUT SCORE
def check_zero(prompt, highest):
    # =============
    # VARIABLES
    # =============
    "SET GLOBAL"
    "SET STRINGS"
    "SET INT'S"
    "SET MARTIX/LIST"
    # =============
    # PROCESS
    # =============
    while True:
        try:
            value = int(input(prompt))
        except ValueError:
            print("Sorry, that input is not valid")
            continue
        if (value > highest) or (value < 0):
            print("Please enter a correct answer")
        else:
            break
    return value

###>- PLOTS SCORE ON [x,y] GRAPH -<###       INPUT NUM, NUM2 / OUTPUT ARR , ARR2
def scorefunction(num, num2):


    #=============
    # VARIABLES
    #=============
    "SET GLOBAL"
    global xchart
    global ychart
    "SET STRINGS"
    "SET INT'S"
    y = num
    x = num2
    "SET MARTIX/LIST"

    # =============
    # PROCESS
    # =============
    # Assigning the correct value to the Likelihood score.
    if y <= 10:                       # If 10 or less Very Low is assigned
        ychart = 0
    if y in range(11, 41):            # If 11 - 40 Low is assigned
        ychart = 1
    if y in range(40, 61):            # If 40-60 Moderate
        ychart = 2
    if y in range(60, 91):            # 60-90 is High
        ychart = 3
    if y in range(91, 125):           # 91 to anything else is Very High
        ychart = 4

    # Assigning the correct risk to the Impact
    if x == 0:                        # An Score of 0 equates to a Very Low Score
        xchart = 0
    if x == 1:                        # 1 = Low
        xchart = 1
    if x == 2:                        # 2 for Moderate
        xchart = 2
    if x == 3:                        # 3 for High
        xchart = 3
    if x == 4:                        # 4 for Very High. // No Score Higher than 4 is possible.
        xchart = 4


###>- If Answers are 5 point higher than needed this fuction corrects that -<###         INPUT: num / OUTPUT: num
def maths(num):
    #=============
    # VARIABLES
    #=============
    "Set Global"
    global runt
    "Set Strings"
    "Set Int's"
    "Set Martix/list"
    #=============
    # PROCESS
    #=============
    "Testing num for a given value"
    num -= 1
    if (num == 2):
        num = 0
    # else:
    #     print('NOPE')
    # # END IF:ELSE
    # "End Function"
    return num


###>- CALCULATES LIKELY HOOD SCORE -<###         INPUT NUM / OUTPUT SCORE
def likelyhood(num):
    #=============
    # VARIABLES
    #=============
    "SET GLOBAL"
    "SET STRINGS"
    "SET INT'S"
    "SET MARTIX/LIST"
    # =============
    # PROCESS
    # =============
    # TAKES THE INPUT AND * 5 TO IT FOR A CORRECT SCORE
    score = num * 5
    return score


###>- GATHERS THE BASIC STRING INFO FOR THE SYSTEM -<###        INPUT NONE / OUTPUT ARR
def basicInfo():

    # =============
    # VARIABLES
    # =============
    "SET GLOBAL"                            # Asking the user basic questions for referencing the system
    global systemlist
    "SET STRINGS"                           # being tested at the time.
    "SET INT'S"
    "SET MARTIX/LIST"

    # =============
    # PROCESS
    # =============

    system_name = input('Enter System Name: ')
    print(" ")

    system_description = input(' Enter System Description: ')
    print(" ")

    system_status = check_int("Please Chose the corresponding number for your system status: \n1.Pre-Milestone "
                              "\n2.LIRP \n3.Full Rate Production \n4.Sustainment \nChoice: ", 4)
    if system_status == 1:
        system_status = str('Pre-Milestone')
    if system_status == 2:
        system_status = str('LIRP')
    if system_status == 3:
        system_status = str('Full Rate Production')
    if system_status == 4:
        system_status = str('Sustainment')
    print(" ")

    authorizing_official = input('Please enter Authorizing Official: ')
    print(" ")

    service_branch = check_int("Please Select Branch: \n1.Army \n2.Navy \n3.Air Force \nChoice: ", 3)
    if service_branch == 1:
        service_branch = str('Army')
    if service_branch == 2:
        service_branch = str('Navy')
    if service_branch == 3:
        service_branch = str('Air Force')
    print(" ")

    data_classification = check_int("Please Select Data Classification: "
                                    "\n1.U \n2.S \n3.TS \nChoice: ", 3)
    if data_classification == 1:
        data_classification = str('Unclassified')
    if data_classification == 2:
        data_classification = str('Secret')
    if data_classification == 3:
        data_classification = str('Top Secret')

    print(" ")
    # arr is used for output and storage.
    arr.append(system_name)
    arr.append(system_status)
    arr.append(authorizing_official)
    arr.append(service_branch)
    arr.append(data_classification)
    arr.append(system_description)
    systemlist.append(system_name)
    return arr


###>- GATHERS THE IMPACT SCORE -<###            INPUT NONE / OUTPUT SCORE
def impact():
    # =============
    # VARIABLES
    # =============
    "SET GLOBAL"
    global arr
    "SET STRINGS"
    "SET INT'S"
    "SET MARTIX/LIST"

    # =============
    # PROCESS
    # =============

    # Checking one section of the impact score.
    mic = check_int("Please Enter Mission Impact if Compromised: \n5.Very High \n4.High \n3.Moderate \n2.Low "
                    "\n1.Very Low \nChoice: ", 5)                           # Input Validation
    mic -= 1
    score = mic
    # Checking other
    isc = check_int("Please Enter Impact to the System if Compromised: \n5.Very High \n4.High \n3.Moderate \n2.Low "
                    "\n1.Very Low \nChoice: ", 5)                        # Input Validation
    isc -= 1
    if score <= isc:        # Comparing scores and using the higher value for the risk
        score = isc
    return score


###>- GATHERS THE BASE SCORE FOR LIKELYHOOD FOR RISK -<###          INPUT RUNT / OUTPUT LIKELY, IMPACT_SCORE
def likelyhood_score():
    # =============
    # VARIABLES
    # =============
    "SET GLOBAL"
    global impact_score
    global runt
    "SET STRINGS"
    "SET INT'S"
    answer = 0          # only used to clear any possible data in the var
    "SET MARTIX/LIST"

    # =============
    # PROCESS
    # =============



    connectivity = check_int("Please Select connectivity to the internet: \n1.Open Network - Commercial ISP "
                             "\n2.Open Network - .edu  "
                             "\n3.Open Network - NIPR  "
                             "\n4.Closed Restricted Network - SIPRNET  "
                             "\n5.Closed Restricted Network - JWICS  "
                             "\n6.Closed Restricted Network - SAP/SAR  "
                             "\n7.Closed Restricted Network - Other  "
                             "\n8.Standalone Network  "
                             "\n9.Standalone System - With Media  "
                             "\n10.Standalone System - No Media"
                             "\nChoice: ", 10)
    print(" ")
    connectivity = 10 - connectivity
    runt += connectivity

    system_fielded = check_int("Please select how many systems are fielded: "
                               "\n1.1-10  "
                               "\n2.11-50  "
                               "\n3.51-100  "
                               "\n4.101-500  "
                               "\n5.501+ "
                               "\nChoice: ", 5)
    print(" ")
    runt += system_fielded

    email = check_zero("Are users able to email?: "
                      "\n1.Yes  "
                      "\n0.No "
                      "\nChoice: ", 1)
    print(" ")
    runt += email

    web = check_zero("Are users able to use a web browser?: "
                    "\n1.Yes  "
                    "\n0.No "
                    "\nChoice: ", 1)
    print(" ")
    runt += web

    admin_privileges = check_int("What kind of users are logged on as?: "
                                 "\n1.User "
                                 "\n2.Admin - Partial privileges "
                                 "\n3.Admin - Elevated privileges "
                                 "\n4.Does not Apply"
                                 "\nChoice: ", 4)
    print(" ")
    admin_privileges -= 1
    if admin_privileges == 3:
        admin_privileges = 0

    runt += admin_privileges

    tfa = check_int("Does the system have PIK or TFA?: "
                    "\n1.Yes "
                    "\n2.No "
                    "\n3.Does not Apply"
                    "\nChoice: ", 3)
    # corrects for the number 3 choice due to maths function.
    print(" ")
    tfa = maths(tfa)
    runt += tfa

    app_whitelist = check_int("Use a App whitelisting capability?: "
                              "\n1.Yes "
                              "\n2.No "
                              "\n3.Does not Apply"
                              "\nChoice: ", 3)
    print(" ")
    app_whitelist = maths(app_whitelist)
    runt += app_whitelist

    host_protection = check_int("Uses Host Based Protection?: "
                                "\n1.Yes "
                                "\n2.No"
                                "\nChoice: ", 2)

    print(" ")
    host_protection = maths(host_protection)
    runt += host_protection

    hard_ports = check_int("Are the unused ports (Ethernet/USB) disabled on the system?: "
                           "\n1.Yes  "
                           "\n2.No"
                           "\nChoice: ", 2)
    print(" ")
    hard_ports = maths(hard_ports)
    runt += hard_ports

    stigs = check_int("Have any STIGs been run on the system?: "
                      "\n1.Yes  "
                      "\n2.No  "
                      "\nChoice: ", 2)
    print(" ")
    stigs = maths(stigs)
    runt += stigs

    encryption = check_int("Is encryption at rest?: "
                           "\n1.Yes  "
                           "\n2.No  "
                           "\nChoice: ", 2)
    print(" ")
    encryption = maths(encryption)
    runt += encryption

    'This is commented out until further notice'
    # owner = input('System Owner Approval Justification Discussion: ')
    #
    # system_ato_date = input('Please enter System ATO Date in MM/DD/YYYY Format: ')
    #
    # anticipated_ato_date = input("Please Enter Anticipated ATO Date in MM/DD/YYYY Format: ")
    #
    impact_score = impact()
    #
    # print('Additional Testing: Please leave this section blank')

    testing = check_int("Has any Testing been complected?: "
                        "\n1.Yes - Vulnerability  \n2.Yes - Penetration  \n3. Yes - Adversary  \n4.No: "
                        "\nChoice: ", 4)
    print(" ")
    # Make a negative number out of the Choice selected
    if testing == 4:
        testing = 0
    else:
        testing = testing * -5
    runt += testing


    # funding = int(input('Is Funding Available: '
    #                     '\n1.Yes  \n2.No  \n0.Does Not Apply \nChoice : '))
    # funding -= 1
    # if (funding == 1) or (funding == 0):
    #     when_funding = input('When will funding be available?: (Please enter in MM/DD/YYYY format)')
    # runt += funding // Funding should not effect the likely hood score

    answer = likelyhood(runt)
    runt = 0                    # Clears runt for any future systems that you would like to include
    return answer


###>- PLOTS LIKELYHOOD AND IMPACT ON A 23 FLAT DATA LIST
def plot(xval, yval):
    # =============
    # VARIABLES
    # =============
    "SET GLOBAL"
    global zero
    global one
    global two
    global three
    global four
    global five
    global six
    global seven
    global eight
    global nine
    global ten
    global eleven
    global twelve
    global thirteen
    global fourteen
    global fifteen
    global sixteen
    global seventeen
    global eighteen
    global nineteen
    global twenty
    global twenty_one
    global twenty_two
    global twenty_three
    global twenty_four
    global a
    "SET STRINGS"
    "SET INT'S"
    "SET MARTIX/LIST"
    # =============
    # PROCESS
    # =============

    """ Plotting the risk of the the system for a 5x5. This can be outputted in CL or to an excel sheet. """

    b = 'R' + str(rcount)
    if xval == 0:
        if yval == 4:
            zero.append(b)
        if yval == 3:
            five.append(b)
        if yval == 2:
            ten.append(b)
        if yval == 1:
            fifteen.append(b)
        if yval == 0:
            twenty.append(b)
    if xval == 1:
        if yval == 4:
            one.append(b)
        if yval == 3:
            six.append(b)
        if yval == 2:
            eleven.append(b)
        if yval == 1:
            sixteen.append(b)
        if yval == 0:
            twenty_one.append(b)
    if xval == 2:
        if yval == 4:
            two.append(b)
        if yval == 3:
            seven.append(b)
        if yval == 2:
            twelve.append(b)
        if yval == 1:
            seventeen.append(b)
        if yval == 0:
            twenty_two.append(b)
    if xval == 3:
        if  yval == 4:
            three.append(b)
        if yval == 3:
            eight.append(b)
        if yval == 2:
            thirteen.append(b)
        if yval == 1:
            eighteen.append(b)
        if yval == 0:
            twenty_three.append(b)
    if xval == 4:
        if yval == 4:
            four.append(b)
        if yval == 3:
            nine.append(b)
        if yval == 2:
            fourteen.append(b)
        if yval == 1:
            nineteen.append(b)
        if yval == 0:
            twenty_four.append(b)
    print(zero, one, two, three, four)
    print(five, six, seven, eight, nine)
    print(ten, eleven, twelve, thirteen, fourteen)
    print(fifteen, sixteen, seventeen, eighteen, nineteen)
    print(twenty, twenty_one, twenty_two, twenty_three, twenty_four)


###>- CHECKS INPUT VALIDATION FOR ALL ENTRYS THAT INCLUDE INTS -<###        INPUT PROMPT / OUTPUT VALUE
def check_int(prompt, highest):
    while True:
       try:
           value = int(input(prompt))
       except ValueError:
           print("Sorry, that input is not valid")
           continue
       if (value > highest) or (value < 1):
           print("Please enter a correct answer")
       else:
           break

    return value


###>- OUTPUTS FINAL INFORMATION TO THE USERS _-<###             INPUT INFOAAR[] / OUTPUT N/A UI
def output():

    # =============
    # VARIABLES
    # =============
    "SET GLOBAL"
    global impact_score
    global likelyhood_final
    global infoarr
    global xchart
    global ychart
    "SET STRINGS"
    "SET INT'S"
    "SET MARTIX/LIST"

    # =============
    # PROCESS
    # =============

    #arr = [system_name, system_status, authorizing_official, service_branch, Rationale_for_waiver, Data_classification]
    print('')
    print('Here are your results!')
    print('System Name: ' + infoarr[0])
    print('System Description: ' + infoarr[5])
    print('System Status: ' + infoarr[1])
    print('Authorizing Official: ' + infoarr[2])
    print('Service Branch: ' + infoarr[3])
    print('Data Classification: ' + infoarr[4])
    print('')
    print('Your system risk score is as follows.\n')
    #print('Y-Value: ' + ychart)

###>- MENU for Text UI. Main is run within MANU -<###           INPUT NA / OUTPUT N/A
def menu():
    print("This is a Risk Scoring Tool\n")
    print(" ")
    while True:
        try:
            choice = str(input('Would you like to enter system information?: \nY/N: '))

        except ValueError:
            print("Sorry, That input is not valid")
            continue
        if (choice == "y") or (choice == "Y"):
            main()
        elif (choice == "n") or (choice == "N"):
           # print("Thank you for using the program")
            break
    while True:
        try:
            secondchoice = str(input('Would you like to view a systems information you entered?: \n Y/N: '))
        except ValueError:
            print("Sorry, that is not valid")
        if (secondchoice == "y") or (secondchoice == "Y"):
            save()
        elif (secondchoice == "n") or (secondchoice == "N"):
            print("Thank you for using the program. All data will be lost if not exported.")
            break
    quit()


def save():
    # =============
    # VARIABLES
    # =============
    "SET GLOBAL"        # Asking the user basic questions for referencing the system
    global arr
    global systemlist
    "SET STRINGS"                           # being tested at the time.
    "SET INT'S"
    numtemp = 1
    "SET MARTIX/LIST"

    # =============
    # PROCESS
    # =============

    # List Systems
    temp = len(systemlist)
    print("Please select system.: ")
    for x in range(0, temp):
        print(numtemp, systemlist[x])
        numtemp += 1

    choisetemp = int(input("Select Here: "))
    # check data entry here
    # need if statements for 1
    answers = ["System Name: ", "System Status: ", "Authorizing Official: ", "Branch: ", "Data Classification: ",
               "Description: ", "Impact Score: ", "LikelyHood Score: "]

    choisetemp *= 8
    choisetemp -= 8
    finaltemp = choisetemp + 8
    test = 0
    print(" ")
    for x in range(choisetemp, finaltemp):
         print(answers[test])
         print(arr[x])
         print(" ")
         test += 1

def main():

    global impact_score
    global likelyhood_final
    global runt
    global infoarr
    global xchart
    global ychart
    global rcount
    # basicinfo()
    # likelyhood_final = likelyhood_score()
    # scorefunction(likelyhood_final, impact_score)       #return

    infoarr = basicInfo()
    likelyhood_final = likelyhood_score()
    arr.append(impact_score)
    arr.append(likelyhood_final)
    scorefunction(likelyhood_final, impact_score)
    output()
    plot(xchart, ychart)
    print("Impact ", impact_score)
    print("LikelyHood ", likelyhood_final)
    rcount += 1
    return 0


menu()





