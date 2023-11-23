import setuptools


long_description = "A small python package for CNN app."

__version__ = "0.0.0"
REPO_NAME = "Kidney_disease"
AUTHOR_USER_NAME = "pushkar16042023"
SRC_REPO = "cnnClassifier"
AUTHOR_EMAIL = "pushkarsh22@gmail.com"

setuptools.setup(
    name=SRC_REPO,
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="A small python package for CNN app",
    long_description=long_description,
    long_description_content_type="text/plain",
    url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    project_urls={
        "Bug Tracker": f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues",
    },
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src")
)
