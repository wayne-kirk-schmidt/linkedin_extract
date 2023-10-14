LinkedIn Extract
================

Want to pull out LinkedIn profiles from a file that you have, but are having a challenge?

This script is designed to help you do just that, get a list of profiles from a text file.

Installing the Scripts
=======================

This script can be used as a standelone or you can pull the logic into other software if you wish.

Each script is written in python3 and currently relies on default libraries within python.

To install, you can do the following: 

    1. Download and install python 3.6 or higher from python.org. Append python3 to the LIB and PATH env.

    2. Download and install git for your platform if you don't already have it installed.
       It can be downloaded from https://git-scm.com/downloads
    
    3. Open a new shell/command prompt. It must be new since only a new shell will include the new python 
       path that was created in step 1. Change to the folder where you want to install the scripts.
    
    4. Execute the following command to install pipenv, which will manage all of the library dependencies:
    
        sudo -H pip3 install pipenv 

    5. Clone this repository. This will create a new folder
    

    6. Change into this folder. Type the following to install all the package dependencies 
       (this may take a while as this will download all of the libraries it uses):

        pipenv install
        
Dependencies
============

As of now, no dependencies, though they will be located within the Pipfile if required.

Script Names and Purposes
=========================

The scripts are organized into sub directories:

    1. ./bin - has all of the scripts here

            ./bin/linkedin_extract.py

    2. ./doc - this has a quick explanation of how to save and extract profile URLs.

NOTE: The documentation will show how to extract using this script, ChatGPT, and potentially other methods.

Examples
========

```
            prompt> python3 ./bin/linkedin_extract.py /some/path/to/a/linkedin/profiles/sample_file.py 
https://www.linkedin.com/in/waynekirkschmidt/
```

To Do List:
===========

* Add output into CSV and other formats
* Add options and arguments to send connect requests if possible

License
=======

Copyright 2023 

* Wayne Kirk Schmidt (wayne.kirk.schmidt@changeis.co.jp)

Licensed under the Apache 2.0 License (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    license-name   Apache 2.0 
    license-url    https://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.

Support
=======

Feel free to e-mail me with issues to: 

+   wayne.kirk.schmnidt@gmail.com
+   wayne.kirk.schmnidt@changeis.co.jp

I will provide "best effort" fixes and extend the scripts.
