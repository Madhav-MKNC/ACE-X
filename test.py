a = ["agent/ace",
"agent/config",
"agent/core", 
"agent/data", 
"agent/emotion", 
"agent/infra", 
"agent/interaction", 
"agent/interfaces", 
"agent/memory", 
"agent/meta", 
"agent/reasoning", 
"agent/scheduler", 
"agent/tests", 
"agent/tools"]


from os import system as run 

def commit(add, message):
    run(f"git add {add}")
    run(f"git commit -m {message}")

def push():
    run("git push origin main")

for i in a:
    commit(i, f"Update {i}/")

push()

