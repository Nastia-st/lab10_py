import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("Inflation.csv", sep=';') # Зчитування даних
df["2019"] = pd.to_numeric(df["2019"], errors="coerce")
df = df[df["2019"] >= 0].dropna(subset=["2019"]) # Видаляємо рядки з пропущеними або від’ємними значеннями
data_2019 = df.head(10) # Беремо перші 10 країн
countries = data_2019["Country Name"]
values = data_2019["2019"]

# Побудова кругової діаграми
plt.figure(figsize=(8, 8))
plt.pie(
    values,
    labels=countries,
    autopct='%1.1f%%',
    startangle=140,
    colors=plt.cm.tab10.colors
)
plt.title("Рівень інфляції у 2019 році (перші 10 країн)")
plt.tight_layout()
plt.show()