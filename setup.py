from setuptools import setup, find_packages


setup(name='ppwned',
      version='0.2.1',
      description='Check if you have an account that'
      'has been compromised in a data breach',
      url='https://github.com/yuriifreire/pywned',
      author='Yuri Freire',
      author_email='yuriifreire@gmail.com',
      license='None',
      packages=find_packages(exclude=['tests*']),
      install_requires=[
          'requests',
      ],
      entry_points={'console_scripts': ['pwned = pwned:main']},
      zip_safe=False)
