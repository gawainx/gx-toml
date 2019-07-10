from setuptools import setup
import setuptools

setup(
        name='gxtoml',
        version='0.1',
        description="gx-toml is a TOML -> object tool",
        author='gawainx',
        author_email='liangyixp@live.cn',
        # packages=['gx-toml'],
        install_requires=['toml'],
        classifiers=[
            "Programming Language :: Python :: 3.7",
            "License :: OSI Approved :: MIT License",
            "Operating System :: OS Independent",
        ],
        packages=setuptools.find_packages(),
)