import os
import shutil

# Pasta onde o script será executado
folder = "."

# Dicionário de extensões e suas respectivas pastas
file_types = {
    "Imagens": [".jpg", ".jpeg", ".png", ".gif", ".bmp"],
    "Documentos": [".pdf", ".docx", ".doc", ".txt", ".xlsx", ".pptx"],
    "Áudios": [".mp3", ".wav", ".aac"],
    "Vídeos": [".mp4", ".avi", ".mkv"],
    "Compactados": [".zip", ".rar", ".7z"],
    "Scripts": [".py", ".sh", ".js"]
}

def organize_files():
    for filename in os.listdir(folder):
        filepath = os.path.join(folder, filename)

        # Ignorar o próprio script
        if filename == "organizer.py":
            continue

        # Ignorar pastas
        if os.path.isdir(filepath):
            continue

        # Pegar extensão do arquivo
        _, ext = os.path.splitext(filename)

        moved = False

        # Verifica para qual pasta a extensão pertence
        for folder_name, extensions in file_types.items():
            if ext.lower() in extensions:
                target_dir = os.path.join(folder, folder_name)
                os.makedirs(target_dir, exist_ok=True)
                shutil.move(filepath, os.path.join(target_dir, filename))
                print(f"Movido: {filename} → {folder_name}")
                moved = True
                break
        
        # Se a extensão não está mapeada
        if not moved and ext != "":
            other_dir = os.path.join(folder, "Outros")
            os.makedirs(other_dir, exist_ok=True)
            shutil.move(filepath, os.path.join(other_dir, filename))
            print(f"Movido: {filename} → Outros")

if __name__ == "__main__":
    organize_files()
