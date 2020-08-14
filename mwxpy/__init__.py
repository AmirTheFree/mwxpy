# In the name of Allah

__doc__ = 'MWX Python Utils'

import os
import json
import sys

def rwfile(path, content=None):
    '''
    path:str | content:any=None(optional)

    Returns the data of file that located in path if content=None

    Writes content to the file that located in path if content is not None
    '''
    if content == None:
        if not os.path.isfile(path):
            raise FileNotFoundError
        fp = open(path,'r')
        data = fp.read()
        fp.close()
        return data
    fp = open(path,'w')
    fp.write(str(content))
    fp.close()

def rwjson(path, content=None):
    '''
    path:str | content:dict=None(optional)

    Returns a dict including data of JSON file that located in path if content=None

    Writes content to the JSON file located in path if content is a dict.
    '''
    if not path.endswith('.json'):
        raise ValueError('Only JSON files allowed')
    if not content:
        if not os.path.isfile(path):
            raise FileNotFoundError
        fp = open(path, 'r')
        data = json.load(fp)
        fp.close()
        return data
    if not isinstance(content, dict):
        raise TypeError('Only dictionaries allowed as content')
    fp = open(path, 'w')
    json.dump(content, fp)
    fp.close()


def browse(path,show_hidden_files = False):
    '''
    path:str | show_hidden_files:bool=False(optional)

    Returns a dict including information of items that located in path

    It will aslo include Unix hidden files (starting with .) if show_hidden_files is True
    '''
    result = {'drives': [], 'folders': [],
              'files': [], 'links': [], 'unknowns': []}
    if not os.path.isdir(path):
        return ValueError('Path not found!')
    for i in sorted(os.listdir(path), key=str.lower):
        if i.startswith('.'):
            if show_hidden_files:
                pass
            else:
                continue
        if os.path.ismount(os.path.join(path, i)):
            result['drives'].append({'name': i, 'type': 'drive'})
        elif os.path.islink(os.path.join(path, i)):
            result['links'].append({'name': i, 'type': 'link'})
        elif os.path.isdir(os.path.join(path, i)):
            result['folders'].append({'name': i, 'type': 'folder'})
        elif os.path.isfile(os.path.join(path, i)):
            extentions = {
                "css": [
                    ".css",
                    ".sass",
                    ".scss"
                ],
                "database": [
                    ".db",
                    ".sqlite3",
                    ".sqlite",
                    ".sql"
                ],
                "html": [
                    ".html",
                    ".htm"
                ],
                "image": [
                    ".png",
                    ".jpg",
                    ".jpeg",
                    ".svg",
                    ".bmp",
                    ".webp",
                    ".ico"
                ],
                "zip": [
                    ".zip",
                    ".rar",
                    ".tar",
                    ".taz",
                    ".tar.xz"
                ],
                "video": [
                    ".mp4",
                    ".avi",
                    ".wmv",
                    ".mkv",
                    ".gif",
                    ".ogg",
                    ".vob",
                    ".flv",
                    "webm",
                    ".ogv",
                    ".mov",
                    ".3gp",
                    ".m4v"
                ],
                "audio": [
                    ".mp3",
                    ".wav",
                    ".m4a",
                    ".ogg",
                    ".wma",
                    ".mp4a"
                ],
                "python": [
                    ".py"
                ],
                "txt": [
                    ".txt"
                ],
                "javascript": [
                    ".js"
                ],
                "json": [
                    ".json"
                ],
                "php": [
                    ".php"
                ],
                "pdf": [
                    ".pdf"
                ],
                "bash": [
                    ".sh"
                ],
                "spreadshit": [
                    ".xls",
                    ".xlsx",
                    ".xlsm",
                    ".xlsb",
                    ".ods"
                ],
                "presentation": [
                    ".ppt",
                    ".pptx",
                    ".odp"
                ],
                "document": [
                    ".docx",
                    ".doc",
                    ".odt",
                ],
            }
            for e in extentions:
                for s in extentions[e]:
                    if i.lower().endswith(s):
                        result['files'].append({'name': i, 'type': e})
            recongnized = False
            for f in result['files']:
                if i == f['name']:
                    recongnized = True
                    break
            if not recongnized:
                result['files'].append({'name': i, 'type': 'file'})
        else:
            result['unknowns'].append({'name': i, 'type': 'unknown'})
    return result

def cprint(color,text):
    '''
    color:str | text:any

    Prints the text painted in color in terminal, command line, ...
    '''
    colors = {
    'RED': '\033[1;31m',
    'GREEN': '\033[1;32m',
    'YELLOW': '\033[1;33m',
    'MAGENTA': '\033[1;35m',
    'BLUE': '\033[1;34m',
    'CYAN': '\033[1;36m',
    'WHITE': '\033[1;37m'
}
    if not isinstance(color,str):
        raise TypeError('Color name must be string')
    try:
        color_capital = color.upper()
        colors[color_capital]
        sys.stdout.write(colors[color_capital])
        print(text)
    except KeyError:
        raise ValueError('No such color')
    except Exception as e:
        print(e)
