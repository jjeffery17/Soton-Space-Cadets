import requests as req

id = input("Enter email ID: ")
if "@" in id:
    id = id.split("@")[0]  # format input

try:
    res = req.get("https://www.ecs.soton.ac.uk/people/"+id)  # get short redirect address
    address = res.history[0].headers["location"]
    res = req.get(address)  # get full redirect address
    print(res.url.split("/")[-1].replace("-", " ").title())  # format and output name
except Exception as e:
    print("Error, could not get name.")
    print("Error Info:", e)
