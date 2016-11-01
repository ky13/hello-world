import subprocess
print(subprocess.Popen(["ls", "-l", "/"], stdout=subprocess.PIPE).communicate()[0])
print("Hello, world!")
