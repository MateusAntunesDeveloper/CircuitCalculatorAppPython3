import tkinter as tk
from tkinter import messagebox


class CircuitCalculatorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculadora de Circuitos Elétricos")
        self.root.geometry("1624x920")
        self.root.config(bg="#1e1e2e")
        
        # Histórico de cálculos
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
        self.option_menu.grid(row=0, column=1, padx=20, pady=10, sticky="w")

        self.select_button = tk.Button(
            self.option_frame,
            text="Selecionar",
            command=self.show_inputs,
            font=("Arial", 16),
            bg="#50fa7b",
            fg="#000000",
            relief="groove",
            padx=10
        )
        self.select_button.grid(row=0, column=2, padx=20, pady=10, sticky="w")

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

    def toggle_history(self):
        """Alterna a visibilidade da aba de histórico."""
        if self.history_frame.winfo_ismapped():
            self.history_frame.pack_forget()
        else:
            self.history_frame.pack(fill="x", pady=20)

    def show_inputs(self):
        """Mostra os campos de entrada correspondentes ao tipo de cálculo selecionado."""
        for widget in self.inputs_frame.winfo_children():
            widget.destroy()

        option = self.selected_option.get()

        if option == "Resistores (Série e Paralelo)":
            self.show_resistors_inputs()
        elif option == "Divisores de Tensão":
            self.show_divider_inputs()
        elif option == "Capacitância Equivalente":
            self.show_capacitance_inputs()
        elif option == "Indutância Equivalente":
            self.show_inductance_inputs()
        elif option == "Potência":
            self.show_power_inputs()
        elif option == "Energia Armazenada (Capacitor/Indutor)":
            self.show_energy_inputs()

    def show_resistors_inputs(self):
        tk.Label(
            self.inputs_frame,
            text="Resistores (separados por vírgula):",
            font=("Arial", 18),
            bg="#1e1e2e",
            fg="#ffffff"
        ).pack()
        self.resistors_entry = tk.Entry(self.inputs_frame, font=("Arial", 14), width=30)
        self.resistors_entry.pack(pady=10)

        tk.Button(
            self.inputs_frame,
            text="Calcular Série",
            command=self.calculate_series,
            bg="#ff79c6",
            fg="#1a1919",
            font=("Arial", 14),
            relief="groove",
            padx=10
        ).pack(pady=5)
        tk.Button(
            self.inputs_frame,
            text="Calcular Paralelo",
            command=self.calculate_parallel,
            bg="#ff79c6",
            fg="#1a1919",
            font=("Arial", 14),
            relief="groove",
            padx=10
        ).pack(pady=5)

    def calculate_series(self):
        try:
            resistors = self._get_values(self.resistors_entry)
            result = sum(resistors)
            self.result_label.config(text=f"Resultado (Série): {result:.2f} Ω")
            self.ask_to_save("Resistores Série", f"Resultado: {result:.2f} Ω")
        except ValueError as e:
            messagebox.showerror("Erro", str(e))

    def calculate_parallel(self):
        try:
            resistors = self._get_values(self.resistors_entry)
            result = 1 / sum(1 / r for r in resistors if r > 0)
            self.result_label.config(text=f"Resultado (Paralelo): {result:.2f} Ω")
            self.ask_to_save("Resistores Paralelo", f"Resultado: {result:.2f} Ω")
        except ValueError as e:
            messagebox.showerror("Erro", str(e))

    def ask_to_save(self, operation, result):
        """Pergunta ao usuário se deseja salvar o cálculo."""
        save = messagebox.askyesno("Salvar Cálculo", f"Você deseja salvar o cálculo: {operation}?\n{result}")
        if save:
            self.save_calculation(f"{operation} - {result}")

    def save_calculation(self, calc_result):
        """Salva o cálculo no histórico."""
        self.calculation_history.append(calc_result)
        self.history_listbox.insert(tk.END, calc_result)

    def _get_values(self, entry):
        """Converte a entrada de texto para uma lista de floats."""
        try:
            values = entry.get().split(",")
            return [float(value.strip()) for value in values]
        except ValueError:
            raise ValueError("Insira valores válidos separados por vírgula.")

if __name__ == "__main__":
    root = tk.Tk()
    app = CircuitCalculatorApp(root)
    root.mainloop()
