'''
Inspired by code and comments in the following StackOverflow article:

base64 encode a zip file in Python
https://stackoverflow.com/questions/11511705/base64-encode-a-zip-file-in-python
'''


# Parsing boolean values with argparse
# https://stackoverflow.com/questions/15008758/parsing-boolean-values-with-argparse
def str2bool(v):
    if isinstance(v, bool):
       return v
    if v.lower() in ('yes', 'true', 't', 'y', '1'):
        return True
    elif v.lower() in ('no', 'false', 'f', 'n', '0'):
        return False
    else:
        raise argparse.ArgumentTypeError('Boolean value expected.')


import argparse
import base64
import os
from pathlib import Path


def Python3Encode( inFilePath , outFilePath ):
    # Python 3
    with open( inFilePath , 'rb' ) as fin, open( outFilePath , 'wb') as fout:
        base64.encode(fin, fout)

def Python3Decode( inFilePath , outFilePath ):
    # Python 3
    with open( inFilePath , 'rb') as fin, open( outFilePath , 'wb') as fout:
        base64.decode(fin, fout)


# https://docs.python.org/3.7/library/argparse.html
parser = argparse.ArgumentParser( description='Encode input file to base64 or decode base64 file to outputfile. Based on https://stackoverflow.com/questions/11511705/base64-encode-a-zip-file-in-python.')
parser.add_argument('--inFile',   type=argparse.FileType('rb'),                  nargs='+',              metavar='inFile',  help='Name of input file.' )
parser.add_argument('--outFile',  type=argparse.FileType('wb'),                                          metavar='outFile', help='Name of output file.' )
parser.add_argument('--encode',   type=str2bool,                 default=False,  nargs='?', const=False,                    help='Encode the file to base64.' )
parser.add_argument('--decode',   type=str2bool,                 default=False,  nargs='?', const=False,                    help='Decode the file from base64.' )

args = parser.parse_args()
inputFile    = args.inFile
outputFile   = args.outFile
actionEncode = args.encode
actionDecode = args.decode

if inputFile is None:
    print( "ERROR: no input file namespecified. Exiting script '" + os.path.basename(__file__) + "'." )
    # https://stackoverflow.com/questions/19747371/python-exit-commands-why-so-many-and-when-should-each-be-used
    raise SystemExit

#print( "" )
#print( f"inputFile          = {inputFile},         type = {type(inputFile)}" )
#print( f"inputFile[0]       = {inputFile[0]},      type = {type(inputFile[0])}" )
#print( f"inputFile[0].name  = {inputFile[0].name}, type = {type(inputFile[0].name)}" )

# https://stackoverflow.com/questions/82831/how-do-i-check-whether-a-file-exists-without-exceptions
inputFileOsPath = Path( inputFile[0].name )

#print( f"inputFileOsPath    = {inputFileOsPath},         type = {type(inputFileOsPath)}" )

if inputFileOsPath.is_file():
    # file exists
    print( f"Found input file {inputFileOsPath}." )
else:
    print( f"ERROR: Not found input file {inputFileOsPath[0].name}. Exiting script '" + os.path.basename(__file__) + "'."  )
    raise SystemExit


if outputFile is None:
    print( "ERROR: no output file namespecified. Exiting script '" + os.path.basename(__file__) + "'." )
    # https://stackoverflow.com/questions/19747371/python-exit-commands-why-so-many-and-when-should-each-be-used
    raise SystemExit

#print( "" )
#print( f"outputFile          = {outputFile}" )
#print( f"outputFile          = {outputFile},         type = {type(outputFile)}" )
#print( f"outputFile.name     = {outputFile.name},    type = {type(outputFile.name)}" )

outputFileOsPath = Path( outputFile.name )
#print( f"outputFileOsPath    = {outputFileOsPath}" )

if outputFileOsPath.is_file():
    # file exists
    print( f"Found input file {outputFileOsPath}." )
else:
    print( f"ERROR: Not found input file {outputFileOsPath}. Exiting script '" + os.path.basename(__file__) + "'."  )
    raise SystemExit


if actionEncode and not actionDecode:
    doEncode = True
elif not actionEncode and actionDecode:
    doEncode = False
else:
    print( "ERROR: either actionEncode or actionDecode must be true/yes. Exiting script '" + os.path.basename(__file__) + "'." )
    # https://stackoverflow.com/questions/19747371/python-exit-commands-why-so-many-and-when-should-each-be-used
    raise SystemExit

#print( "" )
#print( f"inputFileOsPath     = {inputFileOsPath}" )
#print( f"outputFileOsPath    = {outputFileOsPath}" )
#print( f"actionEncode        = {actionEncode}" )
#print( f"actionDecode        = {actionDecode}" )
#print( f"doEncode            = {doEncode}" )

if doEncode:
    Python3Encode( inputFileOsPath , outputFileOsPath )
else:
    Python3Decode( inputFileOsPath , outputFileOsPath )

print( "Done." )
