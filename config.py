import os

oauth2_client_id = os.environ.get("FITOPS_OAUTH_CLIENT_ID", "")
client_secret = os.environ.get("FITOPS_CLIENT_SECRET", "")
redirect_url = os.environ.get("FITOPS_REDIRECT_URL", "")
authorization_uri = os.environ.get("FITOPS_AUTH_URL", "")
access_token_uri = os.environ.get("FITOPS_ACCESS_TOKEN_URI", "")
refresh_token_uri = access_token_uri
