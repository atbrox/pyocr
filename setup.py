#!/usr/bin/env python

from setuptools import setup

setup(name="pyocr",
      version="0.1.2-git",
      description="A Python wrapper for OCR engines (Tesseract, Cuneiform, etc)",
      keywords="tesseract cuneiform ocr",
      url="https://github.com/jflesch/pyocr",
      download_url="https://github.com/jflesch/pyocr/archive/v0.1.2.zip",
      classifiers=[
          "Development Status :: 5 - Production/Stable",
          "Intended Audience :: Developers",
          "License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)",
          "Operating System :: POSIX :: Linux",
          "Programming Language :: Python :: 2.7",
          "Topic :: Multimedia :: Graphics :: Capture :: Scanners",
          "Topic :: Multimedia :: Graphics :: Graphics Conversion",
          "Topic :: Scientific/Engineering :: Image Recognition",
      ],
      license="GPLv3+",
      author="Jerome Flesch",
      author_email="jflesch@gmail.com",
      packages=['pyocr'],
      package_dir={ 'pyocr': 'src' },
      data_files=[],
      scripts=[],
      # pyocr can use Pillow or PIL objects
      install_requires=[],
     )

