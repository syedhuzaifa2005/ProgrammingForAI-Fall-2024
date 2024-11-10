import matplotlib.pyplot as plt

years = [1920, 1930, 1940, 1950, 1960, 1970, 1980, 1990, 2000, 2010, 2020]
sea_levels = [0, 5, 10, 15, 20, 25, 30, 35, 40, 50, 60]

plt.scatter(years, sea_levels, color='blue', label='Sea Level Rise')

plt.xlabel('Year')
plt.ylabel('Sea Level Rise (mm)')
plt.title('Sea Level Rise Over the Past 100 Years')

plt.legend()

plt.show()
