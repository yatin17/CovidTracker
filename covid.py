import tkinter as tk
import requests
import pycountry
import COVID19Py
covid19 = COVID19Py.COVID19()
covid19 = COVID19Py.COVID19(data_source="jhu")
# In the process of migrating from the covid module to a new API
def data_retrieval(root):
  country = textf.get()
  countries_module = pycountry.countries.get(name=country)
  namevar = countries_module.alpha_2
  confirmed_cases = 0
  confirmed_deaths = 0
  data = covid19.getLocationByCountryCode(namevar)#Code(country)
  apidata = requests.get("https://corona.lmao.ninja/v3/covid-19/countries/" + country + "?strict=true")
  new_data = apidata.json()
  recovered_cases = new_data["recovered"]
  total_pop = new_data["population"]
  for vals in data:
    print(vals["latest"]['confirmed'])
    confirmed_cases = confirmed_cases + vals["latest"]["confirmed"]
    confirmed_deaths = confirmed_deaths + vals["latest"]["deaths"]
  first_label.config(text = "Confirmed Cases: "+ str(confirmed_cases))
  second_label.config(text="Confirmed Deaths: " + str(confirmed_deaths))
  disclaimer.config(text="Data retrieved from John Hopkins University\n Creator: Yatin Vi")
  third_label.config(text = "Recovered Cases: "+ str(recovered_cases))
  fourth_label.config(text="Total Population: " + str(total_pop))



root = tk.Tk()
# Sizing, Fonts, Titles
root.geometry("600x400")
first_font = ("Futura", 25, "bold")
second_font = ("Comic Sans MS", 15, "bold")
third_font = ("Comic Sans MS", 5, "bold")
root.title("COVID Cases Tracker")
root.configure(background="grey")
# input
textf = tk.Entry(root, font=first_font)
textf.pack(pady = 10)
textf.focus()
textf.bind('<Return>', data_retrieval)



first_label = tk.Label(root, font=second_font, bg="grey")
first_label.pack()
second_label = tk.Label(root, font=second_font, bg="grey")
second_label.pack()
third_label = tk.Label(root, font=second_font, bg="grey")
third_label.pack()
fourth_label = tk.Label(root, font=second_font, bg="grey")
fourth_label.pack()
disclaimer = tk.Label(root, font=third_font, bg="grey")
disclaimer.pack()
root.mainloop()