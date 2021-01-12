import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="taugeometric",
    version="1.0.2",
    author="Mayken Espinoza -  Joseph Avila - Javier Pagalo ",
    author_email="josdavil@espol.edu.ec",
    description="TauGeometric is a set of tools to get the geometric tortuosity from 2D images of porous materials",
    long_description_content_type="text/markdown",
    url="https://github.com/eljosephavila123/taugeomectic",
    download_url='https://pypi.org/project/taugeometric/',
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    
    python_requires='>=3.6',
)
install_requires = [
    'matplotlib==3.3.3',
     ' numpy==1.19.5',
      'porespy==1.3.1'

]


