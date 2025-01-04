from setuptools import find_packages,setup 
# it will check for all the packages in the entire ML app in the dir we created.
from typing import List

HYPEN_E_DOT='-e .' #global constant
def get_requirements(file_path:str)->List[str]:
    '''
      this function will return the list of requirements
    '''

    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace('\n','') for req in requirements]

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)

    return requirements

#meta data
setup(
    name = 'mlproject',
    version= '0.0.1',
    author= 'Husna',
    author_email= 'husnariyaz96@gmail.com',
    packages=find_packages(),
    #install_requires=['pandas','numpy','seaborn']
    install_requires=get_requirements('requirements.txt')
)

