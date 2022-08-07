from datetime import timedelta
import time
import pandas as pd

# create dictionary with the name of relevant csv files.
CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

# create a list with city names found in the CITY_DATA dicitonary keys
CITIES = ', '.join(list(CITY_DATA.keys())).title()

# create a list with the optional MONTHS
MONTHS = ["All", "January", "February", "March", "April", "May", "June"]

# create a list with the optional DAYS
DAYS = ["All", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')

    # create empty city variable
    city = ''

    # loop until the variable city contains a valid city
    while city not in CITY_DATA.keys():
        # get user input for city (chicago, new york city, washington)
        city = input(f"\nWhich city do you want to explore ({CITIES}): ").lower()

        # display the chosen city
        print(f"You chose {city.title()}")

        # check if the inserted city is valid
        if city not in CITY_DATA.keys():
            # ask user to try again
            print(f"Ooops you can't choose {city}. Try again")

    # create empty month variable
    month = ''

    # loop until the variable month contains a valid month
    while month not in MONTHS:
        # get user input for month (all, january, february, ... , june)
        month = input(f"\nWhich month do you want to analyze? ({', '.join(MONTHS)}): ").title()

        # display the chosen month
        print(f"You chose {month}")

        # check if the inserted month is valid
        if month not in MONTHS:
            # ask user to try again
            print(f"Ooops you can't choose {month}. Try again")

    # create an empty day variable
    day = ''

    # loop until the variable day contains a valid day
    while day not in DAYS:
        # get user input for day of week (all, monday, tuesday, ... sunday)
        day = input(f"\nWhich day do you want to analyze? ({', '.join(DAYS)}): ").title()

        # display the chosen day
        print(f"You chose {day}")

        # check if the inserted day is valid
        if day not in DAYS:
            # ask user to try again
            print(f"Ooops you can't choose {day}. Try again")

    # print a line to seperate the output nicely
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
    # load date for the chosen city
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day_name()

    # filter by month if applicable
    if month != 'All':
        # use the index of the MONTHS list to get the corresponding int
        month = MONTHS.index(month)

        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of the week
    if day != 'All':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day]

    return df

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')

    # set start time of function
    start_time = time.time()

    # calculate the most common month
    common_month = df['month'].mode()[0]
    # display the most common month
    print(f"Most common month: {common_month}")

    # calculate the most common weekday
    common_weekday = df['day_of_week'].mode()[0]
    # display the most common day of week
    print(f"Most common weekday: {common_weekday}")

    # convert Start Time column to datetime
    df['hour'] = df['Start Time'].dt.hour

    # calculate the most common start hour
    common_start_hour = df['hour'].mode()[0]

    # display the most common start hour
    print(f"Most common start hour: {common_start_hour}")

    # calculate and display run time of function
    print("\nThis took %s seconds." % (time.time() - start_time))

    # print a line to seperate the output nicely
    print('-'*40)

def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Route...\n')

    # set start time of function
    start_time = time.time()

    # find most commonly used start station
    common_start_station = df['Start Station'].mode()[0]

    # display most commonly used start station
    print(f"Most common start station is: {common_start_station}")

    # find most commonly used end station
    common_end_station = df['End Station'].mode()[0]

    # display most commonly used end station
    print(f"Most common end station is: {common_end_station}")

    # combine start and end station to one new column: 'Start And End Station'
    df['Start And End Station'] = df['Start Station'] + " - " + df['End Station']

    # find most frequent combination of start station and end station trip
    common_start_to_end = df['Start And End Station'].mode()[0]

    # display most commonly used end statio
    print(f"Most common route is: {common_start_to_end}")

    # calculate and display run time of function
    print("\nThis took %s seconds." % (time.time() - start_time))

    # print a line to seperate the output nicely
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')

    # set start time of function
    start_time = time.time()

    # find total travel time
    tot_travel_time = df['Trip Duration'].sum()

    # display total travel time in hh:mm:ss-format
    print("\nThe total travel time is:")
    print(str(timedelta(seconds=int(tot_travel_time))))

    # find mean travel time
    mean_travel_time = df['Trip Duration'].mean()

    # display mean travel time in hh:mm:ss-format
    print("\nThe average travel time is:")
    print(str(timedelta(seconds=int(mean_travel_time))))

    # calculate and display run time of function
    print("\nThis took %s seconds." % (time.time() - start_time))

    # print a line to seperate the output nicely
    print('-'*40)

def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')

    # set start time of function
    start_time = time.time()

    # get counts of user types
    user_types = df['User Type'].value_counts()

    # display counts of user types
    print("\nCount of user types:")
    print(user_types.to_string())

    # get counts of gender
    gender = df['Gender'].value_counts()

    # display counts of gender
    print("\nCount of gender:")
    print(gender.to_string())

    # find earliest year of birth
    min_birth_year = int(df['Birth Year'].min())

    # find most recent year of birth
    max_birth_year = int(df['Birth Year'].max())

    # find most common year of birth
    common_birth_year = int(df['Birth Year'].mode()[0])

    # display earliest, most recent and most common year of birth
    print("\nBirth years:")
    print(f"Earliest year of birth: {min_birth_year}")
    print(f"Most recent year of birth: {max_birth_year}")
    print(f"Most common year of birth: {common_birth_year}")

    # calculate and display run time of function
    print("\nThis took %s seconds." % (time.time() - start_time))

    # print a line to seperate the output nicely
    print('-'*40)

def view_data(df):
    """Prompt the user whether they would like want to see the raw data."""

    # get user input for whether they want to see the raw data
    dataview = input("\nWould you like to view the raw data? Enter yes or no\n: ")

    # initialize start to 0
    start = 0

    # initialize end to 5
    end = 5

    # set display option to show all columns
    pd.set_option('display.max_columns', None)

    # check if user chose to see raw data
    if dataview.lower() == 'yes':
        # inform user that first five rows are shown
        print("Showing first five rows of data:")

        # display first five rows of data
        print(df[start:end])

    # loop as long as user input is yes
    while dataview.lower() == 'yes':
        # ask if the user want to view five more rows
        dataview = input("\nWould you like to view the next five rows? Enter yes or no\n: ")

        # increment start variable with 5
        start += 5
        # increment end variable with 5
        end += 5

        # check if dataset has reached the end
        if end - 5 > len(df.index):
            # inform that end of the data set is reached
            print("You reached the end of the data set")
            # return from the function
            break

        # check if the user wants to see more rows
        if dataview.lower() == 'yes':
            # display the next five rows
            print(df[start:end])
        elif dataview.lower() == 'no':
            # exit loop
            break
        else:
            # continue loop if input are not "yes" or "no"
            print("Wrong input. Please, try again.")
            dataview = 'yes'


def main():
    while True:
        try:
            # call get-filters() to get users input on city, month and day
            city, month, day = get_filters()

            # load data based on the chosen city, month and day
            df = load_data(city, month, day)

            # display the chosen filters from the users input
            print(f"\nFilters: {city}, {month}, {day}".title())

            # get time stats for chosen dataset
            time_stats(df)
            # get station stats for chosen dataset
            station_stats(df)
            # get trip duration stats for chosen dataset
            trip_duration_stats(df)
            # get time user stats for chosen dataset
            user_stats(df)

        # triggerd when a column can't be found in the data set
        except KeyError as ke:
            # inform the user that the data is not available
            print(f"\nNo data available for {ke}")

        # triggerd if the file of the chosen city can't be found
        except FileNotFoundError:
            # inform the user that the data for the chosen city is not found
            print(f"\nI am sorry. We are unable to reach the data for {city}.")

        # call function to view raw data of chosen dataset
        view_data(df)

        # ask if user want to restart the program
        restart = input('\nWould you like to restart? Enter yes or no.\n')

        # check if user answered yes to restart
        if restart.lower() != 'yes':
            # exit the loop
            break

if __name__ == "__main__":
    main()
