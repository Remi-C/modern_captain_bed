# -*- coding: utf-8 -*-
"""
Created on Sat Apr 01 18:19:53 2017

@author: Remi
"""
# this script generate an html gallery filee containing thumbnail for 
# each image in the repository
# for each image file in the folder

# read all images from a folder, excluding files finishing with thumbnail

# create first part of html
# loop on all images, generate html
# create last part of html

def find_all_images_in_folder(path_to_folder):
    """ find all image file not ending with "thumbnail"
        @returns array of image file name    
    """
    import os, os.path
    
    imgs = [] 
    valid_images = [".jpg",".gif",".png",".jpeg"]
    for f in os.listdir(path_to_folder):
        pre,ext = os.path.splitext(f) 
        if(ext.lower() in valid_images) and not (pre.endswith("thumbnail")):
            #imgs.append( [os.path.join(path_to_folder,pre),ext] )
            imgs.append(  [pre ,ext] )
    return imgs
    
def generate_html_before_after():
    pre = """
    <!DOCTYPE html>
    <html>
    <head>
    	<meta charset=utf-8 />
    	<meta name="description" content="Gallery of photos for modern cpatain bed project">
    	<title>A simple gallery for modern captain bed project</title>
        <link type="text/css" rel="stylesheet" href="../../js/lightGallery/dist/css/lightgallery.min.css" /> 
    	<link rel="stylesheet" media="screen" href="../../gallery.css" />
    	<link href='http://fonts.googleapis.com/css?family=Yanone+Kaffeesatz' rel='stylesheet' type='text/css'>
     
    </head>
    <body>
        <script
    			  src="https://code.jquery.com/jquery-3.2.1.min.js"
    			  integrity="sha256-hwg4gsxgFZhOsEEamdOYGBf13FyQuiTwlAQgxVSNgt4="
    			  crossorigin="anonymous"></script>
     
        <script src="../../js/lightGallery/dist/js/lightgallery.min.js"></script>
    	<script type="text/javascript">
        $(document).ready(function() {
            $("#lightgallery").lightGallery({
    			selector: '.galleryItem'
    		});		
        });
    
    	</script>
    	   
        <div class="header">
        	<h1>Gallery</h1>
        	Click on picture to enlarge.</p>
        </div>
    	
    	<div class="container" id="lightgallery"> 
    """
    post = """
    </div>
    	
    </body>
    </html>
    """
    return pre, post

def generate_one_image_html(image_path, image_ext):
    q = """<div class="galleryItem" data-src="""\
        + '"' \
        +image_path\
        +image_ext\
        +'"><img src="'\
        +image_path\
        +'_thumbnail.jpeg"'\
        +'/></div>'
        #+image_ext+'" /></div>'
        
    return q


def generate_full_html(path_to_folder, ):
    pre, post =  generate_html_before_after()
    full_html = pre 
    all_images = find_all_images_in_folder(path_to_folder)
    for i in all_images:
        #print('i '+ i[0] +' || ' +i[1] )
        q = generate_one_image_html(i[0], i[1]) 
        full_html += q
    full_html += post 
    return full_html
def generate_write_gallery_file( path_to_folder, output_file_name):
    """ simple test functon
    """ 
    #images_paths = find_all_images_in_folder(path_to_folder)
    full_html = generate_full_html(path_to_folder)
    
    file = open(output_file_name,"w") 
 
    file.write(full_html)   
    file.close() 

    return full_html 

def generate_all_galery_files(base_image_folder_path):
    import os
    subfolders =  os.walk('.').next()[1]
    
    for subfolder in subfolders:
        subfolder_path = os.path.join(base_image_folder_path,subfolder)
        gal_file_name = subfolder_path+'/Gallery.html'
        print("generating gallery file for ", subfolder_path, "file name ", gal_file_name)        
        generate_write_gallery_file( subfolder_path, gal_file_name)
 
    
print(generate_all_galery_files('./'))