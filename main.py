"""
jupyter convert
"""

from __future__ import print_function
import sys
import re
from nbconvert import HTMLExporter


def main(asset_dir, jupyter_file, inc_height):
    """
    convert jupyter file to html
    :params jupyter_file: juptyer file path
    """
    html_exporter = HTMLExporter()
    html_exporter.template_file = 'full'

    # lidong: nbconvert/templates/html/full.tpl
    # iframe js
    # <script src="https://cdnjs.cloudflare.com/ajax/libs/require.js/2.1.10/require.min.js"></script>
    # <script src="https://cdnjs.cloudflare.com/ajax/libs/jquery/2.0.3/jquery.min.js"></script>

    # lidong add
    import random
    import os
    if inc_height == "undefined":
        inc_height = "60"
    num = random.randint(1111, 9999)
    dn = os.path.dirname(asset_dir)
    if os.path.exists(dn + ".md"):
        dn = os.path.dirname(dn)
        jupyter_file = os.path.join(dn, jupyter_file)
    else:
        print("not found: " + os.path.join(asset_dir, jupyter_file))
        return

    # lidong mod, jquery only use 2.0.0, other have some problems (TODO, 忘了啥问题,先去掉)
    # <script src="//code.jquery.com/jquery-2.0.0.js"></script>
    # 换成iframe js 的试试
    # <script src="https://cdnjs.cloudflare.com/ajax/libs/jquery/2.0.3/jquery.min.js"></script>

    # config_dir can set css for notebook generated by nbconvert
    reses = {'config_dir': '%s' % os.path.dirname(__file__)}
    restr = "%s" % (str(html_exporter.from_filename(jupyter_file, resources=reses)[0]))
    template = """
<script src="https://cdnjs.cloudflare.com/ajax/libs/jquery/2.0.3/jquery.min.js"></script>
<iframe id="ipynb-%d" marginheight="0" marginwidth="0" frameborder="0" height="100%%" width="100%%" srcdoc="%s" scrolling="auto">
</iframe>
<script>
$("#ipynb-%d").load( function() {
var h = $("#ipynb-%d").contents().find("#notebook").height();
document.getElementById('ipynb-%d').height= h + %s;
})
</script> 
    """ % (num, restr.replace("\"", "'"), num, num, num, inc_height)
    # print(sys.version)
    # template = '2341'
    print(re.sub(r'<a.*?\/a>', '', template))


main(sys.argv[1], sys.argv[2], sys.argv[3])

#  document.getElementById('ipynb-%d').height=$("#ipynb-%d").contents().find("#notebook").height()+100;
