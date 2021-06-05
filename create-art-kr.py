import os
pics = os.listdir('assets/art/korea')
for pic in pics:
   name = pic[0:-4]
   strng = f"""---
name: {name}
path: "/assets/art/korea/{pic}"
---
"""
   file_name = 'pages/art/korea/' + name + '.md'
   with open(file_name, 'w') as new_file:
       new_file.write(strng)