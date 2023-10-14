import setuptools

with open("README.md","r",encoding='utf-8') as f:
    long_description = f.read()


__version__ = '0.0.0'

REPO_NAME = 'Chicken-Disease-Classification'
AUTHOR_USER_NAME = "TheLearner05"
SRC_REPO = "cnnClassifier"
AUTHOR_EMAIL = "jayhegshetye@gmail.com"

setuptools.setup(
    name = SRC_REPO,
    version = __version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description = "a small python package for cnn app",
    long_description = long_description,
    url = f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    project_urls = {
        "Bug Tracker": f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues",

    },
    package_dir = {"": "src"},
    packages=setuptools.find_packages(where='src')

)