from setuptools import setup, find_packages

setup(
  name = 'q-transformer',
  packages = find_packages(exclude=[]),
  version = '0.0.1',
  license='MIT',
  description = 'Q-Transformer',
  author = 'Phil Wang',
  author_email = 'lucidrains@gmail.com',
  long_description_content_type = 'text/markdown',
  url = 'https://github.com/lucidrains/q-transformer',
  keywords = [
    'artificial intelligence',
    'deep learning',
    'attention mechanisms',
    'transformers',
    'q-learning'
  ],
  install_requires=[
    'einops>=0.6.1',
    'robotic-transformer-pytorch>=0.1.0',
    'torch>=1.12'
  ],
  classifiers=[
    'Development Status :: 4 - Beta',
    'Intended Audience :: Developers',
    'Topic :: Scientific/Engineering :: Artificial Intelligence',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3.6',
  ],
)
