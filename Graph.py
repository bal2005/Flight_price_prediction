import matplotlib.pyplot as plt
import seaborn as sns
plt.subplots(figsize=(14,7))
sns.barplot(x=Airline, y=Price,ec = "black",palette="Set2")
plt.title("Airlines Company vs Flight Ticket Price", weight="bold",fontsize=20, pad=20)
plt.ylabel("Flight Ticket Price", weight="bold", fontsize=15)
plt.xlabel("Airlines Name", weight="bold", fontsize=16)
plt.xticks(rotation=90)
plt.show()
