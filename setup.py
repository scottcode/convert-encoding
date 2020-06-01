from setuptools import setup, find_packages


if __name__ == '__main__':
    setup(
        name='convencode',
        version="0.1.0",
        description="Utiliity to convert text file encoding",
        author="Scott Hajek",
        packages=find_packages(),
        entry_points={
            'console_scripts': [
                "convencode = convencode:main"
            ]
        }
    )
