import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="quickda", 
    version="0.1.8",
    author="Sidheswar Venkatachalapathi",
    author_email="gauty95@gmail.com",
    description="Simple & Easy-to-use python modules to perform Quick Exploratory Data Analysis for any structured dataset!",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/sid-the-coder/QuickDA",
    packages=setuptools.find_packages(),
    install_requires=[
          'pandas',
          'numpy',
          'seaborn',
          'matplotlib',
          'pandas_profiling',
          'ppscore',
          'plotly'
      ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)