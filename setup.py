# In the name of Allah

from distutils.core import setup

setup(
  name = 'mwxpy',
  packages = ['mwxgaf','mwx','mwxpy'],
  version = '1.0',
  license='MIT',  
  description = 'MWXGAF\'s personal library',
  author = 'MWX',
  author_email = 'mwxgaf@yahoo.com',
  url = 'http://mwxgaf.ir',
  download_url = 'https://github.com/mwxgaf/mwxpy/archive/v1.tar.gz',
  keywords = ['python', 'mwxgaf', 'mwx'],   
  install_requires=[],
  long_description="In the name of Allah\n\n MWXpy\n\nDocumentation available at:\n\ngithub.com/mwxgaf/mwxpy/wiki",
  long_description_content_type='text/markdown',
  classifiers=[
    'Development Status :: 5 - Production/Stable',
    'Intended Audience :: Developers',
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.7',
    'Programming Language :: Python :: 3.8',
    'Programming Language :: Python :: 3.9',
  ],
)