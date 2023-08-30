#!/usr/bin/env python
from djcompiler import DjangoCompiler


if __name__ == "__main__":
    compiler: DjangoCompiler = DjangoCompiler(
        project_name="Signum Explorer",
        project_author="signum-network",
        project_version="1.0.0",
        build_directory="build",
        other_files_needed=["manage.py", ".env", "__init__.py", "supervisord.conf"],
        other_dirs_needed=["static"],
        ignored_files=["manage.py", "compiler.py", "gunicorn.conf.py"]
    )
    ignored = compiler.initial_ignored_dirs + ["django_compiler/"]
    compiler.set_ignored(ignored)
    compiler.compile_project()
    