import json


class JSONSaver:
    def save(self, data):
        with open("output.json", "w") as file:
            json.dump(data, file, indent=4)


class TextSaver:
    def save(self, data):
        with open("output.txt", "w") as file:
            for key, value in data.items():
                file.write(f"{key}: {value}\n")


event = {"type": "Error", "message": "server crashed"}

for saver in [JSONSaver(), TextSaver()]:
    saver.save(event)
