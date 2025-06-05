from .base import BasePlatform


class GerritPlatform(BasePlatform):
    PATTERNS = {
        "https": (
            r"(?P<protocols>(git\+)?(?P<protocol>https))://"
            r"((?P<username>[^@]+)@)?(?P<domain>[^:/]+)(?P<port>:[0-9]+)?"
            r"(?P<pathname>/(a/)?(?P<repo>((?P<owner>[^/]+?)/)?[^.]+)"
            r"(?:(\.git)?(/)?))$"
        ),
        "ssh": (
            r"(?P<protocols>(git\+)?(?P<protocol>ssh))?(://)?"
            r"((?P<username>[^@]+)@)?(?P<domain>[^:/]+)(:)?(?P<port>[0-9]+)?(?(port))?"
            r"(?P<pathname>/(?P<authprefix>a/)?(?P<repo>((?P<owner>[^/]+?)/)?[^.]+)"
            r"(?:(\.git)?(/)?))$"
        ),
    }
    FORMATS = {
        "https": r"https://%(username_at)s%(domain)s/%(authprefix)s%(repo)s",
        "ssh": r"ssh://%(username_at)s%(domain)s%(colon_port)s/%(repo)s",
    }
    DOMAINS = (
        "gerrit.googlesource.com",
        "www.gerrithub.io",
    )
    DEFAULTS = {"_user": "git", "port": "29418", "authprefix": "a/"}

    @staticmethod
    def clean_data(data):
        data = BasePlatform.clean_data(data)
        if not data["port"]:
            data["port"] = GerritPlatform.DEFAULTS["port"]
        if "_user" not in data or not data["_user"]:
            data["_user"] = GerritPlatform.DEFAULTS["_user"]
        return data
