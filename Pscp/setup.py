from setuptools import setup

setup(
        name="Pscp",
        version="0.1",
        decription="Application that makes scp command easy",
        url="https://github.com/KotatuBot/Pscp",
        pacakges=["Pscp"],
        py_modules=['Pscp'],
        entry_points={
            'console_scripts': [
                'Pscp = Pscp:main'
                ]
            },
        )
