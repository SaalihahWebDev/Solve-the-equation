import matplotlib.pyplot as plt
x=list(range(0,6))
y=[2*i+1 for i in x]
plt.plot(x,y,marker="o")
plt.title("Graph of y=2x+1")
plt.xlabel("x")
plt.ylabel("y")
plt.grid(True)
plt.show()