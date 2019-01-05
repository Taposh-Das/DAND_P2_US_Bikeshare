import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')

    month = "all"
    day = "all"
    while True:
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
        city = input("Would you like to see data for Chicago, New York or Washington?\n")
        city=city.title()
        if city != "Chicago" and city != "New York" and city != "Washington":
            print("\nYou must choose one city or restart the program if you don't want to continue")
        else:
            while True:
    # get user input for month (all, january, february, ... , june)
                month_or_day = input("\nWould you like to filter your data based on month, day or not at all? Type 'none' if you don't want to add time filter.\n")
                month_or_day = month_or_day.lower()#REVW 1
                if month_or_day == "month":
                    month = input("\nEnter name of the month\n").lower()
                    if month=="january" or month=="february" or month=="march" or month=="april" or month=="may" or month=="june" or month=="july" or month=="august" or month=="september" or month=="october" or month=="november" or month=="december":
                        break
                    else:
                        print("\nInvalid month name was given. Please give correct month name next time.")
    # get user input for day of week (all, monday, tuesday, ... sunday)
                elif month_or_day == "day":
                    day = input("\nFor which day of the week would you like to see the data? Type full name of day or type 'all' for all days of the week.\n")
                    day = day.title()#REVW 1
                    if day=="Monday" or day=="Tuesday" or day=="Wednesday" or day=="Thursday" or day=="Friday" or day=="Saturday":
                        break
                    else:
                        print("\nInvalid name of day was given. Please give correct name of day next time.")
                elif month_or_day == "none":
                    break
            break

    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    fileName=""
    if city == 'Chicago':
        fileName ='chicago.csv'
    elif city == 'New York':
        fileName = 'new_york_city.csv'
    elif city == 'Washington':
        fileName = 'washington.csv'

    df = pd.read_csv(fileName)#my comment fileName is name of csv file based on user city input

    # my comment convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    # my comment extract month from the Start Time column to create a month column
    df['month'] = df['Start Time'].dt.month
    # my comment extract day of week from the Start Time column to create a day_of_week column
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    # my comment extract hour from the Start Time column to create a hour column
    df['hour'] = df['Start Time'].dt.hour

    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1
        #print(month)

        # filter by month to create the new dataframe
        df = df[df.month==month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df.day_of_week == day.title()]
    #df = df.loc[(df['column_name'] == some_value) & df['other_column'].isin(some_values)]
    #df = df.loc[(df['month'] == month) & (df['day_of_week'] == day)]
    #testing if filter works by printing df
    #print(df)
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    months = ['january', 'february', 'march', 'april', 'may', 'june']
    popular_month = months[df['month'].mode()[0]-1]
    print("Poplular month for traveling: ",popular_month.title())

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

    # display the most common day of week
    popular_day = df['day_of_week'].mode()[0]
    print("Poplular day of week for traveling: ",popular_day)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

    # display the most common start hour
    popular_hour = df['hour'].mode()[0]
    print("Poplular hour for traveling: ",popular_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station


    # display most commonly used end station


    # display most frequent combination of start station and end station trip


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time


    # display mean travel time


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types


    # Display counts of gender


    # Display earliest, most recent, and most common year of birth


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
