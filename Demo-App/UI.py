import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import subprocess

def select_game():
    # Hide the first page and show the second page
    select_game_frame.grid_remove()
    select_difficulty_frame.grid()

def start_game():
    # Get the selected game and difficulty
    game = game_var.get()
    difficulty = difficulty_var.get()
    print(f'Starting game: {game} with difficulty: {difficulty}')
    
def run_command():
    # Get the selected game and difficulty
    game = game_var.get()
    if(game == "PandaPickAndPlace-v1"):
    	algo = "tqc"
    else:
    	algo = "a2c"
    subprocess.run(["python3", "-m", "enjoy", "--algo", f"{algo}", "--env", f"{game}", "-n 1000"])
    #print(f'Starting game: {game} with difficulty: {difficulty}')

def create_game_frame(game_name, img_path):
    # Create a frame for the game
    game_frame = ttk.Frame(select_game_frame)
    game_frame.grid(row=0, column=0, padx=10, pady=10)

    # Create the image and button for the game
    img = Image.open(img_path)
    img = img.resize((100, 100), Image.ANTIALIAS)
    img = ImageTk.PhotoImage(img)
    game_img = ttk.Label(game_frame, image=img)
    game_img.image = img
    game_img.grid(row=0, column=0, padx=10, pady=10)
    game_button = ttk.Radiobutton(game_frame, text=game_name, variable=game_var, value=game_name)
    game_button.grid(row=0, column=1, padx=10, pady=10)

    return game_frame

# Create the main window
root = tk.Tk()
root.title('Game Selector')
root.geometry('1600x960')

# Create the first page (select game)
select_game_frame = ttk.Frame(root)
select_game_frame.grid(row=0, column=0, padx=20, pady=20)

# Create the label for selecting a game
game_var = tk.StringVar()
game_label = ttk.Label(select_game_frame, text='Select a game:', font=('Arial', 14))
game_label.grid(row=0, column=0, pady=5)

# Create the frames for each game
game1_frame = create_game_frame('PandaPickAndPlace-v1', 'ui_images/pickandplace.jpg')
game1_frame.grid(row=1, column=0)
game2_frame = create_game_frame('Ant-v3', 'ui_images/Ant')
game2_frame.grid(row=2, column=0)
game3_frame = create_game_frame('AsteroidsNoFrameskip-v4', 'ui_images/Asteroids')
game3_frame.grid(row=3, column=0)

game1_frame = create_game_frame('Acrobot-v1', 'ui_images/Acrobot.jpg')
game1_frame.grid(row=4, column=0)
game2_frame = create_game_frame('LunarLander-v2', 'ui_images/Lunarlander')
game2_frame.grid(row=5, column=0)
game3_frame = create_game_frame('BeamRiderNoFrameskip-v4', 'ui_images/Beamrider')
game3_frame.grid(row=6, column=0)

game1_frame = create_game_frame('BipedalWalkerHardcore-v3', 'ui_images/Bipedalwalker')
game1_frame.grid(row=1, column=1)
game2_frame = create_game_frame('BreakoutNoFrameskip-v4', 'ui_images/Breakout')
game2_frame.grid(row=2, column=1)
game3_frame = create_game_frame('CartPole-v1', 'ui_images/Cartpole')
game3_frame.grid(row=3, column=1)


game1_frame = create_game_frame('EnduroNoFrameskip-v4', 'ui_images/Enduro')
game1_frame.grid(row=4, column=1)
game2_frame = create_game_frame('Hopper-v3', 'ui_images/Hopper')
game2_frame.grid(row=5, column=1)
game3_frame = create_game_frame('Humanoid-v3', 'ui_images/Humanoid')
game3_frame.grid(row=6, column=1)
# Create the button to move to the next page
#next_button = ttk.Button(select_game_frame, text='Next', command=select_game, #style='Custom.TButton')

next_button = ttk.Button(text='Next', command=run_command, style='Custom.TButton')
next_button.grid(row=4, column=0, pady=5)

# Create the second page (select difficulty)
select_difficulty_frame = ttk.Frame(root)

# Create the label and combobox for selecting a difficulty
difficulty_var = tk.StringVar()
difficulty_label = ttk.Label(select_difficulty_frame, text='Select a difficulty:', font=('Arial', 14))
difficulty_label.grid(row=0, column=0, pady=5)
difficulty_combobox = ttk.Combobox(select_difficulty_frame, textvariable=difficulty_var)
difficulty_combobox['values'] = ('Easy', 'Medium', 'Hard')
difficulty_combobox.grid(row=1, column=0, pady=5)

# Create the button to start the game
start_button = ttk.Button(select_difficulty_frame, text='Start', command=start_game, style='Custom.TButton')
start_button.grid(row=2, column=0, pady=5)

# Set the style for the widgets
s = ttk.Style()
s.configure('.', font=('Arial', 12))
s.configure('Custom.TButton', foreground='blue', font=('Arial', 14))
root.mainloop()

