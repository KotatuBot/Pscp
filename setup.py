from setuptools import setup,find_packages

setup(
        name="Pscp",
        version="0.1",
        description="Application that makes scp command easy",
        url="https://github.com/KotatuBot/Pscp",
        packages=find_packages(),
        entry_points={
            'console_scripts':['Pscp = Pscp.ssh_main:main']
            },
        )
