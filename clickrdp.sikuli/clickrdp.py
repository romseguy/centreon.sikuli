import sys

# append the custom library directory path to the system path
# so we can import custom modules from this directory such as centreon
centreon_lib_path = sys.argv[1]
if not centreon_lib_path in sys.path: sys.path.append(centreon_lib_path)

import centreon

begin_test = time.time()

try:
	openApp("rdesktop -u 'romain.seguy@uha.fr' -p '$EnsiPro' -g 1024x768 appliweb5")
except:
	centreon.status(2, time.time() - begin_test, "openApp failed")
try:
	wait("start-button.png", 10)
except:
	closeApp("rdesktop")
	centreon.status(2, time.time() - begin_test, "wait failed")

click("start-button.png")
type("notepad" + Key.ENTER)
closeApp("rdesktop")

centreon.status(0, time.time() - begin_test)
