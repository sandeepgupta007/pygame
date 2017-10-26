import cx_Freeze

executables = [cx_Freeze.Executable("space_impact_game.py")]

cx_Freeze.setup(
    name="Space Impact",
    options={"build_exe": {"packages":["pygame"],
                            "include_files":["space_impact_user.png","CHILLER.TTF","Chillout.ttf","HARNGTON.TTF","ITCBLKAD.TTF"]}},
    
    executables = executables

    )
