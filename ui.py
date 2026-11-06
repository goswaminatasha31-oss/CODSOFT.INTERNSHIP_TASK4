import tkinter as tk
class GameUI:
    def __init__(self, root, play_function, reset_function):
        self.root = root
        self.play_function = play_function
        self.reset_function = reset_function
        self.root.title("Rock Paper Scissors")
        self.root.geometry("550x580")
        self.root.resizable(False, False)
        self.root.config(bg="#20243A")
        # Heading
        tk.Label(
            root,
            text="ROCK PAPER SCISSORS",
            font=("Arial", 23, "bold"),
            bg="#20243A",
            fg="white"
        ).pack(pady=(30, 8))
        tk.Label(
            root,
            text="Play against the computer!",
            font=("Arial", 12),
            bg="#20243A",
            fg="#AAB1C5"
        ).pack()
        # Score
        self.score_label = tk.Label(
            root,
            text="You: 0     Draw: 0     Computer: 0",
            font=("Arial", 13, "bold"),
            bg="#303750",
            fg="white",
            padx=15,
            pady=15
        )
        self.score_label.pack(pady=30)
        # Choices
        choice_frame = tk.Frame(root, bg="#20243A")
        choice_frame.pack(pady=15)
        self.user_label = tk.Label(
            choice_frame,
            text="Your Choice",
            font=("Arial", 14, "bold"),
            bg="#303750",
            fg="#40D69A",
            width=15,
            height=3
        )
        self.user_label.pack(side="left", padx=10)
        self.computer_label = tk.Label(
            choice_frame,
            text="Computer Choice",
            font=("Arial", 14, "bold"),
            bg="#303750",
            fg="#FF647C",
            width=15,
            height=3
        )
        self.computer_label.pack(side="left", padx=10)
        # Result
        self.result_label = tk.Label(
            root,
            text="Choose your move!",
            font=("Arial", 17, "bold"),
            bg="#20243A",
            fg="white"
        )
        self.result_label.pack(pady=25)
        # Game buttons
        button_frame = tk.Frame(root, bg="#20243A")
        button_frame.pack(pady=10)
        self.create_button(
            button_frame, "Rock", "✊ Rock"
        )
        self.create_button(
            button_frame, "Paper", "✋ Paper"
        )
        self.create_button(
            button_frame, "Scissors", "✌ Scissors"
        )
        # Reset button
        tk.Button(
            root,
            text="Reset Game",
            font=("Arial", 11, "bold"),
            bg="#3B435D",
            fg="white",
            width=18,
            pady=9,
            bd=0,
            cursor="hand2",
            command=self.reset_function
        ).pack(pady=25)
        # Footer
        tk.Label(
            root,
            text="CODSOFT PYTHON INTERNSHIP - TASK 4",
            font=("Arial", 9),
            bg="#20243A",
            fg="#AAB1C5"
        ).pack(side="bottom", pady=12)
    def create_button(self, parent, choice, text):
        tk.Button(
            parent,
            text=text,
            font=("Arial", 13, "bold"),
            bg="#6755D9",
            fg="white",
            activebackground="#8271F0",
            activeforeground="white",
            width=12,
            height=2,
            bd=0,
            cursor="hand2",
            command=lambda: self.play_function(choice)
        ).pack(side="left", padx=5)
    def show_result(self, user, computer, result):
        self.user_label.config(text=user)
        self.computer_label.config(text=computer)
        if result == "Win":
            message = "Congratulations! You Won!"
            color = "#40D69A"
        elif result == "Lose":
            message = "Computer Won! Try Again."
            color = "#FF647C"
        else:
            message = "It's a Draw!"
            color = "#FFC857"
        self.result_label.config(
            text=message,
            fg=color
        )
    def update_score(self, user, draw, computer):
        self.score_label.config(
            text=f"You: {user}     Draw: {draw}     Computer: {computer}"
        )
    def reset_display(self):
        self.user_label.config(text="Your Choice")
        self.computer_label.config(text="Computer Choice")
        self.result_label.config(
            text="Choose your move!",
            fg="white"
        )