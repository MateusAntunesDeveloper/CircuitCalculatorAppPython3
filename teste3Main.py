import tkinter as tk
from tkinter import messagebox


class CircuitCalculatorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculadora de Circuitos Elétricos")
      
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()

        # Define o tamanho da tela no PC
        width = int(screen_width * 0.9)
        height = int(screen_height * 0.9)

        WID = (screen_width - width) // 2
        LIT = (screen_height - height) // 2

        self.root.geometry(f"{width}x{height}+{WID}+{LIT}")
        self.root.config(bg="#1e1e2e")

        self.calculation_history = []

        # Título
        self.header_frame = tk.Frame(self.root, bg="#1e1e2e")
        self.header_frame.pack(fill="x", pady=20)
        self.title_label = tk.Label(
            self.header_frame,
            text="Calculadora de Circuitos Elétricos",
            font=("Arial", 28, "bold"),
            bg="#1e1e2e",
            fg="#ffffff"
        )
        self.title_label.pack()

        # Seletor de opções
        self.option_frame = tk.Frame(self.root, bg="#1e1e2e")
        self.option_frame.pack(fill="x", pady=10)
        self.option_label = tk.Label(
            self.option_frame,
            text="Selecione o tipo de cálculo:",
            font=("Arial", 18),
            bg="#1e1e2e",
            fg="#ffffff"
        )
        self.option_label.grid(row=0, column=0, padx=20, pady=10, sticky="w")

        self.options = [
            "Resistores (Série e Paralelo)",
            "Divisores de Tensão",
            "Capacitância Equivalente",
            "Indutância Equivalente",
            "Potência",
            "Energia Armazenada (Capacitor/Indutor)",
        ]
        self.selected_option = tk.StringVar(value=self.options[0])
        self.option_menu = tk.OptionMenu(
            self.option_frame, self.selected_option, *self.options
        )
        self.option_menu.config(
            width=30,
            font=("Arial", 14),
            bg="#44475a",
            fg="#ffffff",
            relief="groove"
        )
        self.option_menu.grid(row=0, column=1, padx=25, pady=10, sticky="w")

        self.select_button = tk.Button(
            self.option_frame,
            text="Selecionar",
            command=self.show_inputs,
            font=("Arial", 16),
            bg="#50fa7b",
            fg="#000000",
            relief="groove",
            padx=15
        )
        self.select_button.grid(row=1, column=0, padx=30, pady=10, sticky="w")
        
        # Entradas e resultado
        self.inputs_frame = tk.Frame(self.root, bg="#1e1e2e")
        self.inputs_frame.pack(fill="x", pady=20)
        self.result_frame = tk.Frame(self.root, bg="#1e1e2e")
        self.result_frame.pack(fill="x", pady=10)
        self.result_label = tk.Label(
            self.result_frame,
            text="Resultado:",
            font=("Arial", 20, "bold"),
            bg="#1e1e2e",
            fg="#8be9fd"
        )
        self.result_label.pack()

        # Aba de Histórico
        self.history_button_frame = tk.Frame(self.root, bg="#1e1e2e")
        self.history_button_frame.pack(fill="x", pady=10)
        self.history_button = tk.Button(
            self.history_button_frame,
            text="Visualizar Histórico de Cálculos",
            command=self.toggle_history,
            font=("Arial", 16),
            bg="#ff79c6",
            fg="#000000",
            relief="groove",
            padx=10
        )
        self.history_button.pack()

        self.history_frame = tk.Frame(self.root, bg="#1e1e2e")
        self.history_label = tk.Label(
            self.history_frame,
            text="Histórico de Cálculos",
            font=("Arial", 20, "bold"),
            bg="#1e1e2e",
            fg="#ffb86c"
        )
        self.history_label.pack(pady=10)

        self.history_listbox = tk.Listbox(self.history_frame, font=("Arial", 14), width=50, height=10)
        self.history_listbox.pack(pady=10)
        self.history_frame.pack_forget()  # Inicialmente oculto

    # Restante do código...

if __name__ == "__main__":
    root = tk.Tk()
    app = CircuitCalculatorApp(root)
    root.mainloop()
