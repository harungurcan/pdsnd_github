import time # This module provides various time-related functions. From https://docs.python.org/3/library/time.html
import pandas as pd
import numpy as np


info_cities= {"CHICAGO": "chicago.csv",
              "NEW YORK CITY": "new_york_city.csv",
              "WASHINGTON": "washington.csv"} # Information about cities are in what csv file

print("Greetings! Let us look into some data on bikeshare in the US!")
cities= ["CHICAGO", "NEW YORK CITY", "WASHINGTON"]
months= ["JANUARY", "FEBRUARY", "MARCH", "APRIL", "MAY", "JUNE"]
days= ["MONDAY", "TUESDAY", "WEDNESDAY", "THURSDAY", "FRIDAY", "SATURDAY", "SUNDAY"]

def find_city_month_day():
	while True:
		print("*"*80)
		city = input("What city you you would like to look into?\n..Choose one of them Chicago, New York City, or Washington.\n..Be careful about spelling. Using lowercase or capital letters are OK\n")
		city=city.upper()
		if city in cities:
			break
		else:
			print("Type it again. You should choose one of them Chicago, New York City or Washington with correct spelling")

	while True:
		print("*"*80)
		month=input("What month you would like to look into?\n..Choose one of them January, February, March, April, May, June or all.\n..Be careful about spelling. Using lowercase or capital letters are OK\n")
		month=month.upper()
		if month in months:
			break
		elif month=="ALL":
			break
		else:
			print("Type it again. You should choose one of them January, February, March, April, May, June or all with correct spelling")

	while True:
		print("*"*80)
		day=input("What specific day you would like to investigate?\n..Type one of them Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday or all.\n..Be careful about spelling. Using lowercase or capital letters are OK\n")
		day=day.upper()
		if day in days:
			break
		elif day=="ALL":
			break
		else:
			print("Type it again. You should choose one of them Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday or all with correct spelling")
	print("*"*80)
	print(city, month, day)
	#returning city, month, and day variables based on the user input
	return(city, month, day)

def data_loading_from_csv(city, month, day):
	df = pd.read_csv(info_cities[city])
	df["Start Time"]= pd.to_datetime(df["Start Time"]) # Pandas to_datetime() method helps to convert string Date time into Python Date time object.From https://www.geeksforgeeks.org/
	print("Showing starting time")
	print(df["Start Time"])
	print("*"*80)


	print("Showing months")
	#df["month"] = df["Start Time"].dt.month_name() #Extracting month
	df["month"] = df["Start Time"].dt.month
	print(df["month"])
	print("*"*80)


	print("Showing days")
	df["day_of_week"] = df["Start Time"].dt.day_name() #Extracting month
	print(df["day_of_week"])
	print("*"*80)


	if month != 'ALL':
		new_months = ['JANUARY', 'FEBRUARY', 'MARCH', 'APRIL', 'MAY', 'JUNE']
		month = new_months.index(month) + 1
		df = df[df["month"] == month]

	if day != "ALL":
		df = df[df["day_of_week"] == day.title()]


	return df

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""
    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()
    month_dict = {1:'January', 2:'February', 3: 'March', 4 : 'April', 5:'May', 6:'June'}
    most_common_month = df['month'].mode()[0]
    if most_common_month in month_dict.keys():
    	print('Most common month:', most_common_month)


    # display the most common month
    	print("The most common month is ", df["month"].mode()[0], "\n")


    # display the most common day of week
    	print("The most common day of week  is ", df['day_of_week'].mode()[0], "\n")


    # display the most common start hour
    	df['hour'] = df['Start Time'].dt.hour
    	print("The most common start hour is ", df['hour'].mode()[0])


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('*'*80)

def station_stats(df):
    """Displays statistics on the most popular stations and trip."""
    print('\nCalculating The Most Popular Stations and Trip...\n')

    start_time = time.time()

    # display most commonly used start station
    print("The most commonly used start station is ", df['Start Station'].mode()[0], "\n")


    # display most commonly used end station
    print("The most commonly used end station is ", df['End Station'].mode()[0], "\n")


    # display most frequent combination of start station and end station trip
    df['combination'] = df['Start Station'] + " " + df['End Station']
    print("The most frequent combination of start station and end station trip is: ", df['combination'].mode()[0])


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('*'*80)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""
    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    print("The total travel time is", df['Trip Duration'].sum(), "\n")


    # display mean travel time
    print("The total mean time is", df['Trip Duration'].mean())


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df, city):
    """Displays statistics on bikeshare users."""
    print('\nCalculating User Stats...\n')
    start_time = time.time()
    # Display counts of user types
    user_types = df.groupby(['User Type'])['User Type'].count()
    print(user_types, "\n")
    if city != 'washington':
        # Display counts of gender
        gen = df.groupby(['Gender'])['Gender'].count()
        print(gen)
        print(df['Gender'].value_counts())presentation by Oky
        # Display earliest, most recent, and most common year of birth
        mryob = sorted(df.groupby(['Birth Year'])['Birth Year'], reverse=True)[0][0]
        eyob = sorted(df.groupby(['Birth Year'])['Birth Year'])[0][0]
        mcyob = df['Birth Year'].mode()[0]
        print("The earliest year of birth is ", eyob, "\n")
        print("The most recent year of birth is ", mryob, "\n")
        print("The most common year of birth is ", mcyob, "\n")
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('*'*80)

    x = 1
    while True:
        raw = input('\nWould you like to see some raw data? Enter yes or no.\n')
        if raw.lower() == 'yes':
            print(df[x:x+5])
            x = x+5
        else:
            break

def main():
	while True:
		city, month, day = find_city_month_day()
		df= data_loading_from_csv(city, month, day)
		time_stats(df)
		station_stats(df)
		trip_duration_stats(df)
		user_stats(df, city)

		start_over = input('\nWould you like to restart? Enter yes or no.\n')
		if start_over.upper() != "YES":
			break

if __name__ == "__main__":
	main()
