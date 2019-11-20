from setuptools import setup, find_packages
from microverse_battery.version import __version__

with open("README.rst") as readme_file:
    readme = readme_file.read()

setup(
    name="microverse-battery",
    version=__version__,
    url="https://github.com/balanceofprobability/microverse-battery",
    license="MIT",
    author="John Harrison",
    author_email="balanceofprobability@gmail.com",
    description="You can't just add a sci-fi word to a car word and hope it means something",
    long_description=__doc__,
    packages=find_packages(exclude=["tests"]),
    include_package_data=True,
    zip_safe=False,
    platforms="any",
    install_requires=[
        'Click',
        'pyautogui',
        'tbselenium',
        'toml',
    ],
    entry_points={
        "console_scripts": [
            "microverse = microverse_battery.microverse:cli",
            "miniverse = microverse_battery.miniverse:main",
        ]
    },
    classifiers=[
        # As from http://pypi.python.org/pypi?%3Aaction=list_classifiers
        # 'Development Status :: 1 - Planning',
        # 'Development Status :: 2 - Pre-Alpha',
        'Development Status :: 3 - Alpha',
        # 'Development Status :: 4 - Beta',
        # 'Development Status :: 5 - Production/Stable',
        # 'Development Status :: 6 - Mature',
        # 'Development Status :: 7 - Inactive',
        "Environment :: Console",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: BSD License",
        "Operating System :: POSIX",
        "Operating System :: MacOS",
        "Operating System :: Unix",
        "Operating System :: Microsoft :: Windows",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 3",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
)
