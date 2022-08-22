from setuptools import setup, find_packages

with open("README.md") as readme_file:
    readme = readme_file.read()


setup(
    author="Thomas Mohren",
    author_email="tlmohren@gmail.com",
    python_requires=">=3.6",
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
    ],
    description="Data savers with optional timestamps for logging of events",
    license="MIT license",
    long_description=readme,
    include_package_data=True,
    name="event_data_logging",
    packages=["event_data_logging"],
    test_suite="tests",
    install_requires=["numpy"],
    tests_require=["pytest", "coverage"],
    package_dir={"": "src"},
    url="https://github.com/maimonlab/event_data_logging",
    version="0.1.0",
    zip_safe=False,
)

# keywords="python_boilerplate",
# packages=find_packages(include=["python_boilerplate", "python_boilerplate.*"]),
# packages=find_packages(where="src"),
# package_data=[]
