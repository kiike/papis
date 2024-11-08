#!/usr/bin/env python

from packaging.version import Version
import subprocess

git_description = subprocess.run("git describe --tags --dirty".split(),
                                 capture_output=True,
                                 text=True
                                 ).stdout
# When the command returns something like v0.14
if "-" in git_description:
    raw_version, count, _ = git_description.split("-")
# Otherwise, like v0.14-1-f00b4r
else:
    raw_version = git_description
    count = "0"

version = Version(raw_version)

if version.is_prerelease and version.pre is not None:
    prerelease_id = f"{version.pre[0]}.{version.pre[1]}"
    print(f"{version.major}.{version.minor}.{version.micro}-{prerelease_id}")
else:
    print(f"{version.major}.{version.minor}.{version.micro}.{count}")
