# Security

The backend uses BCrypt for passwords and signed JWTs for API authentication. Uploaded files are stored under `/workspace/project-{id}` with filename path normalization. Test execution is delegated to a separate worker container.

For production execution of untrusted source, enforce rootless execution, seccomp/AppArmor, network disabled by default, read-only root filesystem, CPU/memory/PID limits, non-root users and a queue-based worker pool.
