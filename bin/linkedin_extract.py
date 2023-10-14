#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Exaplanation: linkedin_extract. Quick way to get LinkedIn profiles from a saved file

Usage:
   $ python  linkedin_extract  [ file ]

Style:
   Google Python Style Guide:
   http://google.github.io/styleguide/pyguide.html

    @name           linkedin_extract
    @version        1.00
    @author-name    Wayne Kirk Schmidt
    @author-email   wayne.kirk.schmidt@changeis.co.jp
    @license-name   Apache-2.0
    @license-url    https://www.apache.org/licenses/LICENSE-2.0
"""

__version__ = 1.00
__author__ = "Wayne Kirk Schmidt (wayne.kirk.schmidt@changeis.co.jp)"

import re
import sys
sys.dont_write_bytecode = 1

def extract_linkedin_urls(mytext):
    """
    use regular expressions to extract and clean the linkedin profile URL
    """
    urlpattern = r'(\S*linkedin\.com\S*)'
    linkedin_strings = re.findall(urlpattern, mytext)

    cleaned_linkedin_urls = []
    for linkedin_string in linkedin_strings:
        linkedin_string = re.sub(r'^.*?(www|http)', r'\1', linkedin_string)
        if linkedin_string.startswith("linkedin.com"):
            cleaned_linkedin_urls.append("https://www." + linkedin_string)
        elif linkedin_string.startswith("www."):
            cleaned_linkedin_urls.append("https://" + linkedin_string)
        elif linkedin_string.startswith("http://"):
            cleaned_linkedin_urls.append(linkedin_string.replace("http://", "https://"))
        else:
            cleaned_linkedin_urls.append(linkedin_string)

    return cleaned_linkedin_urls

INPUTFILE = sys.argv[1]

with open(INPUTFILE, 'r', encoding='UTF-8') as targetfile:
    file_contents = targetfile.read()

linkedin_urls = extract_linkedin_urls(file_contents)

for url in list(set(linkedin_urls)):
    print(url)
