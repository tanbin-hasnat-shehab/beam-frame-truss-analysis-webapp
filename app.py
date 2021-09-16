import streamlit as st
import extra_streamlit_components as stx
import codecs
import streamlit.components.v1 as stc
from anastruct import SystemElements
import math
import matplotlib.pyplot as plt
from PIL import Image
st.set_page_config(layout="wide")
def my_html(html_file,width=1000,height=1000):
	html_file=codecs.open(html_file,'r')
	page=html_file.read()
	stc.html(page,width=width,height=height,scrolling=False)


my_html('a.html')





cookie_manager = stx.CookieManager()
cookies = cookie_manager.get_all()

cookie = st.text_input("Cookie", key="0")
clicked = st.button("Get")
value = cookie_manager.get(cookie)



ss = SystemElements(EA=5000)

new_data=[]
for i in range(len(value)):
	if value[i] not  in new_data:
		new_data.append(value[i])
print('\n\n\n')
print(new_data)
no_of_member=0
members=[]
no_of_load=0
loads=[]
no_of_fixed=0
fixed=[]
no_of_hinged=0
hinged=[]

for i in range(len(new_data)):
	if new_data[i]['type']=='line':
		no_of_member+=1
		members.append(new_data[i])
	if new_data[i]['type']=='point_load':
		no_of_load+=1
		loads.append(new_data[i])
	if new_data[i]['type']=='fixed_support':
		no_of_fixed+=1
		fixed.append(new_data[i])
	if new_data[i]['type']=='hinged_support':
		no_of_hinged+=1
		hinged.append(new_data[i])

for i in range(no_of_member):
	ss.add_truss_element(location=[[members[i]['x1'], members[i]['y1']]   , [members[i]['x2'], members[i]['y2']] ])    



for i in range(no_of_load):
	
	ss.point_load(Fx=loads[i]['load'],rotation=loads[i]['rotation'], node_id=ss.find_node_id([loads[i]['pos_x'],loads[i]['pos_y']]))
	




for i in range(no_of_fixed):
	ss.add_support_fixed(node_id=ss.find_node_id([fixed[i]['x'],fixed[i]['y']]))






for i in range(no_of_hinged):
	
	ss.add_support_hinged(node_id=ss.find_node_id([hinged[i]['x'],hinged[i]['y']]))
ss.solve()
ss.show_structure()
plt.title('A sine wave')
plt.savefig('my-figure1.png')
image1 = Image.open('my-figure1.png')
st.image(image1)

ss.show_reaction_force()
plt.title('A sine wave')
plt.savefig('my-figure2.png')
image2 = Image.open('my-figure2.png')
st.image(image2)


ss.show_axial_force()
plt.title('A sine wave')
plt.savefig('my-figure3.png')
image3 = Image.open('my-figure3.png')
st.image(image3)







