import os
import win32com.client

def get_system_components():
    """
    Bilgisayarın donanım bileşenlerini alır (ekran kartı, ses kartı, bluetooth vs.).
    """
    try:
        components = []
        wmi = win32com.client.GetObject("winmgmts:")
        for item in wmi.InstancesOf("Win32_PnPEntity"):
            name = item.Name
            if name:
                components.append(name)
        return components
    except Exception as e:
        print(f"Donanım bileşenleri alınırken bir hata oluştu: {e}")
        return []

def save_components_to_file(file_path):
    """
    Donanım bileşenlerini belirtilen dosya yoluna kaydeder.
    """
    components = get_system_components()

    try:
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write("Bilgisayarda bulunan donanım bileşenleri:\n")
            file.write("\n".join(components))
        print(f"Donanım bileşenleri '{file_path}' dosyasına kaydedildi.")
    except Exception as e:
        print(f"Dosya kaydedilirken bir hata oluştu: {e}")


if __name__ == "__main__":
    # Kullanıcının Masaüstü dizinini al
    desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")
    file_path = os.path.join(desktop_path, "donanim_bilesenleri.txt")  # Masaüstüne kaydet
    save_components_to_file(file_path)
