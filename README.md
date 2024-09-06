# encodeDecodeBase64

## Introduction

Based on responses from Jon Clements (https://stackoverflow.com/users/1252759/jon-clements) and MrJedi2U (https://stackoverflow.com/users/5237938/mrjedi2u).

* base64 encode a zip file in Python
  `https://stackoverflow.com/questions/11511705/base64-encode-a-zip-file-in-python`

* Splitting large text file into smaller text files by line numbers using Python
  `https://stackoverflow.com/questions/16289859/splitting-large-text-file-into-smaller-text-files-by-line-numbers-using-python`

## Usage

This Python script was created and tested with version 3.11 on Windows 10 using PowerShell 7 for the command-line.

If/when/maybe I have time I will test on other platforms such as Ubuntu.


## Execution

These examples asume the above PowerShell session. Python must obviously be added to the `$env:PATH` variable. There isn't any limitation imposed on this script that would prevent execution in another environment such as Windows Command Prompt (CMD.EXE), Git Bash for Windows or Bash. Note that this script has not been tested on Unix/Linix/POSIX.


### Encode from original to base64

Note that the resultiing base64 file is about 30% larger when tested on 1 MB and 10 MB files.

`python .\encodeDecodeBase64.py --inFile ".\testfile.zip" --outFile ".\testfile.zip.b64"  --encode y`

### Decode from base64 to original

`python .\encodeDecodeBase64.py --inFile ".\testfile.zip.b64" --outFile ".\testfile_new.zip"  --encode y`

### Test and verify

Using PowerShell `Get-FileHash`.

`$originalFileHash = Get-FileHash -Path ".\testfile.zip"`

`$decodedFileHash = Get-FileHash -Path ".\testfile_new.zip"`

Test to see if these hash values are the same.

`$decodedFileHash.Hash -eq $originalFileHash.Hash`


## Author

Andrew Nagy

https://www.linkedin.com/in/andrew-e-nagy/
