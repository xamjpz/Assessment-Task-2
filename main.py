 
#Modules

import pandas as pd
import matplotlib.pyplot as plt

#Global Variables
quit = False

#Data Frames for every request

ogdb = pd.read_csv("smoking_original.csv")

cldb = pd.read_csv("smoking.csv",
                    header=None,
                    names=['Year','Average Smoked', 'Percent of Male', 'Percent of Female', 'Percent of Total Population', 'Total Smokers', 'Total Males', 'Total Females'])

#Important Functions

#prints the whole original database
def originaldata():
        ogdb = pd.read_csv('smoking_original.csv', on_bad_lines='warn', encoding='ISO-8859-1' )
        with pd.option_context('display.max_rows', None,
                       'display.max_columns', None,
                       'display.width', None,
                       'display.precision', 3,
                       'display.colheader_justify', 'left'):
           print(ogdb)

#prints the cleaned database
def smokingdata():
    print(cldb)

#prints the sum of every person to ever smoke
def three(): 
    a = cldb['Total Smokers'].sum()
    print(f"The total amount of people to ever smoke is {a} people")

#prints the column of choice that the user chooses
def four():
    column_of_choice = input('Choose a column: ')
    if column_of_choice in cldb.columns:
        result = cldb[column_of_choice]
        print(result)
    else:
        print(f"The column {column_of_choice} is not a column in the DataFrame.")

#prints a comparison of the percent of male smokers from 1980 - 2012
def five():
        cldb.plot(
            kind='bar',
            x='Year',
            y='Percent of Male',
            color='blue',
            alpha=0.3,
            title='Comparison of Percent of Male Smokers')
        plt.show()
    
#prints a comparison of the percent of female smokers from 1980 - 2012
def six():
        cldb.plot(
            kind='bar',
            x='Year',
            y='Percent of Female',
            color='red',
            alpha=0.3,
            title='Comparison of Percent of Female Smokers')
        plt.show()

#function for the main program. It prints a guide for the user to read to help navigate the UI.
def useCases():
    global quit

    print("""This UI will tell you almost everything you want to know about the trends of smoking between the yars 1980 and 2012
          

    Choose from the functions on what you'd like to learn about:

    Basic Functions:

    1. Show the original dataset
    2. Show the updated Data Frame of just Australia
    3. Show the total amount of smokers across the world from 1980 - 2012 

    Advanced Functions:
            
    4. Choose a column to display the information. You can choose from these options: Year, Average Smoked, Percent of Male, Percent of Female, Percent of Total Population, Total Smokers, Total Males, Total Females
    5. To display the Percent of Male Smokers accross the years
    6. To display the Percent of Female Smokers accross the years
            
    7. Quit - Quit Program
          """)
    
    try:
        please = int(input("Choose function: "))

        if please == 1:
            originaldata()
        elif please == 2:
            smokingdata()
        elif please == 3:
            three()
        elif please == 4:
            four()
        elif please == 5:
            five()
        elif please == 6:
            six()
        elif please == 7:
            print("Thank you for using my User Interface goodbye :)")
            quit = True
        else:
            print("Try again, pick a number between 1-7.")
            
    except:
        print("Try entering a number between 1-7 instead of whatever you entered.")
        

#Main Program

while not quit:
    useCases()




