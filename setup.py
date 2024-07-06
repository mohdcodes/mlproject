from setuptools import find_packages, setup
from typing import List

HYPEN_E_DOT = "-e ."
def get_requirements(filePath:str)->list[str]:
    '''
    THIS FUNCTION WILL RETURN THE REQUIREMENTS. 
    '''
    requirements = []
    with open(filePath) as  fileObj:
        requirements = fileObj.readlines()
        requirements = [req.replace("\n", "") for req in requirements]
        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
    return requirements
                                
                                                            
setup(
    name = 'mlproject',
    version='0.0.1',
    author='ArbaazCode',
    author_email='arbaazcode@gmail.com',
    packages=find_packages(),
    install_requires = get_requirements('requirements.txt')
)
