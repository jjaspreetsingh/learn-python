"""
Data Analysis Project
======================

Simple data analysis examples using Python's built-in statistics module.
"""

import statistics
from collections import Counter

# Sample data
sales_data = [120, 150, 140, 180, 200, 160, 175, 190, 210, 185, 165, 195]
temperatures = [22, 24, 25, 23, 26, 27, 25, 24, 23, 26, 28, 25]
student_scores = [85, 90, 78, 92, 88, 85, 91, 87, 89, 86, 90, 88]

print("=== Data Analysis Examples ===\n")

# Basic statistics
print("1. Sales Data Analysis")
print(f"   Data: {sales_data}")
print(f"   Mean: {statistics.mean(sales_data):.2f}")
print(f"   Median: {statistics.median(sales_data):.2f}")
print(f"   Mode: {statistics.mode(sales_data)}")
print(f"   Min: {min(sales_data)}")
print(f"   Max: {max(sales_data)}")
print(f"   Range: {max(sales_data) - min(sales_data)}")
print(f"   Standard Deviation: {statistics.stdev(sales_data):.2f}")

print("\n2. Temperature Analysis")
print(f"   Data: {temperatures}")
print(f"   Average: {statistics.mean(temperatures):.2f}°C")
print(f"   Median: {statistics.median(temperatures):.2f}°C")

print("\n3. Student Scores Analysis")
print(f"   Data: {student_scores}")
print(f"   Average Score: {statistics.mean(student_scores):.2f}")
print(f"   Median Score: {statistics.median(student_scores):.2f}")

# Frequency analysis
print("\n4. Score Frequency Analysis")
score_counts = Counter(student_scores)
print("   Score frequencies:")
for score, count in sorted(score_counts.items()):
    print(f"   {score}: {count} students")

# Data filtering
print("\n5. High Performers (score >= 90)")
high_scores = [score for score in student_scores if score >= 90]
print(f"   High scores: {high_scores}")
print(f"   Count: {len(high_scores)} students")
print(f"   Average: {statistics.mean(high_scores):.2f}")

# Data transformation
print("\n6. Data Transformation")
# Convert scores to percentages (assuming max is 100)
percentages = [f"{score}%" for score in student_scores]
print(f"   As percentages: {percentages[:5]}...")  # Show first 5

# Simple correlation example
print("\n7. Correlation Analysis")
# Check if there's a relationship between sales and temperatures
print("   Checking relationship between sales and temperatures...")
print(f"   Sales mean: {statistics.mean(sales_data):.2f}")
print(f"   Temperature mean: {statistics.mean(temperatures):.2f}")

# Data summary function
def analyze_data(data, name):
    """Analyze and print summary statistics for data."""
    print(f"\n=== {name} Summary ===")
    print(f"Count: {len(data)}")
    print(f"Sum: {sum(data)}")
    print(f"Mean: {statistics.mean(data):.2f}")
    print(f"Median: {statistics.median(data):.2f}")
    try:
        print(f"Mode: {statistics.mode(data)}")
    except statistics.StatisticsError:
        print("Mode: No unique mode")
    print(f"Min: {min(data)}")
    print(f"Max: {max(data)}")
    print(f"Range: {max(data) - min(data)}")
    if len(data) > 1:
        print(f"Std Dev: {statistics.stdev(data):.2f}")

print("\n8. Detailed Analysis Function")
analyze_data(sales_data, "Sales Data")

