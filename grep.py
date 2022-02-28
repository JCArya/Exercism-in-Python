
import re
def grep(pattern, flags, files):
    result = []
    if flags:
        flags = flags.split()
        flags = [flag.replace("-", "") for flag in flags]
    pattern = re.compile(pattern, re.IGNORECASE if "i" in flags else 0)
    for file in files:
        if len(files) > 1:
            file_name = "{}:".format(file)
        else:
            file_name = ""
        with open(file) as f:
            for idx, line in enumerate(f):
                if "n" in flags:
                    line_num = "{}:".format(idx + 1)
                else:
                    line_num = ""
                if "x" in flags:
                    match = pattern.match(line)
                else:
                    match = pattern.search(line)
                if "l" in flags:
                    if("v" in flags and not match) or (
                            "v" not in flags and match):
                        result.append(file + "\n")
                        break
                else:
                    if ("v" in flags and not match) or ("v" not in flags and match):
                        result.append("{file_name}{line_num}{line}".format(
                            file_name=file_name, line_num=line_num, line=line))
    return ''.join(result)
