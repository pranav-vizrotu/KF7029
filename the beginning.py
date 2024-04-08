import redditharbor.login as login
from redditharbor.dock.pipeline import collect

# Configure authentication
SUPABASE_URL = "https://sucbyycpcdlnxivgtetc.supabase.co"
SUPABASE_KEY = "************"
REDDIT_PUBLIC = "WmY540g3fh4SmO27zMjsvA"
REDDIT_SECRET = "***************"
REDDIT_USER_AGENT = "<institution:reddit-research (u/u/pranav_vizrotu)>"  # Format: <institution:project-name (u/reddit-username)>
# e.g. REDDIT_USER_AGENT = "LondonSchoolofEconomics:ICWSM-tutorial (u/reddit-username)"

# Define database table names
DB_CONFIG = {
    "user": "test_redditor",
    "submission": "test_submission",
    "comment": "test_comment"
}

# Login and create instances of Reddit and Supabase clients
reddit_client = login.reddit(public_key=REDDIT_PUBLIC, secret_key=REDDIT_SECRET, user_agent=REDDIT_USER_AGENT)
supabase_client = login.supabase(url=SUPABASE_URL, private_key=SUPABASE_KEY)

# Initialise an instance of the `collect` class
collect = collect(reddit_client=reddit_client, supabase_client=supabase_client, db_config=DB_CONFIG)

subreddits = ["python", "learnpython"]
sort_types = ["hot", "top"]
collect.subreddit_submission_and_comment(subreddits, sort_types, limit=5, level=2,mask_pii=True)

from redditharbor.utils import download

download = download.submission(supabase_client, DB_CONFIG["submission"])
download.to_csv(columns="all", file_name="submission", file_path="data")
