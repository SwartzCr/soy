import sys
import site
sys.path.insert(0, '/var/www/test_proj')
site.addsitedir('/var/www/test_proj/lib/python2.7/site-packages')
from app import app as application
