import setuptools
import os

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="allegro5",
    version="1.0.4",
    author="Amin Guermazi",
    author_email="mino260806@gmail.com",
    description="Allegro 5 C library wrapped in Python",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: zlib/libpng License",
        "Operating System :: OS Independent",
    ],
    url="https://github.com/liballeg/allegro5/tree/5.0.10-pre/python",
    python_requires='>=3.6',
    data_files=[
#        (r'lib\site-packages\allegro5',[os.path.dirname(__file__) + r'\allegro5\allegro-5.0.10-monolith-mt.dll']),
        (r'lib\site-packages\allegro5\demo',[os.path.dirname(__file__) + r'\allegro5\demo\fixed_font.tga'])
        ],
)
