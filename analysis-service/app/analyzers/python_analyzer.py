import ast
def analyze_python(content:str):
 t=ast.parse(content); out={'classes':[],'functions':[],'imports':[],'branches':0,'exceptions':0}
 for n in ast.walk(t):
  if isinstance(n,ast.ClassDef): out['classes'].append(n.name)
  elif isinstance(n,(ast.FunctionDef,ast.AsyncFunctionDef)): out['functions'].append({'name':n.name,'parameters':[a.arg for a in n.args.args]})
  elif isinstance(n,(ast.Import,ast.ImportFrom)): out['imports'].append(getattr(n,'module',None) or ','.join(a.name for a in n.names))
  elif isinstance(n,(ast.If,ast.Match,ast.IfExp)): out['branches']+=1
  elif isinstance(n,ast.Raise): out['exceptions']+=1
 return out
