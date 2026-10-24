# Automated Software Test Generator — Complete Modular Starter

This repository implements the requested multi-page platform architecture: React frontend, Spring Boot REST API, MySQL persistence, FastAPI analysis/generation service, and a separate execution-worker container. It is designed around the supplied specification.

## Current working capabilities
- JWT authentication with BCrypt password hashing
- Project CRUD and ownership checks
- ZIP upload with basic validation
- Java/Python/JavaScript source analysis endpoints
- Java JUnit 5 test generation
- Python PyTest test generation scaffold
- JavaScript Jest test generation scaffold
- Separate execution worker API
- Test cases, suites, runs, results, coverage/report/history data model
- React Router pages for all requested major screens
- Dashboard charts and API-backed project/test data
- Docker Compose for MySQL, frontend, backend, analysis service and execution worker
- Sample Java project for testing

## Important security note
The execution worker is a separate container and should be treated as an untrusted-code runner. For production, add rootless containers, seccomp/AppArmor, read-only filesystems, network isolation, CPU/memory/PID limits and a dedicated job queue. The development worker already enforces a timeout and workspace boundary.

## Run
```powershell
docker compose -f infra/docker-compose.yml up --build
```
Open http://localhost:5173

Default development database: testgen / testgen / testgen.

## Local services
- Frontend: http://localhost:5173
- Spring Boot API: http://localhost:8080
- FastAPI docs: http://localhost:8000/docs
- Execution worker: http://localhost:8001/docs
- MySQL: localhost:3306

## First flow
1. Register an account.
2. Create a Java project.
3. Upload the sample project ZIP from `samples/java-sample/`.
4. Analyze the project.
5. Generate tests.
6. Run tests.
7. Review results and coverage.

The code is deliberately modular so additional testing engines can be added without rewriting the UI or project APIs.
