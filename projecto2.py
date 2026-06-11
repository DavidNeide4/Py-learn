import pandas as pd


def calculate_demographic_data(print_data=True):

    # Ler os dados
    df = pd.read_csv("adult.data.csv")

    # Quantidade de pessoas por raça
    race_count = df["race"].value_counts()

    # Idade média dos homens
    average_age_men = round(
        df[df["sex"] == "Male"]["age"].mean(), 1
    )

    # Percentagem de pessoas com Bacharelado
    percentage_bachelors = round(
        (df["education"] == "Bachelors").mean() * 100, 1
    )

    # Educação avançada
    higher_education = df["education"].isin(
        ["Bachelors", "Masters", "Doctorate"]
    )

    # Percentagem com educação avançada que ganha >50K
    higher_education_rich = round(
        (
            df[higher_education]["salary"] == ">50K"
        ).mean() * 100,
        1
    )

    # Percentagem sem educação avançada que ganha >50K
    lower_education_rich = round(
        (
            df[~higher_education]["salary"] == ">50K"
        ).mean() * 100,
        1
    )

    # Horas mínimas trabalhadas
    min_work_hours = df["hours-per-week"].min()

    # Pessoas que trabalham o mínimo de horas
    min_workers = df[
        df["hours-per-week"] == min_work_hours
    ]

    # Percentagem dos que trabalham menos horas e ganham >50K
    rich_percentage = round(
        (
            min_workers["salary"] == ">50K"
        ).mean() * 100,
        1
    )

    # País com maior percentagem de ricos
    country_salary = (
        df[df["salary"] == ">50K"]["native-country"]
        .value_counts()
        /
        df["native-country"].value_counts()
        * 100
    )

    highest_earning_country = country_salary.idxmax()

    highest_earning_country_percentage = round(
        country_salary.max(),
        1
    )

    # Ocupação mais comum entre ricos na Índia
    top_IN_occupation = (
        df[
            (df["native-country"] == "India")
            &
            (df["salary"] == ">50K")
        ]["occupation"]
        .value_counts()
        .idxmax()
    )

    if print_data:
        print("Número de cada raça:\n", race_count)
        print("Idade média dos homens:", average_age_men)
        print("% com Bacharelado:", percentage_bachelors)
        print("% educação avançada e >50K:", higher_education_rich)
        print("% sem educação avançada e >50K:", lower_education_rich)
        print("Horas mínimas:", min_work_hours)
        print("% ricos entre quem trabalha menos:", rich_percentage)
        print("País com maior % de ricos:", highest_earning_country)
        print("Percentagem:", highest_earning_country_percentage)
        print("Ocupação mais comum na Índia:", top_IN_occupation)

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