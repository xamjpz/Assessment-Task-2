 
import pandas as pd
import matplotlib.pyplot as plt

#Global Variables?
quit = False

#Data Frames for every request

ogdb = pd.read_csv("smoking_original.csv")

cldb = pd.read_csv("smoking.csv",
                    header=None,
                    names=['Year','Average Smoked', 'Percent of Male', 'Percent of Female', 'Percent of Total Population', 'Total Smokers', 'Total Males', 'Total Females'])


#Important Functions
def originaldata():
    print(ogdb)

def smokingdata():
    print(cldb)

def three(): 
    a = cldb['Total Smokers'].sum()
    print(f"The total amount of people to ever smoke is {a} people")

#need help with this 

def four():
    year_of_choice = input('Choose a year: ')
    if year_of_choice in cldb.columns:
        result = cldb[year_of_choice]
        print(result)
    else:
        print(f"The year {year_of_choice} is not a column in the DataFrame.")


        
def five():
        cldb.plot(
            kind='bar',
            x='Year',
            y='Percent of Male',
            color='blue',
            alpha=0.3,
            title='test')
        plt.show()
    
def six():
        cldb.plot(
            kind='bar',
            x='Year',
            y='Percent of Female',
            color='red',
            alpha=0.3,
            title='test')
        plt.show()



def useCases():
    global quit

    print("""This UI will tell you almost everything you want to know about the trends of smoking between the eyars 1980 and 2012
          
    It's interactive so you can get the most out of it as you can.

    Choose from the functions on what you'd like to learn about:

    Basic Functions:

    1. Show the original dataset
    2. Show the updated Data Frame of just Australia
    3. Show the total amount of Australian smokers from 1980 - 2012 

    Advanced Functions:
            
    4. Year:(YYYY) - Show coloumn of information for just that year
    5. Visualise_total - Visualise the total smoking trends between two genders
    6. W male
            
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
            print("put your function here")
            quit = True
        else:
            print("Try again")
            

    except:
        print("smt")
        

#Main Program

while not quit:
    useCases()




