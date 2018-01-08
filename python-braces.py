import sys
from tempfile import *

class Braces:
    def __init__(self):
        self._file = sys.argv[1]
        self.parse_file()

    def parse_file(self):
        converted = NamedTemporaryFile(delete=True)
        with open(self._file, "r") as f, open(converted.name, "w") as tmp:
            prespace = ""
            for lie in f:
                cleanLie = lie.lstrip()
                try:
                    openBrace = cleanLie.index("{")
                    tmp.write(prespace + cleanLie[:openBrace] + ":\n")
                    cleanLie = cleanLie[openBrace + 1:]
                    prespace = prespace + "    "
                except ValueError:
                    pass
                try:
                    closeBrace = cleanLie.index("}")
                    if cleanLie[closeBrace + 1] == ";":
                        tmp.write(prespace + cleanLie[:closeBrace] + "\n")
                        prespace = prespace[:-5]
                        cleanLie = cleanLie[closeBrace + 2:]
                    else:
                        tmp.write(prespace + cleanLie[:closeBrace] + "\n")
                        prespace = prespace[:-5]
                        cleanLie = cleanLie[closeBrace + 1:]
                except ValueError:
                    pass
                cleanLie = cleanLie.lstrip()
                tmp.write(prespace + cleanLie + "\n")
        exec(open(converted.name).read())
            
                        
braces = Braces()
