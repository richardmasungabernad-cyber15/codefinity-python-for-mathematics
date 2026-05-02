import random
import seaborn as sns
import matplotlib.pyplot as plt

def compare_class_scores():
    class1_scores = [random.randint(60, 100) for _ in range(30)]
    class2_scores = [random.randint(55, 98) for _ in range(30)]
    scores = [class1_scores, class2_scores]
    class_labels = ["Class 1", "Class 2"]
    ax = sns.boxplot(data=scores)
    plt.xticks([0, 1], class_labels)
    plt.ylabel("Test Scores")
    plt.title("Test Score Distribution Comparison")
    plt.show()

compare_class_scores()
