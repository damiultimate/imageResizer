#!C:\Users\User\AppData\Local\Programs\Python\Python38-32\python.exe
import os, cgi, cgitb,sys; 
from PIL import Image
import resizeimage

cgitb.enable()
print ('Content-type:text/html')
print()
form=cgi.FieldStorage()
try:
	form_file=form['image']
	new_file1=open(form_file.filename,"wb+")
	new_file1.write(form_file.file.read())

	image=Image.open(form_file.filename+"")
	width, height=image.size
except:
	print("<h1>Error Unknown: No file is selected</h1>")
	sys.exit()


print("<p>Initial width is <span id='initialwidth'>")
print(width)
print("</span>while height is <span id='initialheight'>")
print(height)
print("</span></p>")
# alert(document.getElementById("range").value);
print("Please select the new size from the range below <br><br>")
print("<input oninput='changeWidth()' type='range' id='range' min='0' max='100' style='width:50%;'/><br><br>")
print("New width is <span id='width'>0</span> while new height is <span id='height'>0</span>. Note that new size is <span id='perc'>0</span>% of the original size.<br><br>")
print("<button onclick='move()'>Save</button><br><br>")

print("<img src='"+form_file.filename+"' style='height:90%;'/><br><p>Image preview</p>")

print("""
<script>
changeWidth();
function changeWidth(){
	var width=document.getElementById('initialwidth').innerHTML;
	width=parseInt(width);
	var height=document.getElementById('initialheight').innerHTML;
	height=parseInt(height);
 
 var rangesize=parseInt(document.getElementById('range').value);

width=((rangesize/100)*width);
height=((rangesize/100)*height);

document.getElementById('width').innerHTML=parseInt(width);
document.getElementById('height').innerHTML=parseInt(height);
document.getElementById('perc').innerHTML=parseInt(rangesize);


}
function move(){
 var rangesize = document.getElementById('width').innerHTML;

	window.location.href='makenew.py?width='+rangesize+'&name="""+form_file.filename+"""';
}
</script>
	""")
new_file1.close()
