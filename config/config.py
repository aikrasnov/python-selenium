import os

username = None
access_key = None

try:
    username = os.environ["SAUCE_USERNAME"]
    access_key = os.environ["SAUCE_ACCESS_KEY"]
except KeyError:
    pass


class Config:
    """Configuration class."""

    base_url = None
    screen_on_fail = None
    browser = None
    all_browser = None
    platform = None
    browser_version = None
    has_saucelabs_connect = username and access_key
    saucelabs_connection_string = f"https://{username}:{access_key}@ondemand.saucelabs.com/wd/hub"

    @classmethod
    def setup(cls, cfg):
        """Get values from config file."""
        for key, value in cfg.items():
            setattr(cls, key, value)
