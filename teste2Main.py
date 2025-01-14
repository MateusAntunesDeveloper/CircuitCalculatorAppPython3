import tkinter as tk
from tkinter import messagebox


class CircuitCalculatorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculadora de Circuitos Elétricos")
        self.root.geometry("720x1000")
        self.root.config(bg="#524848")

        self.option_label = tk.Label(root, text="Selecione o tipo de cálculo no sistema:", font=("Arial", 20), bg="#240101", fg="white")
        self.option_label.grid(row=0, column=0, padx=20,pady=10, sticky="w")

        # Label e Dropdown de Opções

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
        self.option_menu.config(width=40, font=("Consolas", 15),bg="#240202", fg="white", relief="raised")
        self.option_menu.grid(row=1,column=0,padx=20,  pady=5)


        # Botão para Selecionar
        self.select_button = tk.Button(root, text="Selecionar", command=self.show_inputs, font=("Futura", 20), bg="#0f6604", fg="white", relief="raised")
        self.select_button.grid(row=2, column=0, padx=20, pady=10, sticky="w")

        # Frame para Entradas
        self.inputs_frame = tk.Frame(root,bg="#524848")
        self.inputs_frame.grid(row=3, column=0, padx=20, pady=10)

        # Resultado
        self.result_label = tk.Label(root, text="Resultado: ", font=("Arial", 20), bg="#240101", fg="white")
        self.result_label.grid(row=10, column=0, padx=20, pady=20, sticky="w")


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
        tk.Label(self.inputs_frame, text="Resistores (separados por vírgula):",font=("Arial", 22), bg="#080808",fg="white").pack()
        self.resistors_entry = tk.Entry(self.inputs_frame, width=40)
        self.resistors_entry.pack(pady=5)

        tk.Button(
            self.inputs_frame, text="Calcular Série", command=self.calculate_series
        ).pack(pady=5)
        tk.Button(
            self.inputs_frame, text="Calcular Paralelo", command=self.calculate_parallel
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
        tk.Label(self.inputs_frame, text="Tensão de Entrada (V):").pack()
        self.voltage_entry = tk.Entry(self.inputs_frame)
        self.voltage_entry.pack(pady=5)

        tk.Label(self.inputs_frame, text="Resistores R1 e R2 (separados por vírgula):").pack()
        self.resistors_divider_entry = tk.Entry(self.inputs_frame)
        self.resistors_divider_entry.pack(pady=5)

        tk.Button(
            self.inputs_frame, text="Calcular Divisor", command=self.calculate_divider
        ).pack(pady=5)

    def calculate_divider(self):
        try:
            voltage = float(self.voltage_entry.get())
            r1, r2 = map(float, self.resistors_divider_entry.get().split(","))
            v_out = voltage * (r2 / (r1 + r2))
            self.result_label.config(text=f"Saída do Divisor: {v_out:.2f} V")
        except ValueError:
            messagebox.showerror("Erro", "Insira valores válidos.")

    def show_capacitance_inputs(self):
        tk.Label(self.inputs_frame, text="Capacitores (separados por vírgula):").pack()
        self.capacitors_entry = tk.Entry(self.inputs_frame)
        self.capacitors_entry.pack(pady=5)

        tk.Button(
            self.inputs_frame, text="Calcular Série", command=self.calculate_capacitance_series, ).pack(pady=5)
        tk.Button(
            self.inputs_frame, text="Calcular Paralelo", command=self.calculate_capacitance_parallel
        ).pack(pady=5)

    def calculate_capacitance_series(self):
        try:
            capacitors = self._get_values(self.capacitors_entry)
            result = 1 / sum(1 / c for c in capacitors if c > 0)
            self.result_label.config(text=f"Capacitância (Série): {result:.2f} F")
        except ValueError as e:
            messagebox.showerror("Erro", str(e))

    def calculate_capacitance_parallel(self):
        try:
            capacitors = self._get_values(self.capacitors_entry)
            result = sum(capacitors)
            self.result_label.config(text=f"Capacitância (Paralelo): {result:.2f} F")
        except ValueError as e:
            messagebox.showerror("Erro", str(e))

    def show_inductance_inputs(self):
        tk.Label(self.inputs_frame, text="Indutores (separados por vírgula):").pack()
        self.inductors_entry = tk.Entry(self.inputs_frame, width=40)
        self.inductors_entry.pack(pady=5)

        tk.Button(
            self.inputs_frame, text="Calcular Série", command=self.calculate_inductance_series
        ).pack(pady=5)
        tk.Button(
            self.inputs_frame, text="Calcular Paralelo", command=self.calculate_inductance_parallel
        ).pack(pady=5)

    def calculate_inductance_series(self):
        try:
            inductors = self._get_values(self.inductors_entry)
            result = sum(inductors)
            self.result_label.config(text=f"Indutância (Série): {result:.2f} H")
        except ValueError as e:
            messagebox.showerror("Erro", str(e))

    def calculate_inductance_parallel(self):
        try:
            inductors = self._get_values(self.inductors_entry)
            result = 1 / sum(1 / l for l in inductors if l > 0)
            self.result_label.config(text=f"Indutância (Paralelo): {result:.2f} H")
        except ValueError as e:
            messagebox.showerror("Erro", str(e))

    def show_power_inputs(self):
        tk.Label(self.inputs_frame, text="Tensão (V):").pack()
        self.voltage_power_entry = tk.Entry(self.inputs_frame)
        self.voltage_power_entry.pack(pady=5)

        tk.Label(self.inputs_frame, text="Corrente (A):").pack()
        self.current_power_entry = tk.Entry(self.inputs_frame)
        self.current_power_entry.pack(pady=5)

        tk.Button(
            self.inputs_frame, text="Calcular Potência", command=self.calculate_power
        ).pack(pady=5)

    def calculate_power(self):
        try:
            voltage = float(self.voltage_power_entry.get())
            current = float(self.current_power_entry.get())
            power = voltage * current
            self.result_label.config(text=f"Potência: {power:.2f} W")
        except ValueError:
            messagebox.showerror("Erro", "Insira valores válidos.")

    def show_energy_inputs(self):
        tk.Label(self.inputs_frame, text="Capacitância (F):").pack()
        self.capacitance_entry = tk.Entry(self.inputs_frame)
        self.capacitance_entry.pack(pady=5)

        tk.Label(self.inputs_frame, text="Tensão (V):").pack()
        self.voltage_energy_entry = tk.Entry(self.inputs_frame)
        self.voltage_energy_entry.pack(pady=5)

        tk.Button(
            self.inputs_frame, text="Calcular Energia", command=self.calculate_energy
        ).pack(pady=5)

    def calculate_energy(self):
        try:
            capacitance = float(self.capacitance_entry.get())
            voltage = float(self.voltage_energy_entry.get())
            energy = 0.5 * capacitance * (voltage ** 2)
            self.result_label.config(text=f"Energia: {energy:.2f} J")
        except ValueError:
            messagebox.showerror("Erro", "Insira valores válidos.")

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
