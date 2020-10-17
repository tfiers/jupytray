from setuptools import find_packages, setup


GITHUB_URL = "https://github.com/tfiers/jupytray"

with open("ReadMe.md", mode="r", encoding="utf-8") as f:
    readme = f.read()

setup(
    name="jupytray",
    description="Run the Jupyter notebook server as a little app in the system tray",
    author="Tomas Fiers",
    author_email="tomas.fiers@gmail.com",
    long_description=readme,
    long_description_content_type="text/markdown",
    url=GITHUB_URL,
    project_urls={"Source Code": GITHUB_URL},
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Operating System :: Microsoft :: Windows",
    ],
    install_requires=["notebook", "click ~= 7.1", "pywin32", "winshell == 0.6"],
    packages=find_packages(where="src"),
    package_dir={"": "src"},  # This means: "Root package can be found in 'src' dir"
    package_data={"": ["*.ico"]},  # Include all .ico files in all found packages.
    entry_points={"console_scripts": ["jupytray-shortcuts = jupytray.shortcuts:cli"]},
    # Get package version from git tags
    setup_requires=["setuptools_scm"],
    use_scm_version={
        "version_scheme": "post-release",
        "local_scheme": "dirty-tag",
    },
)
