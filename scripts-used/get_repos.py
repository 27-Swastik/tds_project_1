import aiohttp
import asyncio
import pandas as pd

token = '//'
headers = {'Authorization': f'token {token}'}
base_url = 'https://api.github.com'

async def fetch_user_repos(session, username):
    repos = []
    page = 1
    while True:
        url = f"{base_url}/users/{username}/repos?sort=pushed&direction=desc&page={page}&per_page=100"
        async with session.get(url, headers=headers) as response:
            user_repos = await response.json()
            if not user_repos:
                break

            repos.extend({
                "login": username,
                "full_name": repo.get('full_name', ''),
                "created_at": repo.get('created_at', ''),
                "stargazers_count": repo.get('stargazers_count', 0),
                "watchers_count": repo.get('watchers_count', 0),
                "language": repo.get('language', ''),
                "has_projects": repo.get('has_projects', False),
                "has_wiki": repo.get('has_wiki', False),
                "license_name": repo.get('license', {}).get('key', '') if repo.get('license') else '' 
            } for repo in user_repos)
            
            if len(repos) >= 500 or len(user_repos) < 100:
                break
            page += 1
    return repos


async def fetch_all_repositories():
    users_df = pd.read_csv('users.csv')
    logins = users_df['login'].tolist()
    
    all_repos = []
    async with aiohttp.ClientSession() as session:
        repo_tasks = [fetch_user_repos(session, login) for login in logins]
        user_repos_lists = await asyncio.gather(*repo_tasks)
        
        all_repos = [repo for user_repos in user_repos_lists for repo in user_repos]

    repos_df = pd.DataFrame(all_repos)
    repos_df.to_csv('repositories.csv', index=False)

if __name__ == '__main__':
    asyncio.run(fetch_all_repositories())
