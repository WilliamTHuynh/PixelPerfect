import cx_Freeze

executables = [cx_Freeze.Executable("main.py")]

cx_Freeze.setup(
    name = "F * * *",
    options = {"build_exe": {"packages": ["pygame"]}, "included_files" :[""]},

    executables = executables
)