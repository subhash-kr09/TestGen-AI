from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from pathlib import Path
import ast, re, json, os
from .analyzers.python_analyzer import analyze_python
from .analyzers.java_analyzer import analyze_java
from .analyzers.javascript_analyzer import analyze_javascript
from .generators.java_generator import generate_junit
from .generators.python_generator import generate_pytest
from .generators.javascript_generator import generate_jest
app=FastAPI(title="TestGen Analysis Service",version="1.0.0")
class ProjectRequest(BaseModel): projectId:int; path:str; language:str
@app.get('/health')
def health(): return {'status':'UP','service':'analysis-service'}
@app.post('/analyze/project')
def analyze(req:ProjectRequest):
    root=Path(req.path)
    if not root.exists(): raise HTTPException(404,'Project workspace not found')
    files=[p for p in root.rglob('*') if p.is_file() and p.suffix in {'.java','.py','.js','.jsx','.ts','.tsx'}]
    results=[]
    for p in files[:300]:
        try:
            text=p.read_text(errors='ignore')
            lang=req.language.lower()
            data=analyze_java(text) if lang=='java' or p.suffix=='.java' else analyze_python(text) if lang=='python' or p.suffix=='.py' else analyze_javascript(text)
            results.append({'file':str(p.relative_to(root)),'language':lang,'analysis':data})
        except Exception as e: results.append({'file':str(p),'error':str(e)})
    return {'projectId':req.projectId,'files':results,'scenarios':['Valid input','Empty input','Invalid input','Null values','Boundary values','Exception handling','Unauthorized request']}
@app.post('/generate/tests')
def generate(req:ProjectRequest):
    root=Path(req.path)
    files=[p for p in root.rglob('*') if p.is_file()]
    generated=[]
    for p in files:
        text=p.read_text(errors='ignore') if p.suffix in {'.java','.py','.js'} else ''
        if not text: continue
        if req.language.lower()=='java' and p.suffix=='.java': code=generate_junit(text,p.name)
        elif req.language.lower()=='python' and p.suffix=='.py': code=generate_pytest(text,p.name)
        elif req.language.lower() in ('javascript','node','nodejs') and p.suffix=='.js': code=generate_jest(text,p.name)
        else: continue
        out=p.parent/(p.stem+'GeneratedTest'+('.java' if req.language.lower()=='java' else '.py' if req.language.lower()=='python' else '.test.js'))
        out.write_text(code); generated.append({'source':str(p.relative_to(root)),'testFile':str(out.relative_to(root)),'code':code})
    return {'projectId':req.projectId,'generated':generated,'count':len(generated)}
