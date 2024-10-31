# THE PROCESS
To scrape the data, I followed these steps:
1. GitHub Access Token: Generated a personal access token from GitHub for authentication to the API. This token allows access to user data while adhering to rate limits.

2. API Requests: Used the requests library in Python to send GET requests to the GitHub API endpoints. Set the authorization header with the access token to authenticate each request.

3. Pagination Handling: Implemented pagination to retrieve multiple pages of users. Each request fetches a limited number of user profiles, so I looped through pages until all eligible users were collected.

4. Data Extraction: Parsed the JSON response to extract relevant user information, such as username, name, company, location, email, hireable status, bio, and follower count.

5. CSV Storage: Stored the extracted data in structured CSV files (users.csv for user profiles and repositories.csv for their repositories) using the pandas library, ensuring proper formatting for analysis.

# INTERESTING FACT
One of the most surprising findings was that a significant portion of developers in Delhi who are hireable do not list their email addresses publicly. Despite the common expectation that hireable individuals would be more likely to share contact information, the data showed that the fraction of hireable users with email addresses was only marginally higher than that of non-hireable users. This highlights a potential trend in privacy concerns among developers, even when seeking job opportunities.

# RECOMMENDATION
Developers should consider enhancing their GitHub profiles by writing comprehensive bios and enabling features like projects and wikis. This could potentially increase their follower count and visibility within the developer community. Additionally, being hireable and actively sharing email addresses may facilitate networking opportunities, leading to more collaborative projects and job offers.
