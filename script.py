import os
import json

s = [
    {'Part 1' : 
     {
         'Section 1' : ['subsection 1', 'subsection 2']
     }
    },
    {'Part 2' : 
     {
         'Section 1' : ['subsection 1', 'subsection 2']
     },
    },
    {'Part 3' : 
     {
         'Section 1' : ['subsection 1', 'subsection 2']
     }
    },
]

d = {
    'title' : "The title of the document",
    'author' : "me",
    'bib' : True,
    'indexes' : ["main", "notations"],
    'abstract' : True,
    'languages' : ['en', 'fr'],
    'structure' : s
}

def subsection(s):
    return "\\subsection{" + s +"}\n"
def section(s):
    return "\\section{" + s +"}\n"
def part(s):
    return "\\chapter{" + s +"}\n"

def section_to_tex(name, dt):
    return section(name) + ''.join([subsection(x) for x in dt])

def part_to_tex(p):
    name = p.keys()[0]
    dt = p[name]
    return (part(name) + ''.join([section_to_tex(k, dt[k]) for k in dt.keys()]))

def structure_to_tex(s):
    return (''.join([part_to_tex(k) for k in s]))

def title(s):
    return "\title{}".format("{"+ s +"}")

def author(s):
    return "\author{}".format("{"+ s +"}")

if __name__ == "__main__":
    print structure_to_tex(s)

