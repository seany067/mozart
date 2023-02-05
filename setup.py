from setuptools import setup, find_packages

def readme():
    with open('README.md') as f:
        return f.read()

setup(
    name="mozart",
    version="0.0.1",
    author='George Honeywood, Joe Rourke, Finlay Wilson, Sean Escreet',
    author_email='github@honeyfox.uk, joseph.rourke.2019@live.rhul.ac.uk, sean@escreet.co.uk',
    description="Python music framework",
    long_description=readme(),
    url="https://github.com/seany067/mozart",
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.9",
    install_requires=[
        "gensound==0.5.3",
        "numpy==1.24.1",
        "PySide6==6.4.2",
        "librosa==0.9.2",
        "ffmpeg-python==0.2.0"
    ],
    package_dir={'': 'src'},
    packages=find_packages(where="src", include="*"),
    include_package_data=True,
)
