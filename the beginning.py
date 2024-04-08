import redditharbor.login as login
from redditharbor.dock.pipeline import collect

# Configure authentication
SUPABASE_URL = "https://sucbyycpcdlnxivgtetc.supabase.co"
SUPABASE_KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InN1Y2J5eWNwY2Rsbnhpdmd0ZXRjIiwicm9sZSI6InNlcnZpY2Vfcm9sZSIsImlhdCI6MTcxMjU0MjEyOCwiZXhwIjoyMDI4MTE4MTI4fQ.d1SiMd_UIeT7xPX7A2f2GnO3mFefhzwtyuXec9o0Jv4"  # Use "service_role/secret" key, not "anon/public"
REDDIT_PUBLIC = "WmY540g3fh4SmO27zMjsvA"
REDDIT_SECRET = "mO4sKlnXUeVF0-Ue6ooSon2is1iLVg"
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
