import Image
import ImageDraw
import ImageOps
import math

def draw_mask(angle,width,height,offset_init,offset_A,offset_focus,offset_B):
	offset = height*offset_init/100
	vectorA = offset+offset_A*height/100
	focus = vectorA+offset_focus*height/100
	vectorB = focus+offset_B*height/100

	mask = Image.new('L', (width,height))
	mask_1px = Image.new('L', (1,height))
	draw_1px = ImageDraw.Draw(mask_1px)
	for y in range (0,offset): # draw white zone
		draw_1px.point((0,y),255)
	for y in range (offset,vectorA): # draw vectorA
		draw_1px.point((0,y),(vectorA-y)*(255/(vectorA-offset)))
	for y in range (vectorA,focus):	# draw white zone
		draw_1px.point((0,y),0)
	for y in range (focus,vectorB):	# draw vectorB
		draw_1px.point((0,y),255-(vectorB-y)*(255/(vectorB-focus)))
	for y in range (vectorB,height): # draw white zone
		draw_1px.point((0,y),255)
	
	m_width,m_height = mask.size
	mask_1px = mask_1px.resize((int(m_width*3),m_height), Image.ANTIALIAS)
	mask_1px = ImageOps.invert(mask_1px)
	mask_top = mask_1px.rotate(angle,Image.NEAREST,1)
	mask_top = ImageOps.invert(mask_top)

	mask.convert("RGBA")
	n_width,n_height = mask_top.size
	mask.paste(mask_top,(-n_width/2,-(n_height/2-height/2)))
	mask.convert("L")
	return mask
