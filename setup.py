from setuptools import setup, find_packages

with open("requirements.txt") as f:
    required_packages = f.read().splitlines()

with open("README.md") as f:
    long_description = f.read()

# py2app
APP = ["bin/argos-translate-gui"]
DATA_FILES = []
OPTIONS = {"packages": ["sentencepiece"], "iconfile": "argostranslate/img/icon.icns"}

setup(
    name="argostranslategui",
    version="1.6.0",
    description="Graphical user interface for Argos Translate",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Argos Open Technologies, LLC",
    author_email="admin@argosopentech.com",
    url="https://www.argosopentech.com",
    packages=find_packages(),
    install_requires=required_packages,
    include_package_data=True,
    scripts=["bin/argos-translate-gui"],
    app=APP,
    data_files=DATA_FILES,
    options={"py2app": OPTIONS},
    setup_requires=["py2app"],
)
