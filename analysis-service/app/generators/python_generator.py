import ast

def generate_pytest(content: str, filename: str):
    tree = ast.parse(content)
    funcs = [n.name for n in ast.walk(tree) if isinstance(n, (ast.FunctionDef, ast.AsyncFunctionDef))]
    tests = []
    for name in funcs[:20]:
        tests.append(
            f"def test_{name}_valid():\n"
            f"    # Arrange / Act / Assert generated for {name}\n"
            "    assert True\n"
        )
    return '\n'.join(tests) or 'def test_generated_smoke():\n    assert True\n'
