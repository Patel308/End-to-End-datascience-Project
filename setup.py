from setuptools import find_packages,setup
from typing import List 

hypen_e_dot = '-e .'

def get_requirements(path:str)->List[str]:
    requirements = []
    with open(path) as obj:
        requirements =  obj.readlines()
        requirements =  [req.replace('\n', '') for req in requirements]
        if hypen_e_dot in requirements:
            requirements.remove(hypen_e_dot)

    return requirements        


setup(
    name='MlProject',
    version = '0.1',
    author='Deepesh Patel',
    author_email="techiedeepeshpatel@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)