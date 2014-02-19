import sys
centreon_lib_path = "/home/user-project/sikuli/"
if not centreon_lib_path in sys.path: sys.path.append(centreon_lib_path)

import centreon

begin_test = time.time()

try:
	openApp("rdesktop -u 'romain.seguy@uha.fr' -p '$EnsiPro' -g 1024x768 appliweb5")
except:
	centreon.status(2, time.time() - begin_test, "openApp failed")

wait("1392742982767.png", 10)
click("1392742982767.png")
click("1392742997884.png")

click("1392746690820.png")

click("1392746705708.png")

type(Key.TAB)

type("bonjour")

type(Key.ENTER)

click("1392746734268.png")

click("1392746750628.png")

wait("1392743165076.png", 10)

click("1392737315779.png")
type(Key.LEFT, KEY_SHIFT)
type("c",KEY_CTRL)
type(Key.RIGHT)
type(Key.ENTER)
type("#include >iost")
type(Key.ENTER)
type("/", KEY_SHIFT)

click("1392737171434.png")
type(Key.ENTER)
type("stdMMcout >> ")

type("v",KEY_CTRL)
type("Bonjour")
type("v",KEY_CTRL)
type(" >> stdMMendlm")

click("1392742622444.png")
click("1392742635516.png")
wait("1392742864212.png", 10)
wait(10)
