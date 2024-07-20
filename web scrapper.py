import requests
from bs4 import BeautifulSoup
import pandas as pd

def get_largest_us_companies():
    # URL of the Wikipedia page of the List of largest companies in the US
    url = "https://en.wikipedia.org/wiki/List_of_largest_companies_in_the_United_States_by_revenue"

    # Send a GET request to the URL
    response = requests.get(url)
    response.raise_for_status()  # Check for request errors

    # Parse the HTML content using Beautiful Soup
    soup = BeautifulSoup(response.content, 'html.parser')

    # Find the table containing the data
    table = soup.find('table', {'class': 'wikitable sortable'})

    # Initialize lists to store the extracted data
    ranks = []
    company_names = []
    industries = []
    revenues = []
    revenue_growths = []
    Employees = []
    Headquarters = []

    # Extract the data from the table rows
    for row in table.find_all('tr')[1:]:  # Skip the header row
        columns = row.find_all('td')
        if len(columns) >= 6:  # Ensure the row has enough columns
            ranks.append(columns[0].text.strip())
            company_names.append(columns[1].text.strip())
            industries.append(columns[2].text.strip())
            revenues.append(columns[3].text.strip())
            revenue_growths.append(columns[4].text.strip())
            Employees.append(columns[5].text.strip())
            Headquarters.append(columns[6].text.strip())

    # Create a Pandas DataFrame to store the data
    data = {
        'Rank': ranks,
        'Company': company_names,
        'Industry': industries,
        'Revenue': revenues,
        'Revenue Growth': revenue_growths,
        'Employees': Employees,
        'Headquarters': Headquarters,
    }
    df = pd.DataFrame(data)
    return df

# Run the function and store the result in a DataFrame
df = get_largest_us_companies()

# Display the DataFrame
print(df)

# Optionally, save the DataFrame to a CSV file
df.to_csv('largest_us_companies.csv', index=False)
