from setuptools import setup, find_packages

with open("README.md", "r") as f:
    long_description = f.read()

setup(
    name="s2tutil",
    version="0.0.2",
    description="Audio to text transcription utility using whisper.cpp models",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Juewei Dong",
    author_email="juewei.dong@brainco.tech",
    url="https://github.com/DavidSonoda/s2tutil",
    license="MIT",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
    ],
    python_requires=">=3.7",
    packages=find_packages(),
    entry_points={
        "console_scripts": [
            "s2tutil = s2tutil.__main__:main",
        ],
    },
    install_requires=[
        "whispercpp@git+https://github.com/aarnphm/whispercpp.git@v0.0.17#egg=whispercpp",
        "click==8.1.3",
    ],
)
