
import os
from glob import glob
from setuptools import find_packages, setup

package_name = 'cvxcv'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        # Install marker file in the package index
        ('share/ament_index/resource_index/packages', ['resource/' + package_name]),
        # Include our package.xml file
        (os.path.join('share', package_name), ['package.xml']),
        # Include all launch files.
        (os.path.join('share', package_name, 'launch'), glob(os.path.join('launch', '*launch.[pxy][yma]*'))),
    ],
    # customize setup.py configuration below
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='Name',
    maintainer_email='your@email.com',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    # end setup.py custom configuration
    entry_points={
        'console_scripts': [
            'node1 = cvxcv.Node1:main',

          # add custom entry points below
          # end custom entry points
        ],
    },
)
    