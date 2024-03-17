import pandas as pd


def calculate_demographic_data(print_data=True):
    # Read data from file
    df = pd.read_csv("adult.data.csv")

    # How many of each race are represented in this dataset? This should be a Pandas series with race names as the index labels.
    race_count = df['race'].value_counts()

    # What is the average age of men?
    male_df = df[df['sex'] == 'Male']
    average_age_men = male_df['age'].mean

    # What is the percentage of people who have a Bachelor's degree?
    total_people = len(df['education'])
    bachelors_people = (df['education'] == 'Bachelors').sum()
    percentage_bachelors = (bachelors_people / total_people) * 100

    # What percentage of people with advanced education (`Bachelors`, `Masters`, or `Doctorate`) make more than 50K?
    # What percentage of people without advanced education make more than 50K?

    # with and without `Bachelors`, `Masters`, or `Doctorate`
    adv_ed = df[df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])]
    no_adv_ed = df[~df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])]
    
    # percentage with salary >50K
    adv_ed_rich = adv_ed[adv_ed['salary'] == '>50K']
    no_adv_ed_rich = no_adv_ed[no_adv_ed['salary'] == '>50K']
    
    adv_ed_rich_len = len(adv_ed_rich['education'])
    no_adv_rich = len(no_adv_ed_rich['education'])

    higher_education_rich = (adv_ed_rich_len/total_people) * 100
    lower_education_rich = (no_adv_rich/total_people) * 100
    
    # What is the minimum number of hours a person works per week (hours-per-week feature)?
    min_work_hours = df['hours-per-week'].min()

    # What percentage of the people who work the minimum number of hours per week have a salary of >50K?
    rich = df[df['salary'].isin(['>50k'])]
    min_working_rich = rich['hours-per-week'] == min_work_hours
    num_min_workers = len(min_working_rich)
    rich_percentage = (num_min_workers/total_people) * 100


    # What country has the highest percentage of people that earn >50K?
    highest_earning_country = None
    highest_earning_country_percentage = None

    # Identify the most popular occupation for those who earn >50K in India.
    top_IN_occupation = None

    # DO NOT MODIFY BELOW THIS LINE

    if print_data:
        print("Number of each race:\n", race_count) 
        print("Average age of men:", average_age_men)
        print(f"Percentage with Bachelors degrees: {percentage_bachelors}%")
        print(f"Percentage with higher education that earn >50K: {higher_education_rich}%")
        print(f"Percentage without higher education that earn >50K: {lower_education_rich}%")
        print(f"Min work time: {min_work_hours} hours/week")
        print(f"Percentage of rich among those who work fewest hours: {rich_percentage}%")
        print("Country with highest percentage of rich:", highest_earning_country)
        print(f"Highest percentage of rich people in country: {highest_earning_country_percentage}%")
        print("Top occupations in India:", top_IN_occupation)

    return {
        'race_count': race_count,
        'average_age_men': average_age_men,
        'percentage_bachelors': percentage_bachelors,
        'higher_education_rich': higher_education_rich,
        'lower_education_rich': lower_education_rich,
        'min_work_hours': min_work_hours,
        'rich_percentage': rich_percentage,
        'highest_earning_country': highest_earning_country,
        'highest_earning_country_percentage':
        highest_earning_country_percentage,
        'top_IN_occupation': top_IN_occupation
    }
