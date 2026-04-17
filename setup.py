import setuptools

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

__version__="0.0.0"

REPO_NAME = "Text-Summarizer"
AUTHOR_USER_NAME = "Deepjyoti-hub"
SRC_REPO = "TextSummarizer"
AUTHOR_EMAIL = "deepjyoti692@gmail.com"


setuptools.setup(
    name=SRC_REPO,
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="A small package for Text Summarization",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    packages=setuptools.find_packages(where="src"),
    project_urls={
        "Bug Tracker": f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues",
    },
    package_dir={"": "src"},
    python_requires=">=3.9"
)