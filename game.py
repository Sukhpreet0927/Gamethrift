import tkinter as tk
from PIL import ImageTk
import requests
import json
from main import get_free_games, get_game_info, get_discounted_games
from tkinter import messagebox

bg_colour = "#FF0000"

   

def clear_widgets(frame):
   for widget in frame.winfo_children():
      widget.destroy()

def load_frame1():
  clear_widgets(frame2)
  clear_widgets(frame3)
  clear_widgets(frame4)
  frame1.tkraise()
  frame1.pack_propagate(False)
  response = get_free_games()
  if response.status_code == 200:
     data = response.json()
  else:
     print(f"Error: Unable to fetch data. Status code: {response.status_code}")
     


  #widgets
  logo_img = ImageTk.PhotoImage(file = "/Users/sukhpreetaulakh/Desktop/Vector-Game-Controller.png")
  logo_widget = tk.Label(frame1, image=logo_img, bg = bg_colour)
  logo_widget.image = logo_img
  logo_widget.pack()

  tk.Label(frame1, text = "Choose",bg = bg_colour, fg = "white", font = ("TkMenuFont", 14)).pack()

  # Search Entry widget
  #global search_entry
  search_entry = tk.Entry(frame1, font=("TkMenuFont", 12), bg="#badee2")
  search_entry.pack(pady=10)

  def search_game():
    search_text = search_entry.get()
    gameInfo = get_game_info(search_text)

    if gameInfo:
        print(f"Game Name: {gameInfo['name']}")
        print(f"Available Platforms: {', '.join(gameInfo['platforms'])}")
        
    load_frame3(search_text)

     
  

   # Search button widget
  tk.Button(frame1, text="Search Game",
            font=("TkHeadingFont", 16),
            bg="#28393a",
            fg="black",
            cursor="hand2",
            activebackground="#badee2",
            activeforeground="black",
            command=lambda:search_game()).pack(pady=10)


  #button widget
  tk.Button(frame1, text="Free Games", 
            font = ("TkHeadingFont", 20), 
            bg="#28393a", 
            fg="black", 
            cursor = "hand2", 
            activebackground="#badee2", 
            activeforeground="black", 
            command=lambda:load_frame2(data)).pack(pady=20)
  
  # Button widget for Discounted Games
  tk.Button(frame1, text="Discounted Games",
            font=("TkHeadingFont", 20),
            bg="#28393a",
            fg="black",
            cursor="hand2",
            activebackground="#badee2",
            activeforeground="black",
            command=lambda: load_frame4()).pack(pady=20)

 

def load_frame2(data):
    clear_widgets(frame1)
    frame2.tkraise()
    # Widgets
    logo_img = ImageTk.PhotoImage(file="/Users/sukhpreetaulakh/Desktop/Vector-Game-Controller.png")
    logo_widget = tk.Label(frame2, image=logo_img, bg=bg_colour)
    logo_widget.image = logo_img
    logo_widget.pack(pady=20)

    tk.Label(frame2, text="List of Free Games", bg=bg_colour, fg="white", font=("TkHeadingFont", 20)).pack(pady=25)

    # Create a scrollabel frame to hold the game labels
    games_frame = tk.Frame(frame2, bg=bg_colour)
    games_frame.pack(expand=True, fill='both')

    canvas = tk.Canvas(games_frame)
    scrollbar = tk.Scrollbar(games_frame, orient="vertical", command=canvas.yview)

    games_container = tk.Frame(canvas, bg=bg_colour)
    games_container.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))

    canvas.create_window((0,0), window=games_container, anchor="nw")
    canvas.configure(yscrollcommand=scrollbar.set)

    canvas.pack(side="left", fill = "both", expand=True)
    scrollbar.pack(side="right", fill="y")



    for game in data['results']:
        tk.Label(games_container, text=game['name'], bg=bg_colour, fg="white", font=("TkMenuFont", 12)).pack(pady=5)

    # Create a frame to hold the buttons
    button_frame = tk.Frame(frame2, bg=bg_colour)
    button_frame.pack(expand=True, fill='both')

    tk.Button(button_frame, text="Back", font=("TkHeadingFont", 18), bg="#28393a", fg="black", cursor="hand2",
              activebackground="#badee2", activeforeground="black", command=lambda: load_frame1()).pack(side='left')

    
  
def load_frame3(search_text):
    clear_widgets(frame1)
    frame3.tkraise()

    # Load widgets
    logo_img = ImageTk.PhotoImage(file="/Users/sukhpreetaulakh/Desktop/Vector-Game-Controller.png")
    logo_widget = tk.Label(frame3, image=logo_img, bg=bg_colour)
    logo_widget.image = logo_img
    logo_widget.pack(pady=20)

    tk.Label(frame3, text="Platform and availability", bg=bg_colour, fg="white", font=("TkHeadingFont", 20)).pack(pady=25)

    gameInfo = get_game_info(search_text)

    if gameInfo:
        tk.Label(frame3, text=f"Game Name: {gameInfo['name']}", bg=bg_colour, fg="white",
                 font=("TkMenuFont", 12)).pack(pady=5)

        platforms_label = tk.Label(frame3, text="Available Platforms:", bg=bg_colour, fg="white",
                                   font=("TkMenuFont", 12))
        platforms_label.pack(pady=5)


        for platform in gameInfo['platforms']:
            tk.Label(frame3, text=platform, bg=bg_colour, fg="black", font=("TkMenuFont", 12)).pack(pady=2)
    else:
        tk.Label(frame3, text="Game not found", bg=bg_colour, fg="white", font=("TkMenuFont", 12)).pack(pady=5)

    button_frame = tk.Frame(frame3, bg=bg_colour)
    button_frame.pack(expand=True, fill='both')

    tk.Button(button_frame, text="Back", font=("TkHeadingFont", 18), bg="#28393a", fg="black", cursor="hand2",
              activebackground="#badee2", activeforeground="black", command=lambda: load_frame1()).pack(side='left')



 
def load_frame4():
   clear_widgets(frame1)
   frame4.tkraise()
   # Widgets
   logo_img = ImageTk.PhotoImage(file="/Users/sukhpreetaulakh/Desktop/Vector-Game-Controller.png")
   logo_widget = tk.Label(frame4, image=logo_img, bg=bg_colour)
   logo_widget.image = logo_img
   logo_widget.pack(pady=20)

   tk.Label(frame4, text = "All discounted games", bg= bg_colour, fg="white", font=("TkHeadingFont", 20)).pack(pady=25)


   #Create Scroll
   games_frame = tk.Frame(frame4, bg=bg_colour)
   games_frame.pack(expand=True, fill='both')

   canvas=tk.Canvas(games_frame)
   scrollbar = tk.Scrollbar(games_frame, orient="vertical", command=canvas.yview)

   games_container = tk.Frame(canvas, bg = bg_colour)
   games_container.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))

   canvas.create_window((0,0), window=games_container, anchor="nw")
   canvas.configure(yscrollcommand=scrollbar.set)

   canvas.pack(side="left", fill = "both", expand=True)
   scrollbar.pack(side="right", fill="y")

   response = get_discounted_games()

   for game in response['results']:
    tk.Label(games_container, text=game['name'], bg= bg_colour, fg="white", font=("TkMenuFont", 12)).pack(pady=5)

   button_frame = tk.Frame(frame4, bg = bg_colour)
   button_frame.pack(expand=True, fill='both')

   tk.Button(button_frame, text="Back", font=("TkHeadingFont", 18), bg="#28393a", fg="black", cursor="hand2",
              activebackground="#badee2", activeforeground="black", command=lambda: load_frame1()).pack(side='left')



   
  




#intialize app
root = tk.Tk()
root.title("Gamethrift")
root.eval("tk::PlaceWindow . center")



#different frames for each case
frame1 = tk.Frame(root, width=500, height=600, bg = bg_colour)
frame2 = tk.Frame(root, bg=bg_colour)
frame3 = tk.Frame(root, bg=bg_colour)
frame4 = tk.Frame(root, bg = bg_colour)


frame1.grid(row=0, column = 0)
frame2.grid(row=0, column = 0)
frame3.grid(row=0, column = 0)
frame4.grid(row = 0, column =0)
 

for frame in (frame1, frame2, frame3, frame4):
  frame.grid(row=0, column=0)



if __name__ == "__main__":
  load_frame1()
  root.mainloop()


