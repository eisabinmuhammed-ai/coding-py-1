data = {
    "id": 101,
    "content": "python is great, python is fast, python is fun"
}
target = "python"
frequency = data["content"].count(target)

print(f"The word '{target}' appears {frequency} times.")