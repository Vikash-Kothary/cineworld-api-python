from setuptools import setup, find_packages

setup(name="Cineworld_API",
      version="0.1.0",
      description=D"Python wrapper for the Cineworld API",
      long_description=open("README.md").read().strip(),
      long_description_content_type="text/markdown",
      author="Vikash Kothary",
      author_email="kothary.vikash@gmail.com",
      url="https://github.com/vikash-kothary/cineworld-api-python",
      license=open("LICENSE").read().strip(),
      packages=find_packages(),
      zip_safe=False,
      install_requires=[
          "requests==2.20.0"
      ],
      keywords=["coffee-meets-bagel-api", "coffee-meets-bagel", "cmb-api", "cmb", "python-3"],
      classifiers=[
          "Programming Language :: Python",
          "Topic :: Software Development :: Libraries :: Python Modules",
          "Development Status :: 3 - Alpha",
          "Intended Audience :: Developers",
          "Intended Audience :: End Users/Desktop",
          "Operating System :: OS Independent",
          "License :: OSI Approved :: MIT License",
          "Programming Language :: Python :: 3.5",
          "Programming Language :: Python :: 2.7",
          "Topic :: Internet :: WWW/HTTP",
          "Environment :: Console"
      ],
      )
