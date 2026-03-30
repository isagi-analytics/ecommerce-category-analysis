import pandas as pd

# Simulated dataset
data = {
    'category': ['electronics', 'electronics', 'personal_care', 'personal_care'],
    'month': ['2024-01-01', '2024-02-01', '2024-01-01', '2024-02-01'],
    'total_revenue': [1000, 900, 500, 800]
}

df = pd.DataFrame(data)
df['month'] = pd.to_datetime(df['month'])

# Sort data
df = df.sort_values(['category', 'month'])

# Month-over-month change
df['mom_change'] = df.groupby('category')['total_revenue'].pct_change()

# Revenue share
df['revenue_share'] = df['total_revenue'] / df.groupby('month')['total_revenue'].transform('sum')

print(df)
