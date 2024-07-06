import setuptools

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

__version__ = "0.0.0"

REPO_NAME = "Brief-A-Text"
AUTHOR_USER_NAME = "sheetalkumari2425"
SRC_REPO = "briefAtext"
AUTHOR_EMAIL = "sheetalkumari2425@gmail.com"

setuptools.setup(
    name=SRC_REPO,
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="A python package for CNN app",
    long_description=long_description,
    long_description_content="text/markdown",
    url=f"https://gitub.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    project_urls={
        "Bus Tracker": f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issue", 
    },
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src")
)