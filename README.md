# MPD Filter

Simple HTTP Proxy and attribute filter for MPEG-DASH manifest

## Required libraries and services
- Tested on a Linux system (Debian 11)
- Python 3

## Install
- Just clone the project from the repository
- Adjust `HOST` and `PORT` environment variables in mpdfilter.py

## Run 
- Go to the project directory `cd mpdfilter`
- Run `python mpdproxy.py` 
- Configure the playout for pointing to you

## Limitations:
- Does not support Byte range requests

## Improvements to be done
- Add more support of MPD
- Add support for byte range

