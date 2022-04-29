"""
Summary:
    Highligh code snippets using pygments
"""
from pathlib import Path

from pygments import highlight
from pygments.formatters import HtmlFormatter
from pygments.lexers import guess_lexer


def to_html_file(text: str):
    Path("index.html").write_text(text)


def main():
    code = 'print "Hello World"'
    lexer = guess_lexer(code)  # Lexer == programming language highlighter
    formatter = HtmlFormatter(style="monokai", full=True)  # Formatter == Outfile format

    result = highlight(code, lexer, formatter)
    print("RESULT".center(60, "-"))
    print(result)


if __name__ == "__main__":
    main()
