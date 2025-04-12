import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


df=pd.read_csv("/content/spotify_history.csv")
print(df)

#An overview of the dataset
df.info()#Statistical information of numeric features of the dataset
print(df.describe())

# Count of unique values for each categorical column
for col in ('platform', 'track_name', 'artist_name', 'album_name', 'reason_start', 'reason_end'):
    print(f'For column {col}, there are {df[col].nunique()} unique values.')

# 📊 Histogram of ms_played
plt.figure(figsize=(10, 5))
hist_plot = sns.histplot(df['ms_played'], bins=20, color='blue')
# Add value labels on top of bars
for bar in hist_plot.patches:
    height = bar.get_height()
    if height > 0:
        hist_plot.text(bar.get_x() + bar.get_width()/2, height + 1, int(height), ha='center', fontsize=9)

plt.title("Distribution of Milliseconds Played")
plt.xlabel("Milliseconds Played")
plt.ylabel("Frequency")
plt.show()


# Pie chart for platform distribution
platform_counts = df['platform'].value_counts()
plt.figure(figsize=(8,8))
plt.pie(platform_counts, labels=platform_counts.index, autopct='%1.1f%%', startangle=140, colors=sns.color_palette("pastel"))
plt.title("Platform Distribution")
plt.axis('equal')  # Equal aspect ratio ensures pie is a circle
plt.show()


top_platforms = df.groupby('platform')['ms_played'].mean().nlargest(20).index

top_platforms_df = df[df['platform'].isin(top_platforms)]

plt.figure(figsize=(12, 6))
sns.boxplot(x='platform', y='ms_played', data=top_platforms_df, palette='pastel', linewidth=1.5)
plt.title("Boxplot of Milliseconds Played by Top 20 Platforms", fontsize=16)
plt.xlabel("Platform", fontsize=14)
plt.ylabel("Milliseconds Played", fontsize=14)
plt.xticks(rotation=45, ha='right')
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()

# Explore correlation between ms_played and shuffle (if applicable)
cor = df[['ms_played', 'shuffle']].corr()
plt.figure(figsize=(5, 6))
sns.heatmap(cor, annot=True, fmt=".2f", linewidths=0.5, cmap="coolwarm")
plt.title("Correlation between Milliseconds Played and Shuffle")
plt.show()

# Barplot for average ms_played by platform
avg_ms_played = df.groupby("platform")["ms_played"].mean().sort_values(ascending=False)
plt.figure(figsize=(13, 6))
sns.barplot(x=avg_ms_played.index, y=avg_ms_played.values, color="orange")
plt.title("Average Milliseconds Played by Platform")
plt.xlabel("Platform")
plt.ylabel("Average Milliseconds Played")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Line Plot for average ms_played by track_name
avg_ms_played_tracks = df.groupby('platform')['ms_played'].mean().sort_values(ascending=False).head(10)
plt.figure(figsize=(8, 6))
sns.lineplot(x=avg_ms_played_tracks.index, y=avg_ms_played_tracks.values, marker='o', linewidth=2)
plt.xticks(rotation=45)
plt.title("Top 10 Tracks by Average Milliseconds Played")
plt.xlabel("platform")
plt.ylabel("Average Milliseconds Played")
plt.grid(True)
plt.tight_layout()
plt.show()
