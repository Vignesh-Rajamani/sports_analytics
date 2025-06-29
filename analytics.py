import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os
import uuid

def analyze_stats(filepath):
    df = pd.read_csv(filepath)

    # Basic summary (top players by points)
    top_players = df.groupby('player_name')['points'].sum().sort_values(ascending=False).head(5)
    summary = top_players.to_dict()

    # ✅ Ensure static folder exists
    static_dir = "static"
    os.makedirs(static_dir, exist_ok=True)

    # Plot and save file
    plot_file = os.path.join(static_dir, f"performance_{uuid.uuid4().hex[:6]}.png")
    plt.figure(figsize=(10, 5))
    sns.barplot(x=top_players.index, y=top_players.values)
    plt.title('Top 5 Players by Total Points')
    plt.ylabel('Points')
    plt.xlabel('Player')
    plt.tight_layout()
    plt.savefig(plot_file)
    plt.close()

    return summary, plot_file
