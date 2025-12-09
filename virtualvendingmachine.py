# Virtual Vending Machine 
import tkinter as tk
import customtkinter as ctk
from vendingmachineproducts import vending_machine_products

class master_frame(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)


class vending_display(ctk.CTkFrame):
    def __init__(self, master_frame, **kwargs):
        super().__init__(master_frame, **kwargs)


class vending_selector(ctk.CTkFrame):
    def __init__(self, master_frame, **kwargs):
        super().__init__(master_frame, **kwargs)
        
        def find_product_id(product_id):
            for product in vending_machine_products:
                if product["id"] == product_id:
                    return product["name"], product["price"]
                return ["Product Not Found"]

        def update_entry(value):
            


        self.entry = ctk.CTkEntry(self, textvariable = entry, placeholder_text = "Enter product id...", state = "disabled")

        self.button1 = ctk.CTkButton(self, text = "1", command = lambda:update_entry(1))
        self.button2 = ctk.CTkButton(self, text = "2", command = lambda:update_entry(2))
        self.button3 = ctk.CTkButton(self, text = "3", command = lambda:update_entry(3))
    
        self.button4 = ctk.CTkButton(self, text = "4", command = lambda:update_entry(4))
        self.button5 = ctk.CTkButton(self, text = "5", command = lambda:update_entry(5))
        self.button6 = ctk.CTkButton(self, text = "6", command = lambda:update_entry(6))

        self.button7 = ctk.CTkButton(self, text = "7", command = lambda:update_entry(7))
        self.button8 = ctk.CTkButton(self, text = "8", command = lambda:update_entry(8))
        self.button9 = ctk.CTkButton(self, text = "9", command = lambda:update_entry(9))

        self.button0 = ctk.CTkButton(self, text = "0", command = lambda:update_entry(0))
        self.button_ok = ctk.CTkButton(self, text = "Ok", command = lambda:find_product_id)
        self.button_cancel = ctk.CTkButton(self, text = "X",)

        self.button1.configure(height = 25, width = 140)
        self.button2.configure(height = 25, width = 140)
        self.button3.configure(height = 25, width = 140)

        self.button4.configure(height = 25, width = 140)
        self.button5.configure(height = 25, width = 140)
        self.button6.configure(height = 25, width = 140)

        self.button7.configure(height = 25, width = 140)
        self.button8.configure(height = 25, width = 140)
        self.button9.configure(height = 25, width = 140)

        self.button0.configure(height = 25, width = 140)
        self.button_ok.configure(height = 25, width = 140)
        self.button_cancel.configure(height = 25, width = 140) 

        self.entry.grid(row = 4, column = 1, padx = 2, pady = 2)

        self.button1.grid(row = 0, column = 0, padx = 2, pady = 2)
        self.button2.grid(row = 0, column = 1, padx = 2, pady = 2)
        self.button3.grid(row = 0, column = 2, padx = 2, pady = 2)

        self.button4.grid(row = 1, column = 0, padx = 2, pady = 2)
        self.button5.grid(row = 1, column = 1, padx = 2, pady = 2)
        self.button6.grid(row = 1, column = 2, padx = 2, pady = 2)

        self.button7.grid(row = 2, column = 0, padx = 2, pady = 2)
        self.button8.grid(row = 2, column = 1, padx = 2, pady = 2)
        self.button9.grid(row = 2, column = 2, padx = 2, pady = 2)

        self.button0.grid(row = 3, column = 1, padx = 2, pady = 2)
        self.button_ok.grid(row = 3, column = 0, padx = 2, pady = 2)
        self.button_cancel.grid(row = 3, column = 2, padx = 2, pady = 2) 


class vending_dispenser(ctk.CTkFrame):
    def __init__(self, master_frame, **kwargs):
        super().__init__(master_frame, **kwargs)
    

class App(ctk.CTk):
    def __init__(self):    
        super().__init__()
    
        self.title("Vending Machine Simulator")

        self.Master_Frame = master_frame(master = self, height = 1200, width = 1200, corner_radius = 0, fg_color = "transparent")
        self.Master_Frame.grid(row = 0, column = 0, sticky = "nsew")

        self.display = vending_display(self.Master_Frame)
        self.display.grid(row = 0, column = 0)

        self.selector = vending_selector(self.Master_Frame)
        self.selector.grid(row = 0, column = 1)

        self.dispenser = vending_dispenser(self.Master_Frame)
        self.dispenser.grid(row = 3, column = 0)

app = App()
app.mainloop()