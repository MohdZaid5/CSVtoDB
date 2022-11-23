Set WshShell = WScript.CreateObject("WScript.Shell")
cmd = "pip install mysql-connector-python"
WshShell.Run cmd