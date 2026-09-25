import tkinter as tk
from tkinter import filedialog, messagebox
from pypdf import PdfWriter

pdf_paths = []

root = tk.Tk()
root.title("PDF Merger")
root.geometry("450x320")
root.resizable(False, False)

label = tk.Label(root, text="Select PDFs and click Merge", font=(None, 11))
label.pack(pady=8)

listbox = tk.Listbox(root, width=60, height=12, selectmode=tk.EXTENDED)
listbox.pack(padx=10)

button_frame = tk.Frame(root)
button_frame.pack(pady=8)


def add_files():
    files = filedialog.askopenfilenames(filetypes=[("PDF files", "*.pdf")])
    for path in files:
        if path not in pdf_paths:
            pdf_paths.append(path)
            listbox.insert(tk.END, path)


def remove_selected():
    for i in reversed(listbox.curselection()):
        listbox.delete(i)
        del pdf_paths[i]


def clear_all():
    listbox.delete(0, tk.END)
    pdf_paths.clear()


def merge_pdfs():
    if not pdf_paths:
        return messagebox.showwarning("No PDFs", "Add at least one PDF first.")

    out = filedialog.asksaveasfilename(defaultextension=".pdf", filetypes=[("PDF files", "*.pdf")], initialfile="merged.pdf")
    if not out:
        return

    try:
        writer = PdfWriter()
        for path in pdf_paths:
            writer.append(path)
        writer.write(out)
        messagebox.showinfo("Done", f"Merged {len(pdf_paths)} PDFs into:\n{out}")
    except Exception as e:
        messagebox.showerror("Error", str(e))


btn_add = tk.Button(button_frame, text="Add PDFs", width=10, command=add_files)
btn_add.grid(row=0, column=0, padx=4)
btn_remove = tk.Button(button_frame, text="Remove", width=10, command=remove_selected)
btn_remove.grid(row=0, column=1, padx=4)
btn_clear = tk.Button(button_frame, text="Clear", width=10, command=clear_all)
btn_clear.grid(row=0, column=2, padx=4)
btn_merge = tk.Button(button_frame, text="Merge", width=10, command=merge_pdfs, bg="#2e7d32", fg="white")
btn_merge.grid(row=0, column=3, padx=4)

root.mainloop()

