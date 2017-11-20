from setuptools import setup,find_packages

setup(
        name="Pscp",
        version="0.1",
        decription="Application that makes scp command easy",
        url="https://github.com/KotatuBot/Pscp",
<<<<<<< HEAD
        pacakges=["Pscp"],
        entry_points={
            'console_scripts': [
                'Pscp = Pscp.__main__:main'
                ]
            },
=======
        pacakges=find_packages(),
        entry_points="""
                     [console_scripts]
                     Pscp = ssh_main.py:main
                     """,
>>>>>>> parent of 3735da8... test
        )
