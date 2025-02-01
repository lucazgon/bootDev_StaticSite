# bootDev_StaticSite
static site generator course via boot.dev

# architecture
- static
    - contains assets, images, data
- src/
    - static site generator (SSG) python code that generates public data
        - delete all content in /public
        - copy static assets to /public
        - convert each block into a tree of HTML Node objects
        - join all HTML nodes under a parent HTML node for the page
        - use a recursive method to convert HTML nodes into a massive HTML string and inject it into HTML template
        - write the HTML string to a file in the /public directory
    - content/
        - .md files
    - template.html
- public/ 
    - output directory w/ final HTML and CSS
    - main.py
- file server
    - serves public files to browser
- browser
    - renders HTML and CSS as a webpage

# notes
- leaving off on TextNode to HTMLNode