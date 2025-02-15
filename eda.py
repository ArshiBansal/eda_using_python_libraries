import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load Dataset
file_path = "C:\\Users\\HP\\OneDrive\\Desktop\\python netflix\\netflix_data.xlsx"
xls = pd.ExcelFile(file_path)
df = pd.read_excel(xls, sheet_name="Netflix Data")

# Handle missing values
df.fillna(df.mean(numeric_only=True), inplace=True)

# Define Netflix color palette
netflix_red = "#E50914"
netflix_black = "#221F1F"
netflix_gray = "#B81D24"
netflix_palette = [netflix_red, netflix_black, netflix_gray]

# Create Figure and Subplots
fig, axes = plt.subplots(2, 2, figsize=(16, 10), gridspec_kw={'height_ratios': [2, 1]}, constrained_layout=False)
fig.patch.set_facecolor('#141414')  # Netflix dark background

# Adjusting the title position to ensure visibility and set title color to white
fig.suptitle('Netflix Analysis', fontsize=20, fontweight="bold", color="white",  ha='center')

# 1. Genre Distribution
ax1 = axes[0, 0]
colors = sns.color_palette("Reds_r", len(df['Main Genre'].value_counts()))
sns.countplot(y=df['Main Genre'], order=df['Main Genre'].value_counts().index, palette=colors, ax=ax1)
ax1.set_title("Distribution of Main Genres", fontsize=14, fontweight="bold", color="white")
ax1.set_xlabel("Count", fontsize=12, color="white")
ax1.set_ylabel("Genre", fontsize=12, color="white")
ax1.tick_params(colors="white")
for index, value in enumerate(df['Main Genre'].value_counts().values):
    ax1.text(value + 10, index, str(value), fontsize=10, color='white', va="center")

# 2. Yearly Content Release Trend
ax2 = axes[0, 1]
sns.histplot(df['Release Year'].dropna(), bins=30, kde=True, color=netflix_red, ax=ax2)
ax2.set_title("Trend of Content Releases Over the Years", fontsize=14, fontweight="bold", color="white")
ax2.set_xlabel("Release Year", fontsize=12, color="white")
ax2.set_ylabel("Count", fontsize=12, color="white")
ax2.tick_params(colors="white")

# 3. Maturity Rating Distribution with Shades of Red
ax3 = axes[1, 0]
df['Maturity Rating'].value_counts().plot.pie(
    autopct='%1.1f%%', 
    colors=sns.color_palette("Reds_r", len(df['Maturity Rating'].value_counts())),  # Shades of red for the pie chart
    startangle=90, 
    shadow=True, 
    ax=ax3)
ax3.set_title("Maturity Rating Distribution", fontsize=14, fontweight="bold", color="white")
ax3.set_ylabel("")
ax3.tick_params(colors="white")

# 4. Feature Correlation Heatmap
ax4 = axes[1, 1]
sns.heatmap(df.select_dtypes(include=['number']).corr(), annot=True, cmap="Reds", linewidths=0.5, fmt=".2f", ax=ax4)
ax4.set_title("Feature Correlation Heatmap", fontsize=14, fontweight="bold", color="white")
ax4.tick_params(colors="white")

# Change all subplot backgrounds to Netflix black
for ax in axes.flat:
    ax.set_facecolor(netflix_black)

# Add Table Below Plots (adjusted position)
top_genres = df['Main Genre'].value_counts().head(5)
summary_table = pd.DataFrame({
    "Genre": top_genres.index,
    "Count": top_genres.values
})

plt.figtext(0.15, -0.2, summary_table.to_string(index=False), fontsize=12, color="white", fontweight="bold")

# Adjust layout and show plot
plt.subplots_adjust(hspace=0.3, bottom=0.15)  # Adjust spacing between subplots and bottom area
plt.show()
