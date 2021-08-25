from pathlib import Path
""" to run this code if the name of the file is content_manager.py
(/usr/bin/python3) manage.py shell -c 'import script.roule'
la point est differente elle est importante
"""

print("enter {}".format(Path(__file__)))

import script.about
import script.work_manager
import script.news_manager
import script.visit
import script.deb

exit("exit {}".format(Path(__file__)))

