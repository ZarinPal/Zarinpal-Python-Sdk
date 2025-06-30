from setuptools import setup, find_packages

setup(
    name='zarinpal-py-sdk',               
    version='0.1.3',                      
    packages=find_packages(where="src/zarinpal-py-sdk"), 
    include_package_data=True,  
    py_modules=['zarinpal'],   
    package_dir={"": "src/zarinpal-py-sdk"},              
    install_requires=[
        "pytest==8.3.4",
        "Requests==2.32.4",
        "requests_mock==1.12.1",
        "setuptools==75.8.0"
    ],
    author='Iman Attary',                   
    author_email='imanattary@gmail.com',
    description='A Python SDK for Zarinpal Payment Gateway',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/ImanAttary/zarinpal_py_sdk',  
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.12',              
)