#!C:\Users\ORE\AppData\Local\Programs\Python\Python38-32\python.exe
import os, cgi, cgitb; 
from PIL import Image
from resizeimage import resizeimage

cgitb.enable()


print ('Content-type:text/html')
print()
form=cgi.FieldStorage()
path=str(form.getvalue('name'))
imag=open(path,'rb+')
img=Image.open(imag)
img=resizeimage.resize_width(img,int(form.getvalue('width')))
new_link="new_"+form.getvalue('name')
img.save(new_link,img.format)
imag.close()
print("""
<script>
window.location.href='index.py?download="""+new_link+"""';

</script>
	""")

