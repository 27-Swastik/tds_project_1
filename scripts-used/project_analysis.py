import pandas as pd
from sklearn.linear_model import LinearRegression
users_df = pd.read_csv('users.csv')
repos_df = pd.read_csv('repositories.csv')

#Regression slope for followers vs repo counts
follower_count = users_df['followers'].values
repo_counts = users_df['public_repos'].values.reshape(-1, 1)
model = LinearRegression()
model.fit(repo_counts, follower_count)
print("Slope:",model.coef_[0])


#Regression slope of followers on bio word count
users_df.columns = users_df.columns.str.strip()
users_df = users_df[users_df['bio'].notna()]
users_df['bio_word_count'] = users_df['bio'].str.split().str.len()
follower_count = users_df['followers'].values.reshape(-1, 1)
bio_word_count = users_df['bio_word_count'].values.reshape(-1, 1)
model = LinearRegression()
model.fit(bio_word_count, follower_count)
slope = model.coef_[0][0]
print("slope:", slope)


#created the most repositories on weekends
repos_df['created_at'] = pd.to_datetime(repos_df['created_at'])
repos_df['day_of_week'] = repos_df['created_at'].dt.day_name()
weekend_repos = repos_df[repos_df['day_of_week'].isin(['Saturday', 'Sunday'])]
top_users = weekend_repos['login'].value_counts().head(5).index.tolist()
top_users_logins = ','.join(top_users)
print(top_users_logins)


#correlation between the number of followers and the number of public repositories
correlation = users_df['followers'].corr(users_df['public_repos'])
print(correlation)


#Finding the most common surname
surnames = users_df['name'].dropna().apply(lambda name: name.strip().split()[-1])
surname_counts = {}
for surname in surnames:
    surname_counts[surname] = surname_counts.get(surname, 0) + 1
max_count = max(surname_counts.values())
ans = []
for name in surname_counts.keys():
    if surname_counts[name] == max_count:
        ans.append(name)
print(ans)
