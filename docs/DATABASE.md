# Database model

Core entities: users, projects, project_files, test_suites, test_cases, test_runs, test_results, coverage_reports, api_endpoints, test_configurations, analysis_results, reports, notifications.

Project ownership is represented by `projects.owner_id`. Additional domain entities reference `projects` through JPA relationships.
