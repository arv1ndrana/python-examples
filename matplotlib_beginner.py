from matplotlib import pyplot as plt

fig, ax = plt.subplots()

animals = ['Hamster', 'Rabbits', 'Dogs', 'Cats']
counts = [4,2,6,3]
bar_colors = ['tab:blue', 'tab:red', 'tab:orange', 'tab:green']

ax.bar(animals, counts,color=bar_colors)
ax.set_ylabel('Count')
ax.set_title('Animals by me')

plt.show()
