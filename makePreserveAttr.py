import sys
import os
from os.path import expanduser
from os import fdopen, remove
from tempfile import mkstemp
from shutil import move
import subprocess


class FileUtils:

    def replace(file_path, pattern, subst):
        #   Create temp file
        fh, abs_path = mkstemp()
        with fdopen(fh, 'w') as new_file:
            with open(file_path) as old_file:
                for line in old_file:
                    new_file.write(line.replace(pattern, subst))
        #   Remove original file
        remove(file_path)
        #   Move new file
        move(abs_path, file_path)


class Shell:

    def execute(cmd):
        try:
            output = subprocess.check_output(cmd, stderr=subprocess.STDOUT, shell=True,
                                             universal_newlines=True)
        except subprocess.CalledProcessError as exc:
            print("Status : FAIL" + "\nreturncode: " + str(exc.returncode) + "\nmessage: " + str(exc.output))
        else:
            return output


def isCommandInBashRc(commandName, bashRcPath):
    result = Shell.execute("cat \""+bashRcPath+"\" | grep -i 'alias' | grep -i \"" + commandName+"\" || true")
    if not result:
        return False
    else:
        return True


def generateBashRcEntry(commandPath, commandName, bashRcPath, templatePath):
    bashFunctionName = commandName + "ReplacementFunction"
    tempFilePath = "/tmp/bashRcEntryTemp.txt"
    Shell.execute("cp \""+templatePath+"\" "+tempFilePath)
    FileUtils.replace(tempFilePath, "<COMMAND_NAME>", commandName)
    FileUtils.replace(tempFilePath, "<COMMAND_PATH>", commandPath)
    FileUtils.replace(tempFilePath, "<FUNCTION_NAME>", bashFunctionName)
    return Shell.execute("cat \""+tempFilePath+"\" >> \""+bashRcPath+"\"")


if len(sys.argv) < 2:
    print("commandPath must be specified")
    exit(1)

commandPath = sys.argv[1]
commandBinaryExists = os.path.isfile(commandPath)
if not commandBinaryExists:
    print("no file found at specified commandPath")
    exit(1)

home = expanduser("~")
commandName = os.path.basename(commandPath)
bashRcPath = home+"/.bashrc"
bashRcExisting = os.path.isfile(bashRcPath)

if not bashRcExisting:
    print(".bashrc file in home dir was not found, please create in order to use this program")
    exit(1)

if isCommandInBashRc(commandName, bashRcPath):
    print("alias for commandName is already set in .bashrc")
    exit(1)

scriptDir = sys.path[0]
generateBashRcEntry(commandPath, commandName, bashRcPath, scriptDir+"/bashRcEntryTemplate")

