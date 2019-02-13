#!/usr/bin/env python
from distutils.core import setup
import slack_emoji_words


def read_files(*filenames):
    """
    Output the contents of one or more files to a single concatenated string.
    """
    output = []
    for filename in filenames:
        f = open(filename)
        try:
            output.append(f.read())
        finally:
            f.close()
    return '\n\n'.join(output)


setup(
    name='slack_emoji_words',
    version=slack_emoji_words.VERSION,
    url='http://github.com/HaoYang0000/slack_emoji_words',
    description='converting words to emoji and printing out to slack ',
    author='Hao Yang',
    author_email='hao.yang@jane.ai',
    platforms=['any'],
    packages=[
        'slack_emoji_words'
    ],
    package_data={'slack_emoji_words': ['docs/*', 'docs/ref/*.rst']},
    classifiers=[
        'Environment :: Web Environment',
    ],
    zip_safe=False,
)