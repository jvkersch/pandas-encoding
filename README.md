Pandas encoding
===============

_Import Pandas the way nature intended!_

Python has strict rules of what a valid identifier can be, and these rules
preclude using emojis anywhere in an identifier. This makes it impossible to
use the oh-so-natural `import pandas as 🐼` to import the
[pandas](https://pandas.pydata.org/) library.

Disclaimer
----------

This is not a serious project. Don't let this code come anywhere near
production environments, don't upload to PyPI, etc.

Howto
-----

Install `pandas.py` in the `encodings` folder inside your Python environment,
and then just set the `PYTHONIOENCODING` environment variable to `pandas` to
enable full compatibility with the majestic giant Panda:


```
$ PYTHONIOENCODING=pandas python
Python 3.6.7 (tags/v3.6.7:6ec5cf24b7, Feb 16 2019, 22:29:37) 
[GCC 7.3.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> import pandas as 🐼
>>> df = 🐼.DataFrame()
>>> df
Empty DataFrame
Columns: []
Index: []
```

You can also use this encoding directly, by including the line `# -*- coding:
pandas -*-` at the top of your script:

```
$ cat example.py 
# -*- coding: pandas -*-

import pandas as 🐼

df = 🐼.DataFrame()
print(df)

$ python example.py 
Empty DataFrame
Columns: []
Index: []

```

Concept
-------

The idea for this was pioneered by the visionary [Marc
Garcia](https://twitter.com/datapythonista) in a [lightning talk at SciPy
2019](https://www.youtube.com/watch?v=Atc3yw9OdxY&index=96&list=PLYx7XA2nY5Gd-tNhm79CNMe_qvi35PgUR). The
idea of using Python encodings for unholy purposes comes from the
[nocolon](https://github.com/paradoxxxzero/nocolon) package (which uses it to
do away with trailing colons in Python code). The code itself was modeled after
the punycode module bundled with the Python interpreter.
