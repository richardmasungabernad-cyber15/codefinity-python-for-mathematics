import random
import matplotlib.pyplot as plt

def simulate_dice_rolls(num_rolls):
    sums = []
    for _ in range (1000):
        dice1 = random.randint(1,6)
        dice2 = random.randint(1,6)
        roll_sums = dice1 + dice2
        sums.append(dice1 + dice2)
    return sums
    
    
from collections import Counter 
def analyze_sums(sums):
    count = Counter(sums)
    most_common = count.most_common(1)[0][0]
    least_common = min(count, key=count.get)
    return most_common, least_common, count
    

def plot_histogram(sums):
    plt.hist(sums, bins=range(2,13), edgecolor = "black", align = "left")
    plt.title("Histogram for sums")
    plt.xlabel("sums")
    plt.ylabel("Frequency")
    plt.show()
    

findings = None  # Store findings at module level

def main():
    global findings
    num_rolls = 1000
    sums = simulate_dice_rolls(num_rolls)
    most_common, least_common, count = analyze_sums(sums)
    plot_histogram(sums)
    findings = (
        f"Most common sum: {most_common} (occurred {count[most_common]} times)\n"
        f"Least common sum: {least_common} (occurred {count[least_common]} times)"
    )
    print(findings)

if __name__ == "__main__":
    main()
