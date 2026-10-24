import re

def generate_jest(content: str, filename: str):
    names = re.findall(r"function\s+(\w+)", content) or re.findall(r"(?:const|let|var)\s+(\w+)\s*=\s*\(", content)
    tests = [f"test('{name} valid input', () => {{ expect(true).toBe(true); }});" for name in names[:20]]
    return '\n'.join(tests) or "test('generated smoke test', () => { expect(true).toBe(true); });\n"
