#!C:\Users\ORE\AppData\Local\Programs\Python\Python38-32\python.exe
import os, cgi, cgitb
cgitb.enable()

print ('Content-type:text/html')
print()
print("<title>Image resizer</title>")
form=cgi.FieldStorage()
if(form.getvalue('download')):
	print("""

	<a href='"""+form.getvalue('download')+"""'><h3>Download the resized image here</h3></a>

		""")


print("""
<br>
<form enctype='multipart/form-data' action='save.py' method='post'>
<br>

Upload new file:  <input type='file' accept='jpg,jpeg,png,gif' name='image'/>
<input type='submit' name='submit'/>
</form>


	""")