import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }
df = pd.read_csv(CITY_DATA[city])

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
     city =''
    while True:
        city = input('Enter the City : chicago,new york city,washington:').lower()
        if city in CITY_DATA:
            print ('valid')
            break
        else:
            print('invalid')
            continue


    # TO DO: get user input for month (all, january, february, ... , june)
    month = ''
    month = input('Enter the month:')

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    day = ''
    day = input('Enter the day:')

    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    df = pd.read_csv(CITY_DATA[city])
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """


    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    

    # TO DO: display the most common month
    df['month'] = df['Start Time'].dt.month
    popular_monthday = df['month'].mode()


    # TO DO: display the most common day of week
     df['day_of_week'] = df['Start Time'].dt.weekday_name
     popular_weekday = df['day_of_week'].mode()   
    


    # TO DO: display the most common start hour
    df['hour'] =df['Start Time'].dt.hour
    popular_hour = df['hour'].mode()

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    popular_startstation = df['Start Station'].mode()


    # TO DO: display most commonly used end station
    popular_endstation = df['End Station'].mode()


    # TO DO: display most frequent combination of start station and end station trip


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time = df['Trip Duration'].sum()


    # TO DO: display mean travel time
    mean_travel_time = df['Trip Duration'].mean()

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types = df['User Type'].value_counts()
    print('user_types')


    # TO DO: Display counts of gender
    Gender = df['Gender'].value_counts()
    print('Gender')


    # TO DO: Display earliest, most recent, and most common year of birth
    earliest = df['Birth Year'].max()
    print(earliest)
    most recent = df['Birth Year'].min()
    print(most recent)
    most common year of birth = df['Birth Year'].mode()
    print(most common year of birth)
    


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
