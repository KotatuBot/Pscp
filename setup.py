from setuptools import setup,find_packages

setup(
        name="Pscp",
        version="0.1",
        decription="Application that makes scp command easy",
        url="https://github.com/KotatuBot/Pscp.git",
        pacakges=find_packages(),
        entry_points="""
                     [console_scripts]
                     greet = Pscp.ssh_main:main
                     """,
        )
