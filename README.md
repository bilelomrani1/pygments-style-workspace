# workspace style for Pygments

Style theme for Pygments used in the workspace template.

## Install

    git clone https://github.com/bilelomrani1/pygments-style-workspace
    cd pygments-style-workspace
    (sudo) python setup.py install

## Export the style as CSS

    pygmentize -S workspace -f html > workspace.css

## Extra information

### `pygments` supported languages


`pygments` at the moment supports over 150 different programming languages,
template languages and other markup languages. To see an exhaustive list of the
currently supported languages, use the command::

    pygmentize -L lexers

### `pygments` styles avaible

To get a list of all available stylesheets, execute the following command on the
command line::

    pygmentize -L styles

Please read the [official documentation](http://pygments.org/docs/) for further information on the usage
of `pygments` styles.
