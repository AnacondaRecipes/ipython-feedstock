import subprocess
import platform
import os
import sys
from pathlib import Path
import IPython
import IPython.conftest
import IPython.core
import IPython.core.magics
import IPython.extensions
import IPython.lib
import IPython.paths
import IPython.terminal.debugger
import IPython.terminal.embed
import IPython.terminal.interactiveshell
import IPython.terminal.magics
import IPython.terminal.prompts
import IPython.terminal.ptutils
import IPython.terminal.shortcuts
import IPython.terminal.shortcuts.auto_match
import IPython.terminal.shortcuts.auto_suggest
import IPython.terminal.shortcuts.filters
import IPython.terminal.tests
import IPython.testing
import IPython.testing.plugin
import IPython.testing.plugin.pytest_ipdoctest
import IPython.testing.tests
import IPython.utils._process_common
import IPython.utils._process_emscripten
import IPython.utils._process_posix
import IPython.utils.capture
import IPython.utils.coloransi
import IPython.utils.contexts
import IPython.utils.data
import IPython.utils.decorators
import IPython.utils.dir2
import IPython.utils.encoding
import IPython.utils.frame
import IPython.utils.generics
import IPython.utils.importstring
import IPython.utils.io
import IPython.utils.ipstruct
import IPython.utils.module_paths
import IPython.utils.openpy
import IPython.utils.process
import IPython.utils.py3compat
import IPython.utils.sentinel
import IPython.utils.shimmodule
import IPython.utils.strdispatch
import IPython.utils.sysinfo
import IPython.utils.syspathcontext
import IPython.utils.tempdir
import IPython.utils.terminal
import IPython.utils.tests
import IPython.utils.timing
import IPython.utils.tokenutil
import IPython.utils.ulinecache
import IPython.utils.wildcard

WIN = platform.system() == "Windows"
LINUX = platform.system() == "Linux"
PYPY = "__pypy__" in sys.builtin_module_names
PPC = "ppc" in platform.machine()

COV_THRESHOLD = os.environ.get("COV_THRESHOLD")

# Environment variable should be set in the meta.yaml
MIGRATING = eval(os.environ.get("MIGRATING", "None"))

PYTEST_SKIPS = ["decorator_skip", "pprint_heap_allocated"]
PYTEST_ARGS = [sys.executable, "-m", "pytest", "-vv"]

IGNORE_GLOBS = [
    "consoleapp.py",
    "external/*.py",
    "sphinxext/*.py",
    "terminal/console*.py",
    "terminal/pt_inputhooks/*.py",
    "utils/*.py",
]

PYTEST_ARGS += sum([[f"--ignore-glob", glob] for glob in IGNORE_GLOBS], [])

if WIN:
    pass
else:
    pass

if LINUX:
    PYTEST_SKIPS += ["system_interrupt"]

if len(PYTEST_SKIPS) == 1:
    PYTEST_ARGS += ["-k", f"not {PYTEST_SKIPS[0]}"]
elif PYTEST_SKIPS:
    PYTEST_ARGS += ["-k", f"""not ({" or ".join(PYTEST_SKIPS) })"""]

if __name__ == "__main__":
    print("Building on Windows?      ", WIN)
    print("Building on Linux?        ", LINUX)
    print("Building for PyPy?        ", PYPY)
    print("Running pytest with args")
    print(PYTEST_ARGS, flush=True)
    sys.exit(subprocess.call(PYTEST_ARGS, cwd=str(Path(IPython.__file__).parent)))