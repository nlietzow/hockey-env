from setuptools import setup

setup(
    name="hockey",
    version="2.18",
    description="Simple Hockey Environments",
    url="https://github.com/martius-lab",
    author="Georg Martius, Uni Tuebingen, Autonomous Learning",
    author_email="georg.martius@uni-tuebingen.de",
    license="MIT",
    packages=["hockey"],
    python_requires=">=3.10",
    install_requires=[
        "gymnasium[other]~=1.0.0",
        "numpy~=1.26.4",
        "box2d-py~=2.3.8",
        "pygame~=2.6.1",
        "stable-baselines3~=2.4.1",
    ],
    zip_safe=False,
)
