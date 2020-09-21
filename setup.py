from setuptools import find_packages, setup


GITHUB_URL = "https://github.com/tfiers/jupyter-tray-app"

with open("ReadMe.md", mode="r", encoding="utf-8") as f:
    readme = f.read()

setup(
    name="jupyter-tray-app",
    description="Run the Jupyter notebook server as an app in the system tray",
    author="Tomas Fiers",
    author_email="tomas.fiers@gmail.com",
    long_description=readme,
    long_description_content_type="text/markdown",
    url=GITHUB_URL,
    project_urls={"Source Code": GITHUB_URL},
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    install_requires=["notebook"],
    packages=find_packages(),
    # Include all .ico files in all found packages.
    package_data={"": ["*.ico"]},
    # Get package version from git tags
    setup_requires=["setuptools_scm"],
    use_scm_version={
        "version_scheme": "post-release",
        "local_scheme": "dirty-tag",
    },
)