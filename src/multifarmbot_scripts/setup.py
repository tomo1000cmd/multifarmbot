from setuptools import setup

package_name = 'multifarmbot_scripts'

setup(
    name=package_name,
    version='0.0.1',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='emmanuel tomo',
    maintainer_email='tomoemmanuel@gmail.com',
    description='Scripts package for multifarmbot',
    license='Apache-2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'example_script = multifarmbot_scripts.example_script:main',
        ],
    },
)