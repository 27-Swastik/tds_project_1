import aiohttp
import asyncio
import pandas as pd

token = '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//'
headers = {'Authorization': f'token {token}'}
base_url = 'https://api.github.com'

def clean_company(company):
    if company:
        company = company.strip()
        if company.startswith('@'):
            company = company[1:]
        return company.upper()
    return ''

async def fetch_user_detail(session, login):
    async with session.get(f"{base_url}/users/{login}", headers=headers) as response:
        return await response.json()

async def fetch_users_in_delhi():
    users = []
    page = 1
    async with aiohttp.ClientSession() as session:
        while True:
            url = f"{base_url}/search/users?q=location:Delhi+followers:>100&page={page}&per_page=100"
            async with session.get(url, headers=headers) as response:
                data = await response.json()
                if 'items' not in data or not data['items']:
                    break

                user_tasks = [fetch_user_detail(session, user['login']) for user in data['items']]
                user_details = await asyncio.gather(*user_tasks)

                users.extend({
                    "login": user['login'],
                    "name": user.get('name', ''),
                    "company": clean_company(user.get('company', '')),
                    "location": user.get('location', ''),
                    "email": user.get('email', ''),
                    "hireable": user.get('hireable', ''),
                    "bio": user.get('bio', ''),
                    "public_repos": user.get('public_repos', 0),
                    "followers": user.get('followers', 0),
                    "following": user.get('following', 0),
                    "created_at": user.get('created_at', ''),
                } for user in user_details if user)
                if 'incomplete_results' in data and data['incomplete_results']:
                    break
                page += 1

    users_df = pd.DataFrame(users)
    users_df.to_csv('users.csv', index=False)

if __name__ == '__main__':
    asyncio.run(fetch_users_in_delhi())
