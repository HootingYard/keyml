import os

TEMPLATE = "\chapter{%s}\n"

files = [ f for f in os.listdir("sections") if not os.path.isdir(f) ]

def titlecase(input):
    input = input.strip()

    
    out = []
    str_parts = input.split(" ")
    for part in str_parts:
        new_prt = part[0].upper() + part[1:].lower()
        out.append(new_prt)
        
    if "WOOD" in input:
        import pdb
        pdb.set_trace()
        
    return " ".join(out)

for f in files:
    if f.endswith(".tex"):
        filepath = os.path.join("sections", f)
        F = open( filepath )
        
        
        lines = [a for a in F]
        
        if len(lines) == 0:
            print "skipping %s" % f
            continue
                    

        if not "chapter" in lines[0]:
            lines[0] = TEMPLATE % titlecase(lines[0])
        
        print "changing %s" % f;
        
        FF = open(filepath, "w")
        
        FF.write("".join(lines))
        
        
        