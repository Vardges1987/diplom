import pandas as pd
from .models import UserInteraction


def analyze_data():
    interactions = UserInteraction.objects.all().values()
    df = pd.DataFrame(interactions)

    df['duration'] = df['end_time'] - df['start_time']
    average_duration = df['duration'].mean()
    print(f'Average duration: {average_duration}')


def visualize_data():
    import matplotlib.pyplot as plt
    import seaborn as sns

    df = pd.DataFrame(UserInteraction.objects.values())
    sns.countplot(data=df, x='success')
    plt.title('Success Rate of Puzzles')
    plt.show()
