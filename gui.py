import tkinter as tk
from tkinter import ttk, filedialog
from sequence import Sequence
from parser import parse_fasta


def run_gui():
    root = tk.Tk()
    app = FastaAnalyzerGUI(root)
    root.mainloop()


class FastaAnalyzerGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("FASTA Analyzer")
        self.root.geometry("1400x800")

        self.file = None
        self.sequences = []

        self.create_widgets()

    def open_file(self):
        self.file = filedialog.askopenfilename()

        if not self.file:
            return

        temp = parse_fasta(self.file)
        for header, sequence in temp:
            self.sequences.append(Sequence(header, sequence))

        print(self.sequences)
        self.list_sequences()

    def list_sequences(self):
        self.sequence_listbox.delete(0, tk.END)

        for sequence in self.sequences:
            self.sequence_listbox.insert(tk.END, sequence)

    def display_stats(self):
        selected = self.sequence_listbox.curselection()
        #curselection returns a tuple that stores the index of the selected item

        if not selected:
            return

        sequence = self.sequences[selected[0]]

        self.header_label.config(text=f"Header: {sequence.header()}")
        self.length_label.config(text=f"Length: {sequence.sequence_length()}")
        self.gc_label.config(text=f"GC Content: {sequence.gc_content(): 2f}%")
        self.at_label.config(text=f"AT Content: {sequence.at_content(): 2f}%")

        self.sequence_label.config(state="normal")
        self.sequence_label.delete("1.0", tk.END)
        self.sequence_label.insert("1.0", sequence.sequence())
        self.sequence_label.config(state="disabled")

    def display_complement(self):
        selected = self.sequence_listbox.curselection()

        if not selected:
            return

        sequence = self.sequences[selected[0]]
        self.output_box.delete("1.0", tk.END)
        self.output_box.insert("1.0", sequence.complement())

    def display_reverse_complement(self):
        selected = self.sequence_listbox.curselection()

        if not selected:
            return

        sequence = self.sequences[selected[0]]
        self.output_box.delete("1.0", tk.END)
        self.output_box.insert("1.0", sequence.reverse_complement())

    def display_codon(self):
        return

    def create_buttons(self, button_frame):
        ttk.Button(button_frame, text="Display Stats", command=self.display_stats).pack(side="left", padx=5)
        ttk.Button(button_frame, text="Codon Frequency").pack(side="left", padx=5)
        ttk.Button(button_frame, text="Complement", command=self.display_complement).pack(side="left", padx=5)
        ttk.Button(button_frame, text="Reverse Complement", command=self.display_reverse_complement).pack(side="left",padx=5)

    def _create_top_bar(self):
        top_frame = ttk.Frame(self.root, padding=10)
        top_frame.pack(fill="x")

        ttk.Label(top_frame, text="FASTA Analyzer", font=("Arial", 20, "bold")).pack(side="left")
        ttk.Button(top_frame, text="Open FASTA File", command=self.open_file).pack(side="right")

    def _create_sequence_panel(self, parent):
        left_frame = ttk.Frame(parent, width=400)
        left_frame.pack(side="left", fill="both", expand=False, padx=(0, 30))

        ttk.Label(left_frame, text="Sequences", font=("Arial", 14, "bold")).pack(anchor="w")

        self.sequence_listbox = tk.Listbox(left_frame, width=50)
        self.sequence_listbox.pack(fill="both", expand=True, pady=10)

        self.x_scrollbar = tk.Scrollbar(left_frame, orient="horizontal")
        self.x_scrollbar.pack(fill="x")

        self.sequence_listbox.config(xscrollcommand=self.x_scrollbar.set)
        self.x_scrollbar.config(command=self.sequence_listbox.xview)

    def _create_stats_panel(self, parent):
        right_frame = ttk.Frame(parent)
        right_frame.pack(side="left", fill="both", expand=True, padx=(30, 0))

        ttk.Label(right_frame, text="Stats", font=("Arial", 14, "bold")).pack(anchor="w")

        self.header_label = ttk.Label(right_frame, text="Header:")
        self.header_label.pack(anchor="w", pady=5)

        self.sequence_label_title = ttk.Label(right_frame, text="Sequence:")
        self.sequence_label_title.pack(anchor="w", pady=(5, 0))

        self.sequence_label = tk.Text(right_frame, height=4, wrap="word", state="disabled", relief="flat")
        self.sequence_label.pack(fill="x", anchor="w", pady=(0, 5))

        self.length_label = ttk.Label(right_frame, text="Length:")
        self.length_label.pack(anchor="w", pady=5)

        self.gc_label = ttk.Label(right_frame, text="GC Content:")
        self.gc_label.pack(anchor="w", pady=5)

        self.at_label = ttk.Label(right_frame, text="AT Content:")
        self.at_label.pack(anchor="w", pady=5)

        button_frame = ttk.Frame(right_frame)
        button_frame.pack(anchor="w", pady=15)
        self.create_buttons(button_frame)

        ttk.Label(right_frame, text="Output", font=("Arial", 12, "bold")).pack(anchor="w")

        self.output_box = tk.Text(right_frame, height=12)
        self.output_box.pack(fill="both", expand=True, pady=5)

    def create_widgets(self):
        self._create_top_bar()

        main_frame = ttk.Frame(self.root, padding=20)
        main_frame.pack(fill="both", expand=True)

        self._create_sequence_panel(main_frame)
        self._create_stats_panel(main_frame)