import matplotlib.markers
import matplotlib.pyplot as plt

a = [1, 2, 3, 4, 5]
b = [23, 55, 33, 45, 29]
c = [24, 58, 45, 24, 60]
d = [34, 56, 25, 88, 34]
# create line plot or line graph
plt.plot(a, b, "rD-", label="$Quarter 1$", ms=4, alpha=1.0)
plt.plot(a, c, marker="h", label="$Quarter 2$", ms=6, alpha=0.5)
plt.plot(a, d, marker=matplotlib.markers.TICKUP, label="$Quarter 3$", ms=8)
plt.title("Student Demo Data")
plt.xlabel("Numbers")
plt.ylabel("Values")
plt.legend(fontsize=14)
# plt.xlim(-5,10)
# plt.ylim(-10, 60)
# plt.axis("equal")
plt.show()  # it is used to show the line plot
