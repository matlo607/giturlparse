from .assembla import AssemblaPlatform
from .base import BasePlatform
from .bitbucket import BitbucketPlatform
from .friendcode import FriendCodePlatform
from .gerrit import GerritPlatform
from .github import GitHubPlatform
from .gitlab import GitLabPlatform

# Supported platforms
PLATFORMS = [
    # name -> Platform object
    ("github", GitHubPlatform()),
    ("bitbucket", BitbucketPlatform()),
    ("friendcode", FriendCodePlatform()),
    ("assembla", AssemblaPlatform()),
    ("gerrit", GerritPlatform()),
    ("gitlab", GitLabPlatform()),
    # Match url
    ("base", BasePlatform()),
]
