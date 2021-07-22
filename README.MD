_**In the name of Allah**_

# MWXpy

### My tiny Python library

## Documentation

Also there is a video for Persian users:

همچنین یک ویدیو آموزشی برای کاربران فارسی زبان موجوده:

[YouTube](https://www.youtube.com/watch?v=gRPDGZAxpO4) | [Aparat](https://www.aparat.com/v/1DrGC)

#### Installation

`pip install mwx`

### Functions

_function_ **cprint ( color:_str_ , text:_anything_)**

This function prints `text` colored in `color` in command line

`color` must be one of these (case insensitive): `red` :red_circle:  or `green` :green_circle:  or `yellow` :yellow_circle:  or `blue` :large_blue_circle: or `white` :white_circle:  or `cyan` :cyclone:  or `magenta` :purple_circle:  

`text` can be anything.It is the text which will be colored and printed to terminal (command line)

NOTE: `color` is case insensitive so `red`,`RED`,`Red`,`ReD`,`REd`,`rED`,`reD` and `rEd` are same :smile:

**Example:**

```python
from mwx import cprint
cprint('green','In the name of Allah')
```

It will print a green `In the name of Allah`

**Errors:**
* `TypeError` if `color` is not `str`(String)
* `ValueError` if `color` is not in the colors list

***

_function_ **rwjson ( path:_str_ , content:_dict-Optional_=`None` )** :

A simple tool for reading & writing JSON files in a very easy way!

`path` : relative or absolute path to the target JSON file

Returns a `dict` including data of targeted JSON file if `content` = `None` (By default it is `None`)

Writes `content`(If it is a `dict`) into the targeted JSON file.

**Example:**

```python
import mwx
data = {'name':'Amirreza','age':16}
mwxpy.rwjson('test.json',data)
```

It will write `data` to `test.json`

```python
from mwx import rwjson
data = rwjson('test.json')
print(data)
```

It will print the whole thing in `test.json` in format of a python `dict`

   
**Errors**:

* `ValueError` if filename does not end with `.json`

* `FileNotFoundError` if `path` is not a file when you want to read the file (`content = None`)

* `TypeError` if `content` is not `dict` or `None`

***

_function_ **rwfile ( path:_str_ , content:_anything-Optional_=`None` )** :

A simple tool for reading & writing files in a very easy way!

`path` : relative or absolute path of the target file

Returns data of the targeted file if `content` = `None` (By default it is `None`)

Writes `content`(If it is not `None`) into the targeted file.

**Example:**

```python
import mwx
data = 'Hey this is some thing! :)'
mwxpy.rwfile('test.txt',data)
```

It will write `data` to `test.txt`

```python
from mwx import rwfile
data = rwfile('test.txt')
print(data)
```

It will print the whole thing in `test.txt`

   
**Errors**:

* `FileNotFoundError` if `path` is not a file when you want to read the file (`content = None`)

***

_function_ **browse ( path:_str_ , show_hidden_files:_bool-Optional_=`False`)** :

A nice simple file explorer

Returns the information of files that exist in target directory in this way(i.e):

```python
{'drives': [], 'folders': [{'name':'test1','type':'folder'},{'name':'test2','type':'folder'}], 'files': [{'name':'test.py','type':'python'}], 'links': [], 'unknowns': []}
```
`path`: relative or absolute path of target directory

If `show_hidden_files` is `True` the result will include Unix hidden file(starting with `.`) and if not result won't include.(By default it is `Flase`)

**Supported types & extentions:**

They are in this way: 
```json
{"type1":[".extention1",".extention2"],"type2": ...
```
:

```json
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
                ]
            }
```

Other types: `file`(for unsupported file types) `folder`(for folders) `drive`(for drives) `link`(for links) `unknown`(for unknowns)

**Example:**

```python
from mwx import browse
print(browse('folder1/folder2'))
```
```python
import mwx
content = mwxpy.browse('/tmp/sub/test',True)
```

The second one will include hidden files too

**Errors:**

* `ValueError` if `path` is not a directory
