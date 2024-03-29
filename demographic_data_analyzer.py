
import pandas as pd


def calculate_demographic_data(print_data=True):
    # Read data from file
    df = pd.read_csv("adult.data.csv")

    # How many of each race are represented in this dataset? This should be a Pandas series with race names as the index labels.
    race_count = df['race'].value_counts()

    # What is the average age of men?
    male_df = df[df['sex'] == 'Male']
    average_age_men = round(male_df['age'].mean(), 1)

    # What is the percentage of people who have a Bachelor's degree?
    total_people = len(df)
    bachelors_people = (df['education'] == 'Bachelors').sum()
    percentage_bachelors = round((bachelors_people / total_people) * 100, 1)

    # What percentage of people with advanced education (`Bachelors`, `Masters`, or `Doctorate`) make more than 50K?
    # What percentage of people without advanced education make more than 50K?

    # with and without `Bachelors`, `Masters`, or `Doctorate`
    adv_ed = df[df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])]
    no_adv_ed = df[~df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])]

    adv_ed_len = len(adv_ed)
    no_adv_ed_len = len(no_adv_ed)
    
    # percentage with salary >50K
    adv_ed_rich = adv_ed[adv_ed['salary'] == '>50K']
    no_adv_ed_rich = no_adv_ed[no_adv_ed['salary'] == '>50K']
    
    adv_ed_rich_len = len(adv_ed_rich)
    no_adv_rich = len(no_adv_ed_rich)

    higher_education_rich = round((adv_ed_rich_len/ adv_ed_len) * 100, 1)
    lower_education_rich = round((no_adv_rich/ no_adv_ed_len) * 100, 1)
    
    # What is the minimum number of hours a person works per week (hours-per-week feature)?
    min_work_hours = df['hours-per-week'].min()
    min_work_hours_df = df[df['hours-per-week'] == min_work_hours]
    min_work_hours_len = len(min_work_hours_df)

    # What percentage of the people who work the minimum number of hours per week have a salary of >50K?
    rich = df[df['salary'].isin(['>50K'])]
    rich_len = len(rich)
    min_working_rich = rich[rich['hours-per-week'] == min_work_hours]
    num_min_workers = len(min_working_rich)
    rich_percentage = round((num_min_workers/min_work_hours_len) * 100, 1)

    

    # What country has the highest percentage of people that earn >50K?
    country_population = df['native-country'].value_counts()
    rich_population = df[df['salary']=='>50K']['native-country'].value_counts()

    highest_earning_country = (rich_population / country_population * 100).idxmax()

    highest_earning_country_percentage = round((rich_population / country_population * 100).max(), 1)

    # Identify the most popular occupation for those who earn >50K in India.
    rich_in_India = rich[rich['native-country'] == 'India']
    top_IN_occupation = rich_in_India['occupation'].value_counts().idxmax()

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

 

