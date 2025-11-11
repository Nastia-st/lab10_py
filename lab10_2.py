import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("Inflation.csv", sep=';', encoding='utf-8-sig') # Зчитування даних із CSV
print(data.head())
data.columns = data.columns.str.strip()
country1 = "Ukraine"
country2 = "United States"
if country1 not in data['Country Name'].values:
    print(f"Країна '{country1}' не знайдена у файлі.")
    exit()
if country2 not in data['Country Name'].values:
    print(f"Країна '{country2}' не знайдена у файлі.")
    exit()
years = data.columns[1:] 
ukraine = data[data['Country Name'] == country1].iloc[0, 1:].values
usa = data[data['Country Name'] == country2].iloc[0, 1:].values

# Побудова лінійного графіка
plt.figure(figsize=(10, 6))
plt.plot(years, ukraine, color='blue', marker='o', linewidth=2, label='Україна')
plt.plot(years, usa, color='red', marker='s', linewidth=2, label='США')
plt.title('Інфляція (% річна) для України та США', fontsize=14)
plt.xlabel('Рік', fontsize=12)
plt.ylabel('Інфляція, %', fontsize=12)
plt.legend()
plt.grid(True)
plt.show()

#Стовпчаста діаграма
print("\nДоступні приклади: Україна, США, Argentina, Germany тощо.")
country = input("Введіть назву країни для побудови стовпчастої діаграми: ").strip()
if country not in data['Country Name'].values:
    print("Такої країни немає у файлі.")
    exit()
values = data[data['Country Name'] == country].iloc[0, 1:].values
plt.figure(figsize=(10, 6))
plt.bar(years, values, color='skyblue')
plt.title(f'Інфляція (% річна) для {country}', fontsize=14)
plt.xlabel('Рік', fontsize=12)
plt.ylabel('Інфляція, %', fontsize=12)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()