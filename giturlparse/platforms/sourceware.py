from .base import BasePlatform


class SourcewarePlatform(BasePlatform):
    PATTERNS = {
        "git": (
            r"(?P<protocols>(?P<protocol>git))://(?P<domain>[^/]+)"
            r"(?P<pathname>/git/(?P<repo>[^.]+)\.git(/)?)$"
        ),
        "https": (
            r"(?P<protocols>(?P<protocol>https))://(?P<domain>[^/]+)"
            r"(?P<pathname>/git/(?P<repo>[^.]+)\.git(/)?)$"
        ),
        "ssh": (
            r"(?P<protocols>(?P<protocol>ssh))://(?P<domain>[^/]+)"
            r"(?P<pathname>/git/(?P<repo>[^.]+)\.git(/)?)$"
        ),
    }
    FORMATS = {
        "git": r"git://%(domain)s/git/%(repo)s.git",
        "https": r"https://%(domain)s/git/%(repo)s.git",
        "ssh": r"ssh://%(domain)s/git/%(repo)s.git",
    }
    DOMAINS = (
        "sourceware.org",
    )
