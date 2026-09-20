import os
import subprocess
import sys
import tempfile 

from sqlalchemy.orm import Session

from database import get_db


def test_get_db_yields_a_session_and_closes_it():
    gen = get_db()
    db = next(gen)
    assert isinstance(db, Session)

    try:
        next(gen)
    except StopIteration:
        pass


def test_missing_database_url_raises_on_import():
    env = os.environ.copy()
    
    env.pop("database_url", None)
    env.pop("DATABASE_URL", None)
    
    env["PYTHONPATH"] = os.path.pathsep.join([os.getcwd(), env.get("PYTHONPATH", "")])
    
    with tempfile.TemporaryDirectory() as tmpdir:
        result = subprocess.run(
            [sys.executable, "-c", "import database"],
            cwd=tmpdir,  
            env=env,
            capture_output=True,
            text=True,
        )
        
    assert result.returncode != 0
    assert "CRITICAL CONFIG ERROR: database_url is missing from the env" in result.stderr
