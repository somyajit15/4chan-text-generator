import matplotlib.pyplot as plt

marks = [10, 20, 25, 30, 35, 40, 45, 50,
         55, 60, 65, 70, 75, 80, 150]

plt.boxplot(marks)

plt.title("Box plot of student marks")
plt.ylabel("marks")

plt.show()