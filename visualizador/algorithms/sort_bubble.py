# Contrato: init(vals), step() -> {"a": int, "b": int, "swap": bool, "done": bool}

items = []
n = 0
i = 0
j = 0

def init(vals):
    global items, n, i, j
    items = list(vals)
    n = len(items)
    i = 0
    j = 0

def step():
    # TODO:
    b=j
    a=j+1
    swap=False
    if a < n - i:
        if items[a]>items[b]:
            items[a],items[b]=items[b], items[a]
            swap=True
            j=j+1
            return {"a": a, "b": b, "swap": swap, "done": False}
        else:
            j=0
            i+=1
            return step()

    
    if i>=n-1:
        return {"done": True}