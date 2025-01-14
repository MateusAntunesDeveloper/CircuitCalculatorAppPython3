import tkinter as tk
from tkinter import messagebox


class CircuitCalculatorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculadora de Circuitos Elétricos")
        self.root.geometry("600x600")
        self.root.config(bg="#f4f4f9")

        # Label e Dropdown de Opções
        self.option_label = tk.Label(root, text="Selecione o tipo de cálculo:", font=("Arial", 14), bg="#f4f4f9")
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
        self.option_menu = tk.OptionMenu(root, self.selected_option, *self.options)
        self.option_menu.config(width=40, font=("Arial", 12))
        self.option_menu.grid(row=1, column=0, padx=20, pady=5)

        # Botão para Selecionar
        self.select_button = tk.Button(root, text="Selecionar", command=self.show_inputs, font=("Arial", 12), bg="#4CAF50", fg="white", relief="raised")
        self.select_button.grid(row=2, column=0, padx=20, pady=15, sticky="w")

        # Frame para Entradas
        self.inputs_frame = tk.Frame(root, bg="#f4f4f9")
        self.inputs_frame.grid(row=3, column=0, padx=20, pady=10)

        # Resultado
        self.result_label = tk.Label(root, text="Resultado: ", font=("Arial", 14), bg="#f4f4f9")
        self.result_label.grid(row=4, column=0, padx=20, pady=20, sticky="w")

    def show_inputs(self):
        """Exibe os campos de entrada para o cálculo selecionado."""
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

    # Funções para Entradas e Cálculos

    def show_resistors_inputs(self):
        tk.Label(self.inputs_frame, text="Resistores (separados por vírgula):", font=("Arial", 12), bg="#f4f4f9").pack()
        self.resistors_entry = tk.Entry(self.inputs_frame, width=40, font=("Arial", 12))
        self.resistors_entry.pack(pady=5)

        tk.Button(
            self.inputs_frame, text="Calcular Série", command=self.calculate_series, font=("Arial", 12), bg="#2196F3", fg="black", relief="raised"
        ).pack(pady=5)
        tk.Button(
            self.inputs_frame, text="Calcular Paralelo", command=self.calculate_parallel, font=("Arial", 12), bg="#2196F3", fg="white", relief="raised"
        ).pack(pady=5)

    def calculate_series(self):
        try:
            resistors = self._get_values(self.resistors_entry)
            result = sum(resistors)
            self.result_label.config(text=f"Resultado (Série): {result:.2f} Ω")
        except ValueError as e:
            messagebox.showerror("Erro", str(e))

    def calculate_parallel(self):
        try:
            resistors = self._get_values(self.resistors_entry)
            result = 1 / sum(1 / r for r in resistors if r > 0)
            self.result_label.config(text=f"Resultado (Paralelo): {result:.2f} Ω")
        except ValueError as e:
            messagebox.showerror("Erro", str(e))

    def show_divider_inputs(self):
        tk.Label(self.inputs_frame, text="Tensão de Entrada (V):", font=("Arial", 12), bg="#f4f4f9").pack()
        self.voltage_entry = tk.Entry(self.inputs_frame, font=("Arial", 12))
        self.voltage_entry.pack(pady=5)

        tk.Label(self.inputs_frame, text="Resistores R1 e R2 (separados por vírgula):", font=("Arial", 12), bg="#f4f4f9").pack()
        self.resistors_divider_entry = tk.Entry(self.inputs_frame, font=("Arial", 12))
        self.resistors_divider_entry.pack(pady=5)

        tk.Button(
            self.inputs_frame, text="Calcular Divisor", command=self.calculate_divider, font=("Arial", 12), bg="#2196F3", fg="white", relief="raised"
        ).pack(pady=5)

    def calculate_divider(self):
        try:
            voltage = float(self.voltage_entry.get())
            r1, r2 = map(float, self.resistors_divider_entry.get().split(","))
            v_out = voltage * (r2 / (r1 + r2))
            self.result_label.config(text=f"Saída do Divisor: {v_out:.2f} V")
        except ValueError:
            messagebox.showerror("Erro", "Insira valores válidos.")

    # As outras funções de cálculo permanecem as mesmas...

    def _get_values(self, entry):
        """Converte os valores de entrada separados por vírgula em uma lista de floats."""
        try:
            values = entry.get().split(",")
            return [float(value.strip()) for value in values]
        except ValueError:
            raise ValueError("Insira valores válidos separados por vírgula.")


if __name__ == "__main__":
    root = tk.Tk()
    app = CircuitCalculatorApp(root)
    root.mainloop()
