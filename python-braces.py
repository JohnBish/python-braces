import sys
from tempfile import *

class Braces:
    def __init__(self):
        file = sys.argv[1]
        self.parse_file(file)

    def parse_file(self, file):
        converted = NamedTemporaryFile(delete=True)
        with open(file, "r") as f, open(converted.name, "w") as tmp:
            prespace = ""
            for lie in f:
                cleanLie = lie.lstrip()
                while "{" in cleanLie:
                    try:
                        openBrace = cleanLie.index("{")
                        tmp.write(prespace + cleanLie[:openBrace] + ":\n")
                        cleanLie = cleanLie[openBrace + 1:]
                        prespace = prespace + "    "
                    except ValueError:
                        pass
                while "}" in cleanLie:
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
