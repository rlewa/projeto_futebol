import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="projetofutebol",
    version="1.0.0",
    author="...",
    author_email="...",
    description="Impact of news on predicting football matches",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/rlewa/projetofutebol',
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=['ftfy','wget', 'numpy', 'pandas', 'sklearn', 'nltk', 'pattern']
) 
