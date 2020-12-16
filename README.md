# pdf-word-highlighter
Small Python script to highlight words in a pdf. Takes either a word or .txt file as input and highlights every instance of those words in the PDF. Options for custom colors and output paths.

Works with both Python 2 and 3.

# Dependecies
PyMuPDF

```pip install pymupdf```

# Usage
```python3 pdf-wordhighlighter.py [-h] [-w WORD] [-wl WORDLIST] [-o OUTPUT] [-c COLOR] pdf```

Automatically highlight keywords in a PDF

## positional arguments:
  `pdf`                   path to the pdf

 ## optional arguments:
  `-h, --help`           
  
  show this help message and exit
  
  `-w WORD, --word WORD`  
  
  word to highlight, can be called multiple 
  
  `-wl WORDLIST, --wordlist WORDLIST`
  
path to text file with one or more words on every line to be searched
                        
  `-o OUTPUT, --output OUTPUT`
  
optional output file name, will default to prepending 'marked-' to the original pdf
                        
  `-c COLOR, --color COLOR`
  
optional argument to specify the color of the highlights. If more than one input  word(list) is provided, the colors will be applied in the same order as the input word(lists), defaulting to yellow if the specified colors >2 but <#wordlists. If m ultiple wordlists are provided but only one color, that color will be applied to all. Defaults to yellow. 

Options: red, blue, green, yellow, magenta, cyan; or RGB color value in the form [X.X, X.X, X.X]

# TODO
- Add options for pageranges and options to exclude pages
- Create default wordlists to use when none are specified
- Make code more efficient by calling "Annot.update" fewer times
- Create installable commandline tool, or figure out a way to add "python3 /path/to/pdf-word-highlighter.py" to the PATH 
