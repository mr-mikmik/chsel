import setuptools

setuptools.setup(
    name="chsel",
    version="0.2.0",
    packages=["chsel"],
    url="https://github.com/UM-ARM-Lab/chsel",
    author='Sheng Zhong',
    author_email='zhsh@umich.edu',
    description="chsel",
    install_requires=[
        'cma',
        'torch',
        'numpy',
        'matplotlib',
        'arm-pytorch-utilities',
        'pytorch-kinematics',
        'pytorch-volumetric',
        'cma',
        'ribs[all]'
    ]
)