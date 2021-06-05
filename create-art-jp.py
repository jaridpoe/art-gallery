import os
pics = os.listdir('assets/art/japan')
for pic in pics:
   name = pic[0:-4]
   strng = f"""---
name: {name}
path: "/assets/art/japan/{pic}"
---
"""
   file_name = 'pages/art/japan/' + name + '.md'
   with open(file_name, 'w') as new_file:
       new_file.write(strng)