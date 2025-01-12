import streamlit.web.cli as stcli
import sys
from pathlib import Path

if __name__ == "__main__":
    sys.argv = ["streamlit", "run", str(Path("app/main.py").absolute())]
    sys.exit(stcli.main()) 