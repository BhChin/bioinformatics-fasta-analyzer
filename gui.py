import tkinter as tk
from tkinter import ttk, filedialog




class FastaAnalyzerGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("FASTA Analyzer")
        self.root.geometry("1000x600")
        self.file = None

        self.create_widgets()

    def open_file(self):
        self.file = filedialog.askopenfilename()
        print(self.file)

    def create_widgets(self):
        top_frame = ttk.Frame(self.root, padding=10)
        top_frame.pack(fill="x")

        title = ttk.Label(top_frame, text="FASTA Analyzer", font=("Arial", 20, "bold"))
        title.pack(side="left")

        file_open_button = ttk.Button(top_frame, text="Open FASTA File", command=self.open_file)
        file_open_button.pack(side="right")

        main_frame = ttk.Frame(self.root, padding=10)
        main_frame.pack(fill="both", expand=True)

        left_frame = ttk.Frame(main_frame, width=250)
        left_frame.pack(side="left", fill="y")

        right_frame = ttk.Frame(main_frame)
        right_frame.pack(side="right", fill="both", expand=True)

        ttk.Label(left_frame, text="Sequences", font=("Arial", 14, "bold")).pack(anchor="w")

        self.sequence_listbox = tk.Listbox(left_frame)
        self.sequence_listbox.pack(fill="both", expand=True, pady=10)

        ttk.Label(right_frame, text="Stats", font=("Arial", 14, "bold")).pack(anchor="w")

        self.header_label = ttk.Label(right_frame, text="Header:")
        self.header_label.pack(anchor="w", pady=5)

        self.length_label = ttk.Label(right_frame, text="Length:")
        self.length_label.pack(anchor="w", pady=5)

        self.gc_label = ttk.Label(right_frame, text="GC Content:")
        self.gc_label.pack(anchor="w", pady=5)

        self.at_label = ttk.Label(right_frame, text="AT Content:")
        self.at_label.pack(anchor="w", pady=5)

        button_frame = ttk.Frame(right_frame)
        button_frame.pack(anchor="w", pady=15)

        ttk.Button(button_frame, text="Complement").pack(side="left", padx=5)
        ttk.Button(button_frame, text="Reverse Complement").pack(side="left", padx=5)
        ttk.Button(button_frame, text="Codon Frequency").pack(side="left", padx=5)

        ttk.Label(right_frame, text="Output", font=("Arial", 12, "bold")).pack(anchor="w")

        self.output_box = tk.Text(right_frame, height=12)
        self.output_box.pack(fill="both", expand=True, pady=5)


def main():
    root = tk.Tk()
    app = FastaAnalyzerGUI(root)
    root.mainloop()


if __name__ == "__main__":
    main()