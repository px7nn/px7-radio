def parse(inp: str):
    try:
        if inp=="ping":
            return {
                'action': 'ping'
            }
        tokens = inp.split()
        if not tokens:
            return -1
        if tokens[0] == "quit" or tokens[0] == "exit" or tokens[0] == "logout":
            exit()
        
        if tokens[0] == "radio" and len(tokens) < 2:
            print("Unknown command")
            return -1
        
        action = tokens[1]
        flags = {}
        name_parts = []

        for i in tokens[2:]:
            if i.startswith("--"):
                key, val = i.split("=", 1)
                key = key[2:]
                flags[key] = val
            else:
                name_parts.append(i)

        name = " ".join(name_parts) if name_parts else None
        out = {
            'action': action,
            'name': name
        }
        return out | flags
        
    except:
        return -1
    
    
