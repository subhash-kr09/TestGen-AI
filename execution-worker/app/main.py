from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from pathlib import Path
import subprocess, time, os
app=FastAPI(title='TestGen Execution Worker',version='1.0.0')
class RunRequest(BaseModel): projectId:int; path:str; language:str; timeoutSeconds:int=120
@app.get('/health')
def health(): return {'status':'UP','service':'execution-worker'}
def run(cmd,cwd,timeout):
 t=time.time()
 try:
  p=subprocess.run(cmd,cwd=cwd,capture_output=True,text=True,timeout=min(timeout,300)); return {'exitCode':p.returncode,'stdout':p.stdout[-12000:],'stderr':p.stderr[-12000:],'durationMs':int((time.time()-t)*1000),'status':'PASSED' if p.returncode==0 else 'FAILED'}
 except subprocess.TimeoutExpired as e: return {'exitCode':-1,'stdout':(e.stdout or '')[-12000:] if isinstance(e.stdout,str) else '','stderr':'Execution timed out','durationMs':int((time.time()-t)*1000),'status':'TIMEOUT'}
@app.post('/run')
def execute(req:RunRequest):
 root=Path(req.path)
 if not root.exists() or not str(root.resolve()).startswith('/workspace'): raise HTTPException(400,'Invalid workspace')
 lang=req.language.lower()
 if lang=='java': result=run(['mvn','-q','test'],root,req.timeoutSeconds)
 elif lang=='python': result=run(['python3','-m','pytest','-q'],root,req.timeoutSeconds)
 elif lang in ('javascript','node','nodejs'): result=run(['npm','test','--','--runInBand'],root,req.timeoutSeconds)
 else: raise HTTPException(400,'Unsupported language')
 return {'projectId':req.projectId,'framework':lang,'result':result}
