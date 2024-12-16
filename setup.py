import setuptools

with open("README.md", "r", encoding="utf-8") as file_obj:
    long_description = file_obj.read()


__version__ = "0.0.0"

REPO_NAME = "wine-quality-prediction-project"
AUTHOR_USER_NAME = "gaurav-batman"
SRC_REPO = "wine_quality_predictor"
AUTHOR_EMAIL = "gaurav@gmail.com"


setuptools.setup(
    name=SRC_REPO,
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="A small python package for ml app",
    long_description=long_description,
    long_description_content="text/markdown",
    url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    project_urls={
        "Bug Tracker": f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues",
    },
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src")
)