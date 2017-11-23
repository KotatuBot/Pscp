# Pscp

-------------

## Overview

Application that makes scp command easy


## Description

A tool to make it easy to retrieve and upload files using the scp command.  
You can set your user name and host name as your own words

## Usage

**usage**:

      [action] [-r] [-c user@hostname] [-n Register_Keyword] [-from Source_path] [-to Destination_path]

**[action]**: 
         You can specify the following actions

         get:      Retrieve files from remote

         put:      Upload files remotely

         register: Add an alias to omit the user name and host name.
                   Can be used with later -n command

         show:     Display all registered aliases

         help:     You can display the commands you can use

         exit:     You can quit Pscp

**[option]**:
         
         -r:    Recursively perform copy operations (copy in directory)

         -c:    Specify user name and host name (specified by user @ hostname)

         -n:    Use registered alias

         -from: Specify directory path or file path of copy source

         -to:   Specify directory path or file path of copy destination

**[example]**:

         get -c mikan@10.1.13.45 -from /home/TEST/test.txt -to /home/mikan  
             --> Copy test.txt to the mikan user's /home/mikan directory

         get -n rasp -from /home/TEST/test.txt -to /home/mikan  
             --> Copy test.txt to the mikan user's /home/mikan directory using alias rasp

         get -r -c mikan@10.1.13.45 -from /home/kotatu/TEST2 -to /home/mikan  
            --> Copy the TEST2 directory to the mikan user's /home/mikan directory

         put -c mikan@10.1.13.45 -from /home/mikan/test.txt -to /home/TEST  
            --> Upload test.txt in mikan user's /home/mikan directory to /home/TEST

         put -r -c mikan@10.1.13.45 -from /home/mikan/TEST2 -to /home/TEST  
            --> Upload the TEST2 directory of mikan user's /home/mikan to /home/TEST

         register  
            --> Register alias

         show  
            --> Display all registered items

## Installation

    $ pip install paramiko
    $ pip install scp
    $ git clone https://github.com/KotatuBot/Pscp.git
    $ cd Pscp
    $ python setup.py install
    $ Pscp
    You can check arguments with the help

                  ________  ________  ________  ________
                 |\   __  \|\   ____\|\   ____\|\   __  \
                 \ \  \|\  \ \  \___|\ \  \___|\ \  \|\  \
                  \ \   ____\ \_____  \ \  \    \ \   ____
                   \ \  \___|\|____|\  \ \  \____\ \  \___|
                    \ \__\     ____\_\  \ \_______\ \__\
                     \|__|    |\_________\|_______|\|__|
                              \|_________|

    >>> create
    >>> exit

# Licence
[MIT](https://github.com/KotatuBot/Pscp/blob/master/LICENSE.txt)
