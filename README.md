# X-attr-preserver
Simple python script for making a specific command-line program preserve xAttr (extended File Attributes)  
of all files given as an commandline-argument to it.  
  
## Usage:  
* create a backup of your .bashrc file before using with `cat ~/.bashrc > ~/.bashrc.bak`    
* `python3.5 makePreserveAttr.py <absolute/Path/To/Program>`   
* the specified program must be in your PATH    
* restart your terminal so the changes take place    


## Example:  
  
* `python3.5 makePreserveAttr.py /usr/bin/vi`  
* now `vi testFile.txt`  wont remove the extended File Attributes of testFile.txt anymore  
  
## How it wokrs:  
  
* Creates an alias of the programname in your .bashrc running a bashfunction instead of the original program.  
* The bashfunction saves the xattributes of all files, given as an commandline-argument to the program, to tempfiles.  
* The bashfunction will then run the original program and restore all saved xattributes.  
  
  
## Requirements:  
  
* Python3.5,   
* clitools: getfattr, setfattr (install with: `sudo apt install attr`)  
