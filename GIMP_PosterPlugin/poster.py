#!/usr/bin/env python


from gimpfu import *

#file1, file2, text are arguments
def poster(file1, cubism, file2, file3, flip, file4, file5, text, fontsize, font, colorBack, colorFore):
 
              # Make a new image in A4 format
              imgW, imgH = 2480, 3508
              img = gimp.Image(imgW, imgH, RGB)
              gimp.message("created a new image")


              # make the colors
              pdb.gimp_context_set_background(colorBack)
              pdb.gimp_context_set_foreground(colorFore)
              gimp.message("created colors")


              # make a background layer
              background = gimp.Layer(img, "background", imgW, imgH, RGBA_IMAGE, 100, NORMAL_MODE) 
              background.fill(BACKGROUND_FILL)
              img.add_layer(background, 1)
              gimp.message("created background")


              # make the text layer
              textLayer = pdb.gimp_text_fontname(img, None, imgW/2, imgH/7, text, 10, True, fontsize, PIXELS, font)
              textLayer.translate(-textLayer.width/2, -textLayer.height/3)
              gimp.message("text created")



              #make image layer 1
              image1 = pdb.file_png_load(file1, file1)

              #cubism effect on background image  
              drawable = image1.layers[0]
              if cubism:
                  pdb.plug_in_cubism(image1, drawable, 30, 9, 1)
  
              pdb.gimp_edit_copy(drawable)
              imageLayer1 = gimp.Layer(img, "image 1", imgW, imgH, RGBA_IMAGE, 100, NORMAL_MODE)
              img.add_layer(imageLayer1,1)
              floatingLayer = pdb.gimp_edit_paste(imageLayer1, True)
              pdb.gimp_floating_sel_anchor(floatingLayer)

                    
              
              #make image layer 2
              image2 = pdb.file_png_load(file2, file2)
              pdb.gimp_edit_copy(image2.layers[0])
              imageLayer2 = gimp.Layer(img, "image 2", imgW, imgH, RGBA_IMAGE, 100, NORMAL_MODE)
              img.add_layer(imageLayer2,1)
              floatingLayer = pdb.gimp_edit_paste(imageLayer2, True)
              pdb.gimp_floating_sel_anchor(floatingLayer)
            


              #make image layer 3
              image3 = pdb.file_png_load(file3, file3)
              pdb.gimp_edit_copy(image3.layers[0])
              imageLayer3 = gimp.Layer(img, "image 3", imgW, imgH, RGBA_IMAGE, 100, NORMAL_MODE)
              img.add_layer(imageLayer3,1)
              floatingLayer = pdb.gimp_edit_paste(imageLayer3, True)
              pdb.gimp_floating_sel_anchor(floatingLayer)

              

              #flipping the elephant (imageLayer3)
              if flip:
                  pdb.gimp_item_transform_flip_simple(imageLayer3, 0, True, 0)    
              
                  #add transform for elephant to move it to the left
                  imageLayer3.translate(-imageLayer3.width/2 , 0)    


              #make image layer 4
              image4 = pdb.file_png_load(file4, file4)
              pdb.gimp_edit_copy(image4.layers[0])
              imageLayer4 = gimp.Layer(img, "image 4", imgW, imgH, RGBA_IMAGE, 100, NORMAL_MODE)
              img.add_layer(imageLayer4,1)
              floatingLayer = pdb.gimp_edit_paste(imageLayer4, True)
              pdb.gimp_floating_sel_anchor(floatingLayer)


              #make image layer 5
              image5 = pdb.file_png_load(file5, file5)
              pdb.gimp_edit_copy(image5.layers[0])
              imageLayer5 = gimp.Layer(img, "image 5", imgW, imgH, RGBA_IMAGE, 100, NORMAL_MODE)
              img.add_layer(imageLayer5,1)
              floatingLayer = pdb.gimp_edit_paste(imageLayer5, True)
              pdb.gimp_floating_sel_anchor(floatingLayer)                          

                        

              # Create a new image window and place in display
              gimp.Display(img)
              # Show the new image window
              gimp.displays_flush()


register(
              "python_fu_poster",
              "Poster",
              "Create a poster",
              "EJ",
              "Copyright@EJ",
              "2023",
              "Poster",
              "", 
              [
                  (PF_FILE, "file1", "Choose Image 1", ""),
                  (PF_TOGGLE, "cubism", "Implement cubism:", False),

                  (PF_FILE, "file2", "Choose Image 2", ""), 
                  (PF_FILE, "file3", "Choose Image 3", ""),
                  (PF_TOGGLE, "flip", "Implement flip:", False),

                  (PF_FILE, "file4", "Choose Image 4", ""),
                  (PF_FILE, "file5", "Choose Image 5", ""),                                    
                  (PF_STRING, "text", "Choose Copyright",

"""
  TALKING ABOUT
PUMPKINS DOES NOT
 MAKE THEM GROW
"""),
                  (PF_SPINNER, "fontsize", "Font Size", 170, (10, 200, 5)),
                  (PF_FONT, "font", "Choose Font", "Superclarendon Heavy"),
                  (PF_COLOR, "colorBack", "Background color", (255, 255, 255)),
                  (PF_COLOR, "colorFore", "Foreground color", (0, 0, 0)),


                  



              ],
              [],
              poster, menu="<Image>/File/Create/Assign2"
)

main()
