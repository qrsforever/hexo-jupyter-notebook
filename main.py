"""
jupyter convert
"""

from __future__ import print_function
import sys
import re
from nbconvert import HTMLExporter


def main(jupyter_file):
    """
    convert jupyter file to html
    :params jupyter_file: juptyer file path
    """
    html_exporter = HTMLExporter()
    html_exporter.template_file = 'full'
    restr = "%s" % (str(html_exporter.from_filename(jupyter_file)[0]))
    template = """
<iframe id='ipynb'   marginheight="0" frameborder="0" width='924px' srcdoc="%s"  style="scrolling:no;">
</iframe>

<script>

$("#ipynb").load( function() {
console.log($("#ipynb").contents().find("body").find("#notebook"));
document.getElementById('ipynb').height=$("#ipynb").contents().find("#notebook").height()+100;
})
</script> 
    """ % restr.replace("\"", "'")
    # print(sys.version)
    # template = '2341'
    print(re.sub(r'<a.*?\/a>', '', template))

main(sys.argv[1])
