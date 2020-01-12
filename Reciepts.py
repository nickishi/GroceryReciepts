'''
Created on Nov 6, 2019

@author: Nick
'''

import csv
import tkinter 
import tkinter.messagebox

    
    

def Close_Button():
    global root      #Function used for exit button, destroys window when executed
    root.destroy()

def Checkout_Button():     #Function used to check for negatives, strings, and proper formatting.
    global root            # If everything is correct, calculations run and export to a receipt.csv
    TotalMoney = float(0)
    
    Milk = Milk_Entry.get()
        
    Eggs = Eggs_Entry.get()
        
    OrangeJuice = OrangeJuice_Entry.get()
    
    CornFlakes = CornFlakes_Entry.get()

    try:
        
        if "-" in Milk or "-" in Eggs or "-" in OrangeJuice or "-" in CornFlakes:   #Checks for negatives while variables are still strings
            tkinter.messagebox.showerror("Error", "Sorry, you can only buy positive amounts of items.")
        else:
           
            if Milk == '':      #Checks to see if no value was entered. If no value is entered, variable is converted from '' string to int(0)
                Milk = int(0) 
            
            else:
                Milk = int(Milk)
                
            if Eggs == '':
                Eggs = int(0)
            
            else:
                Eggs = int(Eggs)
                
            if OrangeJuice == '':
                OrangeJuice = int(0)
            
            else:
                OrangeJuice = int(OrangeJuice)
                
            if CornFlakes == '':
                CornFlakes = int(0)
            
            else:
                CornFlakes = int(CornFlakes)
            
            with open("reciept.csv", "w") as file:
                writer = csv.writer(file, lineterminator = "\n")   #Creates 'reciept.csv' file with the proper formatting required for homework
                if Milk != 0:
                    
                    row1 = ["Milk", Milk, Milk * PriceOfItem[0]]
                    
                    TotalMoney = TotalMoney + (Milk * PriceOfItem[0])
                    
                    writer.writerow(row1)
                    
                if OrangeJuice != 0:
                    row2 = ["Orange Juice", OrangeJuice, OrangeJuice * PriceOfItem[1]]
                    TotalMoney = TotalMoney + (OrangeJuice * PriceOfItem[1])
                    writer.writerow(row2)
                if Eggs != 0:
                    row3 = ["Eggs", Eggs, Eggs * PriceOfItem[2]]
                    TotalMoney = TotalMoney + (Eggs * PriceOfItem[2])
                    writer.writerow(row3)
                if CornFlakes != 0:
                    row4 = ["Corn Flakes", CornFlakes, CornFlakes * PriceOfItem[3]]
                    TotalMoney = TotalMoney + (CornFlakes * PriceOfItem[3])
                    writer.writerow(row4)
                row5 = ["--","--","--"]
                writer.writerow(row5)
                row6 = ["Total", "",TotalMoney]
                writer.writerow(row6)
            tkinter.messagebox.showinfo("Success!", "A receipt has been created as receipt.csv.")
            Milk_Entry.delete(first = 0, last = 100)
            Eggs_Entry.delete(first = 0, last = 100)        #Resets entry boxes for next entry
            OrangeJuice_Entry.delete(first = 0, last = 100)
            CornFlakes_Entry.delete(first = 0, last = 100)
        
    except:
        tkinter.messagebox.showerror("Error", "Sorry, the receipt cannot be created. Please enter only integer values.")
        Milk_Entry.delete(first = 0, last = 100)
        Eggs_Entry.delete(first = 0, last = 100)        #Prints error and resets each entry box
        OrangeJuice_Entry.delete(first = 0, last = 100)
        CornFlakes_Entry.delete(first = 0, last = 100)

def main_box():
    global root
    global Milk_Entry
    global Eggs_Entry
    global OrangeJuice_Entry  #Global variables used in other function calculations
    global CornFlakes_Entry
    global gate2
    root = tkinter.Tk() #Generates root as the main window
    root.title("Gerry's Groceries Checkout")
    
    
    root.geometry("325x60") #Sets the window size
    
    
    Milk_Label = tkinter.Label(root,text = "Milk ($2.99):")  #Displays the labels for each grocery item
    Eggs_Label = tkinter.Label(root, text = "Eggs($2.49):")
    OrangeJuice_Label = tkinter.Label(root, text = "Orange Juice($3.25):")
    CornFlakes_Label = tkinter.Label(root, text = "Corn Flakes($4.25):")
    
    Checkout = tkinter.Button(root, text = "Checkout", command = Checkout_Button) #Button functions to checkout and exit program
    Close = tkinter.Button(root, text = "Exit", command = Close_Button)
    
    root.configure(bg = "khaki1")
    Milk_Label.configure(bg = "khaki1")
    Eggs_Label.configure(bg = "khaki1")        #Colors the respective labels/main window
    OrangeJuice_Label.configure(bg = "khaki1")
    CornFlakes_Label.configure(bg = "khaki1")
    Checkout.configure(bg = "green")
    Close.configure(bg = "red")
    
    
    Milk_Entry = tkinter.Entry(root, width = 4)   #Entry functions for user input how much of each item is bought
    Eggs_Entry = tkinter.Entry(root,  width = 4)
    OrangeJuice_Entry = tkinter.Entry(root, width = 4)
    CornFlakes_Entry = tkinter.Entry(root, width = 4)
    
    Milk_Label.grid(row = 0)
    Milk_Entry.grid(row = 0, column = 1)   #.grid for each label/entry displays the parts in the correct places
    
    Eggs_Label.grid(row = 1, sticky = "W")
    Eggs_Entry.grid(row = 1, column = 1)
    
    OrangeJuice_Label.grid(row = 0, column = 2, sticky = "W")
    OrangeJuice_Entry.grid(row = 0, column = 3, sticky = "W")
    
    CornFlakes_Label.grid(row = 1, column = 2, sticky = "W")
    CornFlakes_Entry.grid(row = 1, column = 3, sticky = "W")
    
    Checkout.grid(row = 0, column = 5)
    Close.grid(row = 1, column = 5)
    
    
    root.mainloop()   #Keeps the main window running until exit function is ran


global PriceOfItem
try:
    with open("grocerydb.csv", "r") as file:       #Opens file with pre-defined prices
        reader = csv.reader(file)
        PriceOfItem = []         #Moves prices into a list to compare with main calculation
        
        for row in reader:
            price = float(row[1])
            
            PriceOfItem.append(price)
    main = main_box()
    
except:
    tkinter.messagebox.showerror("Error!", "Please check if the correct file is selected and try again.")  #Error pop if price file is not found
