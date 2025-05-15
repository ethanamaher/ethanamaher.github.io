import argparse
import os
import codecs
from datetime import date

TARGET_WIDTH = 80

def main():
    parser = argparse.ArgumentParser(description="Convert markdown to html and plaintext files for blogpost")
    parser.add_argument("inputfile", help="path to input markdown file")
    parser.add_argument("outputfile", help="path to output markdown and txt file")

    args = parser.parse_args()

    if not os.path.exists(args.inputfile):
        print(f"Error: Input file '{args.inputfile}' not found.")
        return

    try:
        with codecs.open(args.inputfile, mode="r", encoding="utf-8") as f:
            lines = f.readlines()
        blog_title = lines[0]
        pre_content = "".join(lines[3:-1])
        pre_content = pre_content.rstrip("\n")
    except Exception as e:
        print(f"Error reading input file: {e}")
        return

    date_today = date.today().strftime("%Y-%m-%d")
    header_spaces = TARGET_WIDTH - len(date_today)

    date_today = date_today.rstrip('\n')
    post_header = f"""{' '*header_spaces}{date_today}"""

    TITLE_LEN = len(blog_title)

    title_spaces = int((TARGET_WIDTH/2) - (TITLE_LEN/2))
    blog_title = blog_title.rstrip('\n')
    title_fmt = f"""<strong>{' '*title_spaces}{blog_title}</strong>"""

    html_output = f"""
<!DOCTYPE html>
    <head>
        <meta http-equiv="Content-Type" content="text/html; charset=windows-1252">
        <title>
            ethan maher | {blog_title}
        </title>
        <link rel="stylesheet" type="text/css" href="../styles.css">
    </head>
    <body>
        <nav>
            <ul>
                <li><strong>ethanamaher</strong></li>
                <li><a href="/index.html">home</a></li>
                <li><a href="/projects.html">projects</a></li>
                <li><a href="/blog.html">blog</a></li>
            </ul>
        </nav>
<pre>

{post_header}

{title_fmt}

{pre_content}
</pre>
        <hr>
        <div class="footer">
            <a href="/links.html">links</a> |
            <a href="Maher_Ethan_Resume.pdf">resume</a>
        </div>
    </body>
</html>
"""

    try:
        with codecs.open(args.outputfile, "w", encoding="utf-8") as f:
            f.write(html_output)
        print("Wrote html file")
    except Exception as e:
        print(f"Error writing html file: {e}")

if __name__ == "__main__":
    main()
