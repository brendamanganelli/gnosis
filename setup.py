
#python3 -m pip install setuptools
import setuptools

setuptools.setup(
    name="quantlib",
    version="0.1",
    url="#",
    install_requires = ["opencv-python"],
    author_email="",
    packages=setuptools.find_packages(),
    zip_safe=False
)

