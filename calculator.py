import tkinter as tk

Cor_Display = "#93C572"
Cor_Label = "black"
Cor_button = "#808080"
Cor_button_op = "#D3D3D3"
Cor_Limpar = "white"
Cor_Limpar_bg = "#5F5C5B"

Font_def = ("Arial", 20, "bold")
Font_sml = ("Arial", 16)
Font_lrg = ("FONTFAMILY_ROMAN", 40, "bold")
Font_Digits = ("Arial", 24, "bold")

class Calculadora:
    def __init__(self):

##Criando a janela usando a toolkit
        self.window = tk.Tk()
##Tam da janela com a calculadora
        self.window.geometry("375x667")
##N permite o user mudar o Tam da calculadora
        self.window.resizable(None, None)
##Nome da janela
        self.window.title("Calculadora")
##Cor Background
        self.window.configure(bg = 'black')

##Criando displays
        self.total_expression = ""
        self.current_expression = ""

##Display calculadora
        self.display_frame = self.create_display_frame()
##Label com a expressão e o valor total
        self.total_label, self.label = self.create_display_labels()

#Posicionamento no grid
        self.digits={
            7: (1,1), 8: (1,2), 9:(1,3),
            4: (2,1), 5: (2,2), 6:(2,3),
            1: (3,1), 2: (3,2), 3:(3,3),
            0: (4,2), ".": (4,1)
        }

##Botão
        self.operations = {"/": "\u00F7", "*": "\u00D7", "-": "-", "+": "+"}
        self.buttons_frame = self.create_buttons_frame()

        self.buttons_frame.rowconfigure(0, weight = 1)
        for x in range(1, 5):
            self.buttons_frame.rowconfigure(x, weight = 1)
            self.buttons_frame.columnconfigure(x, weight=1)
        self.create_digit_buttons()
        self.create_operation_buttons()
        self.create_clear_button()
        self.create_equal_button()
        self.create_square_button()
        self.create_root_button()

#Criando os displays
    def create_display_labels(self):
##Label com o valor Total
        total_label = tk.Label(self.display_frame, text = self.total_expression, anchor = tk.E, bg = Cor_Display,
                               fg = Cor_Label, padx = 24, font = Font_sml)
        total_label.pack(expand = True, fill = "both")

##Label com a expressão
        label = tk.Label(self.display_frame, text=self.current_expression, anchor=tk.E, bg=Cor_Display,
                               fg=Cor_Label, padx=24, font=Font_lrg)
        label.pack(expand=True, fill="both")

        return total_label, label


    def create_display_frame(self):
##Tamanho e BG do display
        frame = tk.Frame(self.window, bg = Cor_Display, height = 221)
        frame.pack(expand = True, fill = "both")
        return frame

#add num ao display
    def add_to_expression(self, value):
        self.current_expression += str(value)
        self.update_label()

#Criando os botões, comando para adicionar o num ao display
    def create_digit_buttons(self):
        for digit, grid_value in self.digits.items():
            button = tk.Button(self.buttons_frame, text = str(digit), bg = Cor_button, fg = Cor_Label,
                               font = Font_Digits, command = lambda x = digit: self.add_to_expression(x))
            button.grid(row = grid_value[0], column = grid_value[1], sticky = tk.NSEW)

    def append_operator(self, operator):
        self.current_expression += operator
        self.total_expression += self.current_expression
#Limpa para o prox num
        self.current_expression = ""
        self.update_total_label()
        self.update_label()

#Sinais
    def create_operation_buttons(self):
        i = 0
        for operator,symbol in self.operations.items():
            button = tk.Button(self.buttons_frame, text = symbol, bg = Cor_button_op, fg = Cor_Label, font = Font_def,
                               command = lambda x = operator: self.append_operator(x))
            button.grid(row = i, column = 4, sticky = tk.NSEW)
            i = i + 1

#Limpar
    def clear(self):
        self.total_expression = ""
        self.current_expression = ""
        self.update_label()
        self.update_total_label()

    def create_clear_button(self):
        for operator,symbol in self.operations.items():
            button = tk.Button(self.buttons_frame, text = "L", bg = Cor_Limpar_bg, fg = Cor_Limpar, font = Font_def,
                               command = self.clear)
            button.grid(row = 0, column = 1, columnspan = 1, sticky = tk.NSEW)

    def root(self):
        self.current_expression = str(eval(f"{self.current_expression}**0.5"))
        self.update_label()
    def create_root_button(self):
        for operator,symbol in self.operations.items():
            button = tk.Button(self.buttons_frame, text = "\u221ax", bg = Cor_Limpar_bg, fg = Cor_Limpar, font = Font_def,
                               command = self.root)
            button.grid(row = 0, column = 3, columnspan = 1, sticky = tk.NSEW)

    def square(self):
        self.current_expression = str(eval(f"{self.current_expression}**2"))
        self.update_label()
    def create_square_button(self):
        for operator,symbol in self.operations.items():
            button = tk.Button(self.buttons_frame, text = "x\u00b2", bg = Cor_Limpar_bg, fg = Cor_Limpar, font = Font_def,
                               command = self.square)
            button.grid(row = 0, column = 2, columnspan = 1, sticky = tk.NSEW)

#Igual
    def evaluate(self):
        self.total_expression += self.current_expression
        self.update_total_label()
##Se erro
        try:

            self.current_expression = str(eval(self.total_expression))

            self.total_expression = ""
        except Exception as e:
            self.current_expression = "Erro"
        finally:
            self.update_label()

    def create_equal_button(self):
        for operator,symbol in self.operations.items():
            button = tk.Button(self.buttons_frame, text = "=", bg = Cor_button_op, fg = Cor_Label, font = Font_def,
                               command = self.evaluate)
            button.grid(row = 4, column = 3, columnspan = 2, sticky = tk.NSEW)

    def create_buttons_frame(self):
        frame = tk.Frame(self.window)
        frame.pack(expand=True, fill="both")
        return frame


    def update_total_label(self):
        expression = self.total_expression
        for operator, symbol in self.operations.items():
            expression = expression.replace(operator, f' {symbol} ')
        self.total_label.config(text = expression)


    def update_label(self):
        self.label.config(text = self.current_expression[:11])

    def run(self):
        self.window.mainloop()

if __name__ == "__main__":
    calcula = Calculadora()
    calcula.run()
