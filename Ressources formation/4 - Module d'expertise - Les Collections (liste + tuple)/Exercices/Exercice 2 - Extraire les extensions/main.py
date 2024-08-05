# LES COLLECTIONS : LISTES / TUPLES
# Exercice "Extraire les extensions"

#-------------------------FUNCTIONS-------------------------
def get_file_extension(file_name: str) -> str:
    file_extension = file_name.split(".")    
    if len(file_extension) == 1: # fichier sans extension
        return None
    return file_extension[-1]
    
def get_file_type(file_extension: str, definition_extensions_list) -> str:
    if file_extension is None:
        return "Aucune extension"
    else:
        for file_description in definition_extensions_list:
            if file_extension in file_description:
                return file_description[1]
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
        file_type = get_file_type(file_extension=file_extension, definition_extensions_list=definition_extensions)
       
        # Return result
        print(f"{file} ({file_type})")
        
#-------------------------EXE-------------------------
main()