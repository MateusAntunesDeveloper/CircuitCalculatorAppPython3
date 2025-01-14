import os
import tkinter as tk
from tkinter import messagebox


class CircuitCalculatorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculadora de Circuitos Elétricos")
        self.root.geometry("1624x920")
        self.root.config(bg="#1e1e2e")

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

        # Histórico de cálculos
        self.history = []

        # Botão para salvar cálculo
        self.save_button = tk.Button(
            self.root,
            text="Salvar Cálculo",
            command=self.save_result,
            font=("Arial", 16),
            bg="#ffb86c",
            fg="#000000",
            relief="groove",
            padx=10
        )
        self.save_button.pack(pady=20)

        # Botão para visualizar cálculos salvos
        self.view_button = tk.Button(
            self.root,
            text="Visualizar Cálculos Salvos",
            command=self.view_history,
            font=("Arial", 16),
            bg="#ffb86c",
            fg="#000000",
            relief="groove",
            padx=10
        )
        self.view_button.pack(pady=10)

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

    # (Adicione o código das funções de cálculo aqui...)

    def save_result(self):
        """Exibe a opção de salvar o cálculo realizado."""
        result = self.result_label.cget("text")
        if result != "Resultado:":
            response = messagebox.askyesno(
                "Salvar Cálculo", "Você deseja salvar este cálculo?"
            )
            if response:
                self.history.append(result)
                messagebox.showinfo("Salvo", "Cálculo salvo com sucesso!")
        else:
            messagebox.showwarning("Erro", "Nenhum cálculo realizado.")

    def view_history(self):
        """Exibe os cálculos salvos em uma nova janela."""
        if not self.history:
            messagebox.showinfo("Histórico", "Nenhum cálculo salvo.")
        else:
            history_window = tk.Toplevel(self.root)
            history_window.title("Histórico de Cálculos")
            history_window.geometry("400x300")
            history_window.config(bg="#1e1e2e")

            history_listbox = tk.Listbox(
                history_window,
                font=("Arial", 14),
                bg="#44475a",
                fg="#ffffff",
                width=50,
                height=15
            )
            history_listbox.pack(pady=10)

            for item in self.history:
                history_listbox.insert(tk.END, item)

    # (Continue com as funções de cálculo conforme o código original...)

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
