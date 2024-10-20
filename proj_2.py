import pandas as pd
import matplotlib.pyplot as plt
import datetime as dt
companies = pd.read_csv("Unicorn_Companies.csv")
companies["Date Joined"] = pd.to_datetime(companies["Date Joined"])
companies["Year Joined"] = companies["Date Joined"].dt.year
companies_sample = companies.sample(n = 50, random_state = 42)
companies_sample["years_till_unicorn"] = companies_sample["Year Joined"] - companies_sample["Year Founded"]

companies_sample['valuation_billions'] = companies_sample['Valuation']

companies_sample['valuation_billions'] = companies_sample['valuation_billions'].str.replace('$', '')

companies_sample['valuation_billions'] = companies_sample['valuation_billions'].str.replace('B', '')

companies_sample['valuation_billions'] = companies_sample['valuation_billions'].astype('int')

grouped = (companies_sample[["Industry", "valuation_billions"]]
           .groupby("Industry")
           .max()
           .sort_values(by="valuation_billions")
          )

plt.bar(grouped.index, grouped["valuation_billions"])



plt.title("Bar plot of maximum unicorn company valuation per industry (from sample)")



plt.xlabel("Industry")



plt.ylabel("Maximum valuation in billions of dollars")



plt.xticks(rotation=45, horizontalalignment='right')



plt.show()

