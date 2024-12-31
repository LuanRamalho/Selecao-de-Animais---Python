import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import requests
from io import BytesIO

# Links das imagens de cada animal
animal_images = {
    "Cachorro": "https://i.pinimg.com/736x/7e/a8/86/7ea886cd9d9de708574f857dcb998804.jpg",
    "Gato": "https://i.pinimg.com/736x/b4/de/5d/b4de5dd3dfcd4607cf2a15932def92a9.jpg",
    "Coelho": "https://i.pinimg.com/736x/f8/6c/3d/f86c3d4669d4100db869607e222e1a35.jpg",
    "Tartaruga": "https://i.pinimg.com/736x/5b/78/19/5b78199ae2819d892297e9212eff3764.jpg",
    "Elefante": "https://i.pinimg.com/736x/53/b0/a8/53b0a891a9e1110b637b8033d4d44d50.jpg",
    "Girafa": "https://i.pinimg.com/736x/6b/d9/79/6bd9799f0f0e8a8e1b91fe835d60f90d.jpg",
    "Boi": "https://i.pinimg.com/736x/5b/ae/de/5baede60ebc379dd042ebb54369426fb.jpg",
    "Vaca": "https://i.pinimg.com/736x/70/fe/9c/70fe9ce8f486b91c36457f204e0f3f75.jpg",
    "Porco": "https://i.pinimg.com/736x/b9/ce/71/b9ce715817fdcdd072ed150755ed5035.jpg",
    "Javali": "https://i.pinimg.com/736x/ac/8c/7a/ac8c7ad7f2e4719c99b5a6ecff4e59ef.jpg",
    "Cavalo": "https://i.pinimg.com/736x/c9/27/0e/c9270e46e5ac9141fb088927af545092.jpg",
    "Camelo": "https://i.pinimg.com/736x/72/50/4c/72504c6ac684dda2a02da7d5705bbd11.jpg",
    "Galo": "https://i.pinimg.com/736x/6b/e6/37/6be6375f4ae70f7c15665040717c6d17.jpg",
    "Galinha": "https://i.pinimg.com/736x/5f/c4/18/5fc41851895ffb436e8f2b142898d1da.jpg",
    "Touro": "https://i.pinimg.com/736x/71/cb/f3/71cbf3326623fcaf0a852ffb819383ac.jpg",
    "Zebra": "https://i.pinimg.com/736x/16/4b/6c/164b6cea01dd893aacc783dd0bbaafb6.jpg",
    "Gavião": "https://i.pinimg.com/736x/6d/d7/fa/6dd7fabdbbf1f7757def0cbc896cbbc4.jpg",
    "Falcão": "https://i.pinimg.com/736x/91/0b/f3/910bf38c8bbfb4bafc485a36b4a961a5.jpg",
    "Rinoceronte": "https://i.pinimg.com/736x/9e/02/8e/9e028e2ead360959263a1f840ab664dc.jpg",
    "Hipopótamo": "https://i.pinimg.com/736x/de/5b/00/de5b005c24cb55e89dabe8d1e430f4d7.jpg",
    "Macaco": "https://i.pinimg.com/736x/4f/a3/45/4fa3457be1cd631eb6b4698947d4b555.jpg",
    "Leão": "https://i.pinimg.com/736x/38/04/bd/3804bdc52bb42b36214b07830a216023.jpg",
    "Tigre": "https://i.pinimg.com/736x/fa/47/a9/fa47a9288f7fc77438b56c241f4416ea.jpg",
    "Onça": "https://i.pinimg.com/736x/7a/6a/ed/7a6aedb7d3e5581f766f5003eda3746c.jpg",
    "Jacaré": "https://i.pinimg.com/736x/a1/76/e1/a176e1653eaf8d7e990fc8021244f0b4.jpg",
    "Cobra": "https://i.pinimg.com/736x/24/f6/be/24f6bed5a421281df44d092d5c0ae315.jpg",
    "Peixe": "https://i.pinimg.com/736x/f4/a7/46/f4a74608b643e670777ae93d0e27d92b.jpg",
    "Tubarão": "https://i.pinimg.com/736x/4c/bf/d6/4cbfd686ae0572882bd9db7a16eab85d.jpg",
    "Baleia": "https://i.pinimg.com/736x/9b/cb/13/9bcb134247a24abec3d9f24e1901ed85.jpg",
    "Estrela do Mar": "https://i.pinimg.com/736x/84/a4/59/84a459b36b69c870ebccc13419bc7422.jpg",
    "Golfinho": "https://i.pinimg.com/736x/c2/0f/28/c20f289452c77dfeac800993f8013abc.jpg"
}

def load_image(animal):
    # Limpa a imagem atual
    for widget in image_frame.winfo_children():
        widget.destroy()
    
    # Verifica se o animal foi selecionado
    if animal in animal_images:
        image_url = animal_images[animal]
        try:
            # Faz o download da imagem
            response = requests.get(image_url)
            response.raise_for_status()
            img_data = BytesIO(response.content)
            img = Image.open(img_data)
            img = img.resize((300, 300), Image.LANCZOS)
            tk_image = ImageTk.PhotoImage(img)
            
            # Exibe a imagem
            label = tk.Label(image_frame, image=tk_image)
            label.image = tk_image
            label.pack()
        except Exception as e:
            error_label = tk.Label(image_frame, text="Erro ao carregar imagem", fg="red")
            error_label.pack()

# Cria a janela principal
root = tk.Tk()
root.title("Seleção de Animais")
root.geometry("450x500")
root.configure(bg="lightblue")

# Frame para o título
title_frame = tk.Frame(root, bg="lightblue")
title_frame.pack(pady=10)

title_label = tk.Label(title_frame, text="Selecione um Animal", font=("Arial", 18, "bold"), bg="lightblue", fg="darkblue")
title_label.pack()

# Frame para a seleção de animais
selection_frame = tk.Frame(root, bg="lightblue")
selection_frame.pack(pady=10)

animal_label = tk.Label(selection_frame, text="Animal:", font=("Arial", 14), bg="lightblue")
animal_label.pack(side=tk.LEFT, padx=5)

animal_combobox = ttk.Combobox(selection_frame, values=list(animal_images.keys()), font=("Arial", 12))
animal_combobox.pack(side=tk.LEFT, padx=5)

select_button = tk.Button(selection_frame, text="Mostrar Imagem", font=("Arial", 12, "bold"), bg="darkblue", fg="white",
                          command=lambda: load_image(animal_combobox.get()))
select_button.pack(side=tk.LEFT, padx=5)

# Frame para exibir a imagem
image_frame = tk.Frame(root, bg="lightblue")
image_frame.pack(pady=20)

# Inicia o loop principal
root.mainloop()
