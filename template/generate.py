import sys
import os

if len(sys.argv) > 1:
    html_name = sys.argv[1]
    os.system('cp .extend_base_html ' + html_name + '.html')
