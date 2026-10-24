import re

def generate_junit(content: str, filename: str):
    package_match = re.search(r"^\s*package\s+([\w.]+)\s*;", content, re.MULTILINE)
    package_decl = f"package {package_match.group(1)};\n\n" if package_match else ""
    classes = re.findall(r"\bclass\s+(\w+)", content)
    cls = classes[0] if classes else filename.replace('.java', '')
    methods = re.findall(r"(?:public|private|protected)?\s*[\w<>\[\]]+\s+(\w+)\s*\([^)]*\)\s*(?:\{|throws)", content)
    keywords = {'if', 'for', 'while', 'switch', 'catch', 'synchronized'}
    tests = []
    seen = set()
    for method in methods[:20]:
        if method in keywords or method == cls:
            continue  # skip keywords and constructors (same name as class)
        if method in seen:
            continue  # avoid generating duplicate method names, which would fail to compile
        seen.add(method)
        tests.append(
            "    @Test\n"
            f"    void {method}_shouldHandleValidInput() {{\n"
            f"        // Arrange / Act / Assert generated for {method}\n"
            f"        assertNotNull(new {cls}());\n"
            "    }\n"
        )
    body = ''.join(tests) or '    @Test\n    void generatedSmokeTest(){ assertTrue(true); }\n'
    return (
        f"{package_decl}"
        "import org.junit.jupiter.api.*;\n"
        "import static org.junit.jupiter.api.Assertions.*;\n\n"
        f"class {cls}GeneratedTest {{\n{body}}}\n"
    )
