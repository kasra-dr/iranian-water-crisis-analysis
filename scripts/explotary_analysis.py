import os
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import arabic_reshaper
from bidi.algorithm import get_display

# --- Helper function for persian text ---
def persian_text(text):
    reshaped_text = arabic_reshaper.reshape(text)
    bidi_text = get_display(reshaped_text)
    return bidi_text

# Chart appearance settings
sns.set_theme(style="whitegrid")
plt.rcParams['font.family'] = 'Vazir'
plt.rcParams['font.size'] = 12
plt.rcParams['axes.labelsize'] = 12
plt.rcParams['axes.titlesize'] = 12
plt.rcParams['xtick.labelsize'] = 12
plt.rcParams['ytick.labelsize'] = 12
plt.rcParams['legend.fontsize'] = 12
plt.rcParams['figure.figsize'] = [10, 8]

# Define the path to the data files
CLEANED_DATA_PATH = 'data/processed/cleaned_iran_data.csv'
PLOTS_DIR = 'results/plots'

# Make folder for plots if it doesn't exist
os.makedirs(PLOTS_DIR, exist_ok=True)

# Read the deleted data
try:
    df = pd.read_csv(CLEANED_DATA_PATH)
    print("Cleaned data loaded successfully")
except FileNotFoundError:
    print(f"File not found: {CLEANED_DATA_PATH}")
    exit(1)

# -- Time series flow analysis ---
# Population trend chart
plt.figure(figsize=(12, 6))
sns.lineplot(x='year', y='population', data=df, marker='o', color='blue')
plt.title(persian_text('(2000-2024) روند افزایش جمعیت ایران'), fontsize=16)
plt.xlabel(persian_text('سال'), fontsize=12)
plt.ylabel(persian_text('(ده میلیون نفر) جمعیت'), fontsize=12)
plt.gca().get_yaxis().set_major_formatter(plt.FuncFormatter(lambda x, p: format(int(x), ',')))
plt.grid(True)
plt.savefig(os.path.join(PLOTS_DIR, 'population_trend.png'))
plt.close()

# Agriculture land trend chart
plt.figure(figsize=(12, 6))
sns.lineplot(x='year', y='agricultural_land_sqkm', data=df, marker='o', color='green')
plt.title(persian_text('(2000-2024) روند تغییر مساحت زمین‌های کشاورزی ایران'), fontsize=16)
plt.xlabel(persian_text('سال'), fontsize=12)
plt.ylabel(persian_text('(کیلومتر مربع) مساحت زمین‌های کشاورزی'), fontsize=12)
plt.gca().get_yaxis().set_major_formatter(plt.FuncFormatter(lambda x, p: format(int(x), ',')))
plt.grid(True)
plt.savefig(os.path.join(PLOTS_DIR, 'agricultural_land_trend.png'))
plt.close()

print("Time series plots saved.")

# --- Correlation analysis ---
# Calculate the correlation matrix
corr_matrix = df[['population', 'agricultural_land_sqkm']].corr()

# Draw the heatmap
plt.figure(figsize=(8, 6))
sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', fmt=".2f", linewidths=.5)
plt.title(persian_text('ماتریس همبستگی بین جمعیت و مساحت زمین‌های کشاورزی'), fontsize=16)
plt.savefig(os.path.join(PLOTS_DIR, 'correlation_heatmap.png'))
plt.close()

print("Correlation heatmap saved.")
print("\n✅ Explotary data analysis completed. Plots are saved in the 'results/plots' folder.")

# --- Initial interpretation ---
print("\n--- Initial interpretation ---")
print(persian_text("1. نمودار جمعیت، یک روند صعودی یکنواخت و قوی را نشان می‌دهد."))
print(persian_text("2. نمودار زمین‌های کشاورزی نوسانات بیشتری دارد؛ یک دوره کاهش در اواسط دهه ۲۰۰۰ و سپس یک ثبات نسبی."))
print(persian_text(f"3. ماتریس همبستگی مقدار {corr_matrix.iloc[0,1]:.2f} را نشان می‌دهد که یک همبستگی منفی ضعیف بین افزایش جمعیت و مساحت زمین‌های کشاورزی در این بازه را نشان می‌دهد. این نتیجه جالب و غیرمنتظره است و نیاز به بررسی بیشتر دارد."))