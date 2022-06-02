import tkinter as tk
from tkinter import ttk
from tkinter import * 

root = tk.Tk()
root.title('About Application')

# frame = Frame(root)
# frame.pack()

window_width = 600
window_height = 400

# get the screen dimension
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

# find the center point
center_x = int(screen_width/2 - window_width / 2)
center_y = int(screen_height/2 - window_height / 2)

# set the position of the window to the center of the screen
root.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')

# bagian judul / kop
labelJudul = tk.Label(root,
        borderwidth = 2,
        width = 600,
        wraplength=500,
        relief="ridge",
        font=("Helvetica", 12),
        text="ANOTASI KARAKTER PADA VIDEO WAYANG KULIT DENGAN METODE EDGE DETECTION DAN ALGORITMA CONVOLUTIONAL NEURAL NETWORK (CNN)"
)

# bagian identitas developer
labelNama = tk.Label(root,
        text="Sanding Riyanto | 1811501541",
        font=("Helvetica", 12)
)

# bagian detail informasi program aplikasi
labelDetail = tk.Label(root,
        font=("Helvetica", 11),
        wraplength=600,
        text="Program aplikasi ini diperuntukan untuk mengidentifikasi karakter tokoh wayang kulit dari foto atau video wayang kulit. Dikembangkan dengan kombinasi metode Canny Adge Detection dan algoritma Convolutional Neural Network (CNN - Transfer Learning dengan Mobilnet V2), serta dengan bahasa pemrograman Python 3 - Tkinter untuk GUI-nya",
        anchor='w'
)

labelDetail2 = tk.Label(root,
        font=("Helvetica", 11),
        wraplength=600,
        text="Mekanisme pengidentifikasian karakter wayang dengan aplikasi ini adalah sebagai berikut:",
        anchor='w'
)

labelDetail3 = tk.Label(root,
        font=("Helvetica", 11),
        wraplength=600,
        text="1. Proses Preprocessing Data, 2. Training dan Build CNN Model, 3. Identifikasi citra wayang kulit, 4. Identifikasi video wayang kulit, 5. Menampilkan informasi terkait karakter wayang yang teridentifikasi",
        anchor='w'
)

# footer

# memanggil label variabel dengan fungsi Pack()
labelJudul.pack(ipadx=5, ipady=5, pady=5)
labelNama.pack()
labelDetail.pack(fill='both', pady=20)
labelDetail2.pack(fill='both')
labelDetail3.pack(fill='both')

root.mainloop()