import re

def analyze_java(content: str):
    classes = re.findall(r"\bclass\s+(\w+)", content)
    methods = []
    pattern = r"(?:public|private|protected)?\s*(?:static\s+)?([\w<>\[\], ?]+)\s+(\w+)\s*\(([^)]*)\)"
    for ret, name, args in re.findall(pattern, content):
        methods.append({"name": name, "returnType": ret.strip(), "parameters": [x.strip() for x in args.split(',') if x.strip()]})
    endpoint_pattern = r"@(GetMapping|PostMapping|PutMapping|DeleteMapping)\s*\(\s*['\"]([^'\"]+)"
    endpoints = [{"method": m.upper(), "path": p} for m, p in re.findall(endpoint_pattern, content)]
    return {
        "classes": classes,
        "methods": methods,
        "apiEndpoints": endpoints,
        "dependencies": re.findall(r"import\s+([\w.]+);", content),
        "branches": len(re.findall(r"\b(if|for|while|switch|catch)\b", content)),
        "exceptions": len(re.findall(r"\bthrow\s+new\b", content)),
    }
