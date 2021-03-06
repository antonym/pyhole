#   Copyright 2011 Josh Kearney
#
#   Licensed under the Apache License, Version 2.0 (the "License");
#   you may not use this file except in compliance with the License.
#   You may obtain a copy of the License at
#
#       http://www.apache.org/licenses/LICENSE-2.0
#
#   Unless required by applicable law or agreed to in writing, software
#   distributed under the License is distributed on an "AS IS" BASIS,
#   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#   See the License for the specific language governing permissions and
#   limitations under the License.

from pip.req import parse_requirements
from setuptools import setup

from pyhole import version


def requirements():
    install_reqs = parse_requirements("requirements.txt")
    return [str(ir.req) for ir in install_reqs]


setup(
    name="irc-pyhole",
    version=version.version_hash(),
    author="Josh Kearney",
    author_email="josh@jk0.org",
    description="A modular IRC bot for Python developers.",
    license="Apache License, Version 2.0",
    url="http://pyhole.org",
    packages=["pyhole", "pyhole.plugins"],
    install_requires=requirements(),
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Intended Audience :: Information Technology",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
    ],
    entry_points={
        "console_scripts": ["pyhole = pyhole.client:main"]
    },
    setup_requires=['nose>=1.3.0']
)
