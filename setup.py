from setuptools import setup

setup(name='richy',
      version='0.45b0',
      description='Personal assistant for GNU/Linux.',
      url='https://github.com/MichPCX/richy',
      author='michpcx',
      author_email='michpcx@protonmail.ch',
      license='GNU',
      py_modules=['richy_main'],
      entry_points={
               'console_scripts': ['richy=richy_main:main'],
           },
      install_requires=[
          'guessit<2',
          'terminaltables',
          'tqdm',
          'colorama',
	      'wikipedia'
      ],
      keywords=['richy', 'personal', 'assistant', 'linux', 'python'],
      classifiers=[
          'Environment :: Console',
          'License :: GNU License',
          'Operating System :: MacOS :: MacOS X',
          'Operating System :: Unix',
          'Operating System :: POSIX',
          'Programming Language :: Python',
          'Programming Language :: Python :: 2.7',
          'Programming Language :: Python :: 3.4',
          'Programming Language :: Python :: 3.5',
          'Topic :: Utilities',
          'Topic :: Software Development :: Libraries :: Python Modules',
          'Topic :: Software Development :: User Interfaces',
          'Topic :: Software Development :: Version Control',
      ],)
