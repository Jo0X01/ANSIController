from setuptools import setup

__author__ = "JoOx01"
__pkg_name__ = "ANSIController"
__version__ = "1.1.1"
__desc__ = """Basic Python Module to control & color & style text in terminal"""

with open('README.md', 'r', encoding='utf-8') as f:
    long_description = f.read()

setup(
    name=__pkg_name__,
    packages=[__pkg_name__],
    version=__version__,
    license='MIT',
    description=__desc__,
    author=__author__,
    long_description=long_description,
    long_description_content_type='text/markdown',
    # author_email='forsell450@gmail.com',
    url='https://github.com/jo0x01/ansicontroller',
    keywords=[
        'cmd',
        'ansi',
        'terminal',
        'ansi_terminal',
        'ANSIControl',
        'ANSIController',
        'ASNI',
        'ansicontroller',
        'ansi_escape'
    ],
    install_requires=['keyboard'],
    entry_points={
        'console_scripts': [
            'ansicontroller = ANSIController.__main__:main'
        ]
    },
    classifiers=[
        # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
        'Development Status :: 3 - Alpha',
        'Environment :: Console',
        'Environment :: Console :: Curses',
        'Environment :: Console :: Framebuffer',
        'Environment :: Console :: Newt',
        'Intended Audience :: Developers',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',
        "Operating System :: OS Independent",
    ],
)
