import matplotlib.pyplot as plt

# Funkcja wyświetlająca okienko z informacjami
def show_info(title, content):
    plt.figure(figsize=(6, 4))
    # Wyświetlenie tekstu (przesunięcie w dół)
    plt.text(0.05, 0.6, content, fontsize=12, wrap=True, va='top')
    plt.axis('off')
    # Tytuł z odpowiednim przesunięciem
    plt.suptitle(title, fontsize=16, y=0.95)
    plt.show()
