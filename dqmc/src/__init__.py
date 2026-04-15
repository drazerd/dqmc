import os

# Windows DLL path (safe optional)
if os.name == "nt":
    try:
        os.add_dll_directory(r"C:\msys64\ucrt64\bin")
    except Exception:
        pass

# Pure Python backend only
# Fortran backend removed
