from setuptools import setup, find_packages

setup(
    name='gangagsoc',
    packages=find_packages(),
    version='v2024',
    license='gpl-3.0',
    description='The Challenge for GSoC 2024 student to participate in the Ganga project',
    author='Ulrik Egede',
    author_email='ulrik.egede@monash.edu',
    url='https://github.com/ganga-devs/GangaGSoC2024',
    keywords=['GSoC', 'Ganga', 'Challenge'],
    install_requires=[
        'pytest>=8.3.5',
        'ganga>=8.7.9',
        'google-generativeai>=0.8.4',
        'pytest-cov>=4.1.0',
        'aiofile>=3.8.8',
        'PyPDF2>=3.0.0',
        'black>=24.2.0',
        'isort>=5.13.2',
        'pylint>=3.0.3',
    ],
    python_requires='>=3.11',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: GNU General Public License v3.0',
        'Programming Language :: Python :: 3.11',
        'Programming Language :: Python :: 3.12',
    ],
)