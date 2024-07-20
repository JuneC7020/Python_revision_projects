import pandas as pdKim

def monthNday(month, day):
    return month*100 + day

def get_zodiac_sign(month, day):
    zodiac_signs = [
        ("Capricorn", 120, 119),
        ("Aquarius", 120, 218),
        ("Pisces", 219, 320),
        ("Aries", 321, 419),
        ("Taurus", 420, 520),
        ("Gemini", 521, 621),
        ("Cancer", 622, 722),
        ("Leo", 723, 822),
        ("Virgo", 823, 922),
        ("Libra", 923, 1023),
        ("Scorpio", 1024, 1121),
        ("Sagittarius", 1122, 1221),
        ("Capricorn", 1222, 119)
    ]

    birth_md = monthNday(month, day)

    for sign, start_date, end_date in zodiac_signs:
        if start_date <= birth_md <= end_date:
            return sign
    
    return "Capricorn"

name = input("What is your name?: ")
birthmonth = int(input("What is the month of your birth?(1-12): "))
birthday = int(input("What is the day of your birth?(1-31): "))
# birthyear = input("What is the year of your birth?: ")


zodiac_sign = get_zodiac_sign(birthmonth, birthday)

print(f"Hello, {name}. Your Zodiac sign is {zodiac_sign}.")


data = {
    "Name": [name],
    "Zodiac Sign": [zodiac_sign]
}

df = pd.DataFrame(data)
df.to_csv('zodiac_signs.csv', index=False)

print("Your information has been saved to 'zodiac_signs.csv'.")

