Encoding Converter
==================

Command line utility for converting a text file of one 
standard encoding to another. 

## Installation
```shell script
python setup.py install
```

## Usage
Display help
```shell script
convencode -h
```

Convert encoding in a file
```shell script
convencode in_file_path in_encoding out_file_path out_encoding
```

For the encodings, use same kind of string you would use when 
using the python `open()` command: 'utf-8', 'utf-16', etc.
