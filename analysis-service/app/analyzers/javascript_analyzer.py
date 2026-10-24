import re

def analyze_javascript(content: str):
    classes = re.findall(r"\bclass\s+(\w+)", content)
    funcs = re.findall(r"(?:function\s+|(?:const|let|var)\s+)(\w+)\s*=\s*\([^)]*\)\s*=>|function\s+(\w+)\s*\(", content)
    names = [a or b for a, b in funcs]
    endpoint_pattern = r"\.(get|post|put|delete)\s*\(\s*['\"]([^'\"]+)"
    endpoints = [{"method": m.upper(), "path": p} for m, p in re.findall(endpoint_pattern, content)]
    return {"classes": classes, "functions": names, "apiEndpoints": endpoints,
            "branches": len(re.findall(r"\b(if|for|while|switch)\b", content)),
            "exceptions": len(re.findall(r"\bthrow\b", content))}
