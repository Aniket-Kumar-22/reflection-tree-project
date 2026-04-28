import json

print("DAILY REFLECTION TOOL")
print("----------------------")

with open("tree/reflection_tree.json") as f:
    tree = json.load(f)


# Store signals (axis scores)
state = {
    "axis1": {"internal": 0, "external": 0},
    "axis2": {"contribution": 0, "entitlement": 0},
    "axis3": {"self": 0, "others": 0}
}

# Start node
current = "START"

while True:
    node = tree[current]

    # print node text
    if "text" in node:
        print("\n" + node["text"])

    # If END node → stop program
    if node["type"] == "end":
        break

    # Question Node
    if node["type"] == "question":

        #show options
        for key, option in node["options"].items():
            print(f"{key}.{option['text']}")

        # Take input
        choice = input("choose option: ")

        # Validate input
        while choice not in node["options"]:
            choice  = input("Invalid choice. Choose again: ")

        selected = node["options"][choice]

        # Check if option has signal
        if "signal" in selected:
            axis, value = selected["signal"].split(":")
            state[axis][value] += 1

        # Move to next node
        current = selected["next"]

    # DECISION NODE
    elif node["type"] == "decision":

        axis = node["condition"]

        # Determine dominant side
        scores = state[axis]
        dominant = max(scores, key=scores.get)

        current = node[dominant]

    # REFLECTION / BRIDGE / SUMMARY
    else:
        input("\nPress Enter to continue...")
        current = node["next"]