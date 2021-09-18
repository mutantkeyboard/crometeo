import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="crometeo",
    version="0.0.1",
    author="Antonio Nesic",
    author_email="nesic.antonio@gmail.com",
    description="Client for readingn data from Meteo.hr",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/mutantkeyboard/crometeo",
    project_urls={
        "Bug Tracker": "https://github.com/mutantkeyboard/crometeo/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Intended Audience :: End Users/Desktop",
        "Framework :: Scrapy",
        "Topic :: Internet :: WWW/HTTP"
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.6",
)