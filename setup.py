import setuptools

with open("README.markdown", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="devnullaas",
    version="1.0.0",
    author="codl",
    author_email="codl@codl.fr",
    description=
    "Discard data through devnull-as-a-service.com and other DAAS",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=setuptools.find_packages(),
    classifiers=(
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
    ),
    install_requires=('requests', ),
    url="https://github.com/codl/py-devnullaas",
)
