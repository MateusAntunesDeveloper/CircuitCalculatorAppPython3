import tkinter as tk
from tkinter import messagebox


class CircuitCalculatorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculadora de Circuitos Elétricos")
        self.root.geometry("800x600")
        
        # Label e Campo de Entrada
        self.label = tk.Label(root, text="Insira os valores dos resistores (separados por vírgula):")
        self.label.pack(pady=10)
        
        self.entry = tk.Entry(root, width=40)
        self.entry.pack(pady=5)
        
        # Botões
        self.series_button = tk.Button(root, text="Calcular Série", command=self.calculate_series)
        self.series_button.pack(pady=5)
        
        self.parallel_button = tk.Button(root, text="Calcular Paralelo", command=self.calculate_parallel)
        self.parallel_button.pack(pady=5)
        
        # Resultado
        self.result_label = tk.Label(root, text="Resultado: ", font=("Arial", 12))
        self.result_label.pack(pady=20)
    
    def calculate_series(self):
        """Calcula a resistência em série."""
        try:
            resistors = self._get_resistors()
            result = sum(resistors)
            self.result_label.config(text=f"Resultado (Série): {result:.2f} Ω")
        except ValueError as e:
            messagebox.showerror("Erro", str(e))
    
    def calculate_parallel(self):
        """Calcula a resistência em paralelo."""
        try:
            resistors = self._get_resistors()
            result = 1 / sum(1 / r for r in resistors if r > 0)
            self.result_label.config(text=f"Resultado (Paralelo): {result:.2f} Ω")
        except ValueError as e:
            messagebox.showerror("Erro", str(e))
    
    def _get_resistors(self):
        """Lê e valida os valores dos resistores inseridos."""
        try:
            values = self.entry.get().split(",")
            resistors = [float(value.strip()) for value in values]
            if not resistors:
                raise ValueError("Por favor, insira ao menos um valor.")
            return resistors
        except Exception:
            raise ValueError("Insira valores válidos separados por vírgula (ex: 10, 20, 30).")


if __name__ == "__main__":
    root = tk.Tk()
    app = CircuitCalculatorApp(root)
    root.mainloop()
