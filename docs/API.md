# API overview

Auth: POST `/api/auth/register`, POST `/api/auth/login`, POST `/api/auth/forgot-password`
Projects: GET/POST `/api/projects`, GET/DELETE `/api/projects/{id}`
Project actions: POST `/api/projects/{id}/upload`, `/analyze`, `/generate-tests`, `/run-tests`
Project data: GET `/api/projects/{id}/test-cases`, `/analysis`
Health: GET `/api/health`

All project endpoints require `Authorization: Bearer <JWT>`.
