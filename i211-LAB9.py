import csv
import tools

listCompanies = csv.DictReader(open("companies.csv", "r"))
listofINCompanies = []

stateInput = str(input("Enter a state:"))

for company in listCompanies:
    if company['state'] == stateInput.upper():
        listofINCompanies.append([company['company_name'], company['web']])

listofINCompanies.sort(key=lambda company:company[0])

tools.table_print(("Company","Website"), listofINCompanies, 50)
