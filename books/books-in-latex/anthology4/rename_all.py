import os
import shutil

old_dir = "original_text"

for fn in os.listdir(old_dir):
    old_path = os.path.join( old_dir, fn )
    
    if not os.path.isdir(  old_path ):
    
        base_name, ext = fn.split(".")
        
        stripped_of_spaces = base_name.replace(" ", "_")
        
        new_name = ".".join([ stripped_of_spaces.lower() , "tex" ])
        
        new_path = os.path.join( "sections", new_name )
        
        if not os.path.exists( new_path ):
            
            shutil.copy( old_path,  new_path )