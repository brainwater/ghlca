Github Large Code Analysis (ghlca)
==================================

Scripts, utilities, and stuff used to answer questions that need data from github to answer.

## Steps
First I used BigQuery to download csv lists of the most "important" repositories on GitHub. I then used those csvs as a list of repositories to download, using the script downrepos.bash, which takes a list of repository urls and downloads them to the specified folder (I used `tail -n +2 ${filename} | cut -d "," -f 1` to get a list of the repo urls).

## BigQuery
I used bigquery for listing the most "important" repositories on GitHub. I got lists of the repositories with the most number of watchers, the most number of forks, and the highest value of watchers multiplied with forks.
### Most Watchers
    SELECT
      *
    FROM [publicdata:samples.github_timeline] a
    JOIN EACH
      (
         SELECT MAX(created_at) as max_created, repository_url 
         FROM [publicdata:samples.github_timeline]
         GROUP EACH BY repository_url
      ) b
      ON 
      b.max_created = a.created_at and
      b.repository_url = a.repository_url
    ORDER BY repository_watchers desc
    LIMIT 5000
### Most forks
    SELECT
      *
    FROM [publicdata:samples.github_timeline] a
    JOIN EACH
      (
         SELECT MAX(created_at) as max_created, repository_url 
         FROM [publicdata:samples.github_timeline]
         GROUP EACH BY repository_url
      ) b
      ON 
      b.max_created = a.created_at and
      b.repository_url = a.repository_url
    ORDER BY repository_forks desc
    LIMIT 5000
### Greatest Value for Forks * Watchers
    SELECT
      *,
      repository_watchers * repository_forks as repository_value
    FROM [publicdata:samples.github_timeline] a
    JOIN EACH
      (
         SELECT MAX(created_at) as max_created, repository_url 
         FROM [publicdata:samples.github_timeline]
         GROUP EACH BY repository_url
      ) b
      ON 
      b.max_created = a.created_at and
      b.repository_url = a.repository_url
    ORDER BY repository_value desc
    LIMIT 5000
## Layout
Bash scripts are under the 'scripts' directory, python scripts are under the 'python' directory.
### Python Scripts
Located under the 'python' directory, there are a few prefixes that indicate what the script is used for.
The ghlca.py file is the common file with common variables and utilities defined.
#### 'pop' prefix
Populates the mongodb with data, and should be idempotent when run twice, and will fill in the missing data when more repos are added.
#### 'get' prefix
Indicates that it will look through the data and print out something about it. It should not change anything in the database or otherwise.


