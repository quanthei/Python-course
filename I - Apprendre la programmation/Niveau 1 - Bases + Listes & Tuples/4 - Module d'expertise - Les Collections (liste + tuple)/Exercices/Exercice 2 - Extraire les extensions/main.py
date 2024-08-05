# LES COLLECTIONS : LISTES / TUPLES
# Exercice "Extraire les extensions"

#-------------------------FUNCTIONS-------------------------
def get_file_extension(file_name: str) -> str:
    file_extension = file_name.split(".")    
    if len(file_extension) > 1: # fichier avec une extension
        file_extension[-1]
    return None # fichier sans extension
    
def get_file_type_description(file_extension: str, definition_extensions_list) -> str:
    if file_extension is None:
        return "Aucune extension"
    else:
        for file_description in definition_extensions_list:
            if file_extension in file_description:
                file_extension_description = file_description[1]
                return file_extension_description
    return "Extension non connue"
        
fichiers = ("notepad.exe", "mon.fichier.perso.doc", "notes.TXT", "vacances.jpeg", "planning", "data.dat")

definition_extensions = (("doc", "Document Word"),
                        ("exe", "Executable"),
                        ("txt", "Document Texte"),
                        ("jpeg", "Image JPEG"))

#-------------------------MAIN-------------------------
def main():
    for file in fichiers:
        # Get file extension
        file_extension = get_file_extension(file_name=file.lower())
      
        # Fetch file type based on file_extension
        file_type_description = get_file_type_description(file_extension=file_extension, definition_extensions_list=definition_extensions)
       
        # Return result
        print(f"{file} ({file_type_description})")
        
#-------------------------EXE-------------------------
main()