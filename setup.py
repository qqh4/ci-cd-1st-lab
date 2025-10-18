from setuptools import setup, find_packages

setup(
    name="ci_cd_1st_lab",
    version="1.0.0",
    packages=find_packages(),
    install_requires=[
        "Flask>=3.1.2"
    ],
    description="Simple demo project for CI/CD pipeline with SAST",
    author="qqh4",
    python_requires=">=3.8",
)
