from setuptools import find_packages, setup

package_name = 'saf_tcpserver'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='mathias',
    maintainer_email='mathiasaskhansen04@gmail.com',
    description='Publishing and listening to data recieved from a PLC via TCP',
    license='Apache-2.0',
    extras_require={
        'test': [
            'pytest',
        ],
    },

    entry_points={
        'console_scripts': [
            'server_node = saf_tcpserver.publisher:main',
            'logger_node = saf_tcpserver.subscriber:main',
        ],
},
)
