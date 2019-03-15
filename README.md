# XAttrPreserver
simple python script for making a specific command-line program preserve xAttr (extended File Attributes) of all files given as an commandline-argument to it

USAGE:
  python3.5 makePreserveAttr.py <absolute/Path/To/Program>
  #the specified program must be in your PATH

EXAMPLE:
  python3.5 makePreserveAttr.py /usr/bin/vi
  #now 'vi testFile.txt'  wont remove the extended File Attributes of testFile.txt anymore

HOW IT WORKS:
  Creates an alias of the programname in your .bashrc running a bashfunction instead of the original program.
  The bashfunction saves the xattributes of all files, given as an commandline-argument to the program, to tempfiles.
  The bashfunction will then run the original program and restore all saved xattributes.

WARNING:
  Create a backup of your .bashrc file before using! (cat ~/.bashrc > ~/.bashrc.bak).
  This is bad python and only tested with python3.5 on Ubuntu 16.04.
  If something goes wrong just restore you .bashrc or delete the entries in it yourself.
