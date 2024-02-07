from setuptools import find_packages, setup

setup(
    name="rocket_launches",
    packages=find_packages(exclude=["rocket_launches_tests"]),
    install_requires=[
        "dagster",
        "dagster-cloud"
    ],
    extras_require={"dev": ["dagster-webserver", "pytest"]},
)
