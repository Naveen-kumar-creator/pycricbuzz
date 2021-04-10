from setuptools import setup
setup(
  name = 'pycricbuzz',
  packages = ['pycricbuzz'], 
  version = '2.4',
  description = 'A library for fetching live cricket scores from cricbuzz',
  author = 'Shivam Mitra',
  author_email = 'shivamm389@gmail.com',
  license = 'GPLv2',
  url = 'https://github.com/Naveen-kumar-creator/pycricbuzz', 
  download_url = 'https://github.com/Naveen-kumar-creator/pycricbuzz.git', 
  keywords = ['cricket', 'cricbuzz'], 
  install_requires=[
          'requests',
      ],
  classifiers = [],
)
