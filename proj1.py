
import pandas as pd
import matplotlib.pyplot as plt
import datetime as dt
companies = pd.read_csv("Unicorn_Companies.csv")
companies["Date Joined"] = pd.to_datetime(companies["Date Joined"])
companies["Year Joined"] = companies["Date Joined"].dt.year
companies_sample = companies.sample(n = 50, random_state = 42)
companies_sample["years_till_unicorn"] = companies_sample["Year Joined"] - companies_sample["Year Founded"]
grouped = (companies_sample[["Industry", "years_till_unicorn"]]
           .groupby("Industry")
           .max()
           .sort_values(by="years_till_unicorn")
          )


plt.bar(grouped.index, grouped["years_till_unicorn"])





plt.title("Bar plot of maximum years taken by company to become unicorn per industry (from sample)")



plt.xlabel("Industry")


plt.ylabel("Maximum number of years")


plt.xticks(rotation=45, horizontalalignment='right')


plt.show()