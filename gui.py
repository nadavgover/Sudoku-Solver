from tkinter import *
import Sudoku

class SudokuGui(object):
    def __init__(self):
        self.root = Tk()
        self.sudoku = None
        self.callId = None

        font = ('Verdana', 20)  # the size of the font determines the height of the cell
        cell_size = 2
        padding = 2
        validate_cmd = (self.root.register(self.allow_only_one_digit))  # validate command

        # first row
        self.cell00 = StringVar()
        self.cell00_entry = Entry(self.root, width=cell_size, font=font, justify=CENTER,
                                 borderwidth=0, highlightthickness=1, highlightbackground="black",
                                 textvariable=self.cell00, bg="light grey",
                                 validate='all', validatecommand=(validate_cmd, '%P'))
        self.cell00_entry.grid(row=0, column=0)

        self.cell01 = StringVar()
        self.cell01_entry = Entry(self.root, width=cell_size, font=font, justify=CENTER,
                                  borderwidth=0, highlightthickness=1, highlightbackground="black",
                                  textvariable=self.cell01, bg="light grey",
                                  validate='all', validatecommand=(validate_cmd, '%P'))
        self.cell01_entry.grid(row=0, column=1)

        self.cell02 = StringVar()
        self.cell02_entry = Entry(self.root, width=cell_size, font=font, justify=CENTER,
                                  borderwidth=0, highlightthickness=1, highlightbackground="black",
                                  textvariable=self.cell02, bg="light grey",
                                  validate='all', validatecommand=(validate_cmd, '%P'))
        self.cell02_entry.grid(row=0, column=2, padx=(0, padding))

        self.cell03 = StringVar()
        self.cell03_entry = Entry(self.root, width=cell_size, font=font, justify=CENTER,
                                  borderwidth=0, highlightthickness=1, highlightbackground="black",
                                  textvariable=self.cell03, bg="white",
                                  validate='all', validatecommand=(validate_cmd, '%P'))
        self.cell03_entry.grid(row=0, column=3)

        self.cell04 = StringVar()
        self.cell04_entry = Entry(self.root, width=cell_size, font=font, justify=CENTER,
                                  borderwidth=0, highlightthickness=1, highlightbackground="black",
                                  textvariable=self.cell04, bg="white",
                                  validate='all', validatecommand=(validate_cmd, '%P'))
        self.cell04_entry.grid(row=0, column=4)

        self.cell05 = StringVar()
        self.cell05_entry = Entry(self.root, width=cell_size, font=font, justify=CENTER,
                                  borderwidth=0, highlightthickness=1, highlightbackground="black",
                                  textvariable=self.cell05, bg="white",
                                  validate='all', validatecommand=(validate_cmd, '%P'))
        self.cell05_entry.grid(row=0, column=5, padx=(0, padding))

        self.cell06 = StringVar()
        self.cell06_entry = Entry(self.root, width=cell_size, font=font, justify=CENTER,
                                  borderwidth=0, highlightthickness=1, highlightbackground="black",
                                  textvariable=self.cell06, bg="light grey",
                                  validate='all', validatecommand=(validate_cmd, '%P'))
        self.cell06_entry.grid(row=0, column=6)

        self.cell07 = StringVar()
        self.cell07_entry = Entry(self.root, width=cell_size, font=font, justify=CENTER,
                                  borderwidth=0, highlightthickness=1, highlightbackground="black",
                                  textvariable=self.cell07, bg="light grey",
                                  validate='all', validatecommand=(validate_cmd, '%P'))
        self.cell07_entry.grid(row=0, column=7)

        self.cell08 = StringVar()
        self.cell08_entry = Entry(self.root, width=cell_size, font=font, justify=CENTER,
                                  borderwidth=0, highlightthickness=1, highlightbackground="black",
                                  textvariable=self.cell08, bg="light grey",
                                  validate='all', validatecommand=(validate_cmd, '%P'))
        self.cell08_entry.grid(row=0, column=8)

        # second row
        self.cell10 = StringVar()
        self.cell10_entry = Entry(self.root, width=cell_size, font=font, justify=CENTER,
                                  borderwidth=0, highlightthickness=1, highlightbackground="black",
                                  textvariable=self.cell10, bg="white",
                                  validate='all', validatecommand=(validate_cmd, '%P'))
        self.cell10_entry.grid(row=1, column=0)

        self.cell11 = StringVar()
        self.cell11_entry = Entry(self.root, width=cell_size, font=font, justify=CENTER,
                                  borderwidth=0, highlightthickness=1, highlightbackground="black",
                                  textvariable=self.cell11, bg="white",
                                  validate='all', validatecommand=(validate_cmd, '%P'))
        self.cell11_entry.grid(row=1, column=1)

        self.cell12 = StringVar()
        self.cell12_entry = Entry(self.root, width=cell_size, font=font, justify=CENTER,
                                  borderwidth=0, highlightthickness=1, highlightbackground="black",
                                  textvariable=self.cell12, bg="white",
                                  validate='all', validatecommand=(validate_cmd, '%P'))
        self.cell12_entry.grid(row=1, column=2, padx=(0, padding))

        self.cell13 = StringVar()
        self.cell13_entry = Entry(self.root, width=cell_size, font=font, justify=CENTER,
                                  borderwidth=0, highlightthickness=1, highlightbackground="black",
                                  textvariable=self.cell13, bg="light grey",
                                  validate='all', validatecommand=(validate_cmd, '%P'))
        self.cell13_entry.grid(row=1, column=3)

        self.cell14 = StringVar()
        self.cell14_entry = Entry(self.root, width=cell_size, font=font, justify=CENTER,
                                  borderwidth=0, highlightthickness=1, highlightbackground="black",
                                  textvariable=self.cell14, bg="light grey",
                                  validate='all', validatecommand=(validate_cmd, '%P'))
        self.cell14_entry.grid(row=1, column=4)

        self.cell15 = StringVar()
        self.cell15_entry = Entry(self.root, width=cell_size, font=font, justify=CENTER,
                                  borderwidth=0, highlightthickness=1, highlightbackground="black",
                                  textvariable=self.cell15, bg="light grey",
                                  validate='all', validatecommand=(validate_cmd, '%P'))
        self.cell15_entry.grid(row=1, column=5, padx=(0, padding))

        self.cell16 = StringVar()
        self.cell16_entry = Entry(self.root, width=cell_size, font=font, justify=CENTER,
                                  borderwidth=0, highlightthickness=1, highlightbackground="black",
                                  textvariable=self.cell16, bg="white",
                                  validate='all', validatecommand=(validate_cmd, '%P'))
        self.cell16_entry.grid(row=1, column=6)

        self.cell17 = StringVar()
        self.cell17_entry = Entry(self.root, width=cell_size, font=font, justify=CENTER,
                                  borderwidth=0, highlightthickness=1, highlightbackground="black",
                                  textvariable=self.cell17, bg="white",
                                  validate='all', validatecommand=(validate_cmd, '%P'))
        self.cell17_entry.grid(row=1, column=7)

        self.cell18 = StringVar()
        self.cell18_entry = Entry(self.root, width=cell_size, font=font, justify=CENTER,
                                  borderwidth=0, highlightthickness=1, highlightbackground="black",
                                  textvariable=self.cell18, bg="white",
                                  validate='all', validatecommand=(validate_cmd, '%P'))
        self.cell18_entry.grid(row=1, column=8)

        # third row
        self.cell20 = StringVar()
        self.cell20_entry = Entry(self.root, width=cell_size, font=font, justify=CENTER,
                                 borderwidth=0, highlightthickness=1, highlightbackground="black",
                                 textvariable=self.cell20, bg="light grey",
                                 validate='all', validatecommand=(validate_cmd, '%P'))
        self.cell20_entry.grid(row=2, column=0, pady=(0, padding))

        self.cell21 = StringVar()
        self.cell21_entry = Entry(self.root, width=cell_size, font=font, justify=CENTER,
                                  borderwidth=0, highlightthickness=1, highlightbackground="black",
                                  textvariable=self.cell21, bg="light grey",
                                  validate='all', validatecommand=(validate_cmd, '%P'))
        self.cell21_entry.grid(row=2, column=1, pady=(0, padding))

        self.cell22 = StringVar()
        self.cell22_entry = Entry(self.root, width=cell_size, font=font, justify=CENTER,
                                  borderwidth=0, highlightthickness=1, highlightbackground="black",
                                  textvariable=self.cell22, bg="light grey",
                                  validate='all', validatecommand=(validate_cmd, '%P'))
        self.cell22_entry.grid(row=2, column=2, pady=(0, padding), padx=(0, padding))

        self.cell23 = StringVar()
        self.cell23_entry = Entry(self.root, width=cell_size, font=font, justify=CENTER,
                                  borderwidth=0, highlightthickness=1, highlightbackground="black",
                                  textvariable=self.cell23, bg="white",
                                  validate='all', validatecommand=(validate_cmd, '%P'))
        self.cell23_entry.grid(row=2, column=3, pady=(0, padding))

        self.cell24 = StringVar()
        self.cell24_entry = Entry(self.root, width=cell_size, font=font, justify=CENTER,
                                  borderwidth=0, highlightthickness=1, highlightbackground="black",
                                  textvariable=self.cell24, bg="white",
                                  validate='all', validatecommand=(validate_cmd, '%P'))
        self.cell24_entry.grid(row=2, column=4, pady=(0, padding))

        self.cell25 = StringVar()
        self.cell25_entry = Entry(self.root, width=cell_size, font=font, justify=CENTER,
                                  borderwidth=0, highlightthickness=1, highlightbackground="black",
                                  textvariable=self.cell25, bg="white",
                                  validate='all', validatecommand=(validate_cmd, '%P'))
        self.cell25_entry.grid(row=2, column=5, pady=(0, padding), padx=(0, padding))

        self.cell26 = StringVar()
        self.cell26_entry = Entry(self.root, width=cell_size, font=font, justify=CENTER,
                                  borderwidth=0, highlightthickness=1, highlightbackground="black",
                                  textvariable=self.cell26, bg="light grey",
                                  validate='all', validatecommand=(validate_cmd, '%P'))
        self.cell26_entry.grid(row=2, column=6, pady=(0, padding))

        self.cell27 = StringVar()
        self.cell27_entry = Entry(self.root, width=cell_size, font=font, justify=CENTER,
                                  borderwidth=0, highlightthickness=1, highlightbackground="black",
                                  textvariable=self.cell27, bg="light grey",
                                  validate='all', validatecommand=(validate_cmd, '%P'))
        self.cell27_entry.grid(row=2, column=7, pady=(0, padding))

        self.cell28 = StringVar()
        self.cell28_entry = Entry(self.root, width=cell_size, font=font, justify=CENTER,
                                  borderwidth=0, highlightthickness=1, highlightbackground="black",
                                  textvariable=self.cell28, bg="light grey",
                                  validate='all', validatecommand=(validate_cmd, '%P'))
        self.cell28_entry.grid(row=2, column=8, pady=(0, padding))

        # fourth row
        self.cell30 = StringVar()
        self.cell30_entry = Entry(self.root, width=cell_size, font=font, justify=CENTER,
                                  borderwidth=0, highlightthickness=1, highlightbackground="black",
                                  textvariable=self.cell30, bg="white",
                                  validate='all', validatecommand=(validate_cmd, '%P'))
        self.cell30_entry.grid(row=3, column=0)

        self.cell31 = StringVar()
        self.cell31_entry = Entry(self.root, width=cell_size, font=font, justify=CENTER,
                                  borderwidth=0, highlightthickness=1, highlightbackground="black",
                                  textvariable=self.cell31, bg="white",
                                  validate='all', validatecommand=(validate_cmd, '%P'))
        self.cell31_entry.grid(row=3, column=1)

        self.cell32 = StringVar()
        self.cell32_entry = Entry(self.root, width=cell_size, font=font, justify=CENTER,
                                  borderwidth=0, highlightthickness=1, highlightbackground="black",
                                  textvariable=self.cell32, bg="white",
                                  validate='all', validatecommand=(validate_cmd, '%P'))
        self.cell32_entry.grid(row=3, column=2, padx=(0, padding))

        self.cell33 = StringVar()
        self.cell33_entry = Entry(self.root, width=cell_size, font=font, justify=CENTER,
                                  borderwidth=0, highlightthickness=1, highlightbackground="black",
                                  textvariable=self.cell33, bg="light grey",
                                  validate='all', validatecommand=(validate_cmd, '%P'))
        self.cell33_entry.grid(row=3, column=3)

        self.cell34 = StringVar()
        self.cell34_entry = Entry(self.root, width=cell_size, font=font, justify=CENTER,
                                  borderwidth=0, highlightthickness=1, highlightbackground="black",
                                  textvariable=self.cell34, bg="light grey",
                                  validate='all', validatecommand=(validate_cmd, '%P'))
        self.cell34_entry.grid(row=3, column=4)

        self.cell35 = StringVar()
        self.cell35_entry = Entry(self.root, width=cell_size, font=font, justify=CENTER,
                                  borderwidth=0, highlightthickness=1, highlightbackground="black",
                                  textvariable=self.cell35, bg="light grey",
                                  validate='all', validatecommand=(validate_cmd, '%P'))
        self.cell35_entry.grid(row=3, column=5, padx=(0, padding))

        self.cell36 = StringVar()
        self.cell36_entry = Entry(self.root, width=cell_size, font=font, justify=CENTER,
                                  borderwidth=0, highlightthickness=1, highlightbackground="black",
                                  textvariable=self.cell36, bg="white",
                                  validate='all', validatecommand=(validate_cmd, '%P'))
        self.cell36_entry.grid(row=3, column=6)

        self.cell37 = StringVar()
        self.cell37_entry = Entry(self.root, width=cell_size, font=font, justify=CENTER,
                                  borderwidth=0, highlightthickness=1, highlightbackground="black",
                                  textvariable=self.cell37, bg="white",
                                  validate='all', validatecommand=(validate_cmd, '%P'))
        self.cell37_entry.grid(row=3, column=7)

        self.cell38 = StringVar()
        self.cell38_entry = Entry(self.root, width=cell_size, font=font, justify=CENTER,
                                  borderwidth=0, highlightthickness=1, highlightbackground="black",
                                  textvariable=self.cell38, bg="white",
                                  validate='all', validatecommand=(validate_cmd, '%P'))
        self.cell38_entry.grid(row=3, column=8)

        # fifth row
        self.cell40 = StringVar()
        self.cell40_entry = Entry(self.root, width=cell_size, font=font, justify=CENTER,
                                  borderwidth=0, highlightthickness=1, highlightbackground="black",
                                  textvariable=self.cell40, bg="light grey",
                                  validate='all', validatecommand=(validate_cmd, '%P'))
        self.cell40_entry.grid(row=4, column=0)

        self.cell41 = StringVar()
        self.cell41_entry = Entry(self.root, width=cell_size, font=font, justify=CENTER,
                                  borderwidth=0, highlightthickness=1, highlightbackground="black",
                                  textvariable=self.cell41, bg="light grey",
                                  validate='all', validatecommand=(validate_cmd, '%P'))
        self.cell41_entry.grid(row=4, column=1)

        self.cell42 = StringVar()
        self.cell42_entry = Entry(self.root, width=cell_size, font=font, justify=CENTER,
                                  borderwidth=0, highlightthickness=1, highlightbackground="black",
                                  textvariable=self.cell42, bg="light grey",
                                  validate='all', validatecommand=(validate_cmd, '%P'))
        self.cell42_entry.grid(row=4, column=2, padx=(0, padding))

        self.cell43 = StringVar()
        self.cell43_entry = Entry(self.root, width=cell_size, font=font, justify=CENTER,
                                  borderwidth=0, highlightthickness=1, highlightbackground="black",
                                  textvariable=self.cell43, bg="white",
                                  validate='all', validatecommand=(validate_cmd, '%P'))
        self.cell43_entry.grid(row=4, column=3)

        self.cell44 = StringVar()
        self.cell44_entry = Entry(self.root, width=cell_size, font=font, justify=CENTER,
                                  borderwidth=0, highlightthickness=1, highlightbackground="black",
                                  textvariable=self.cell44, bg="white",
                                  validate='all', validatecommand=(validate_cmd, '%P'))
        self.cell44_entry.grid(row=4, column=4)

        self.cell45 = StringVar()
        self.cell45_entry = Entry(self.root, width=cell_size, font=font, justify=CENTER,
                                  borderwidth=0, highlightthickness=1, highlightbackground="black",
                                  textvariable=self.cell45, bg="white",
                                  validate='all', validatecommand=(validate_cmd, '%P'))
        self.cell45_entry.grid(row=4, column=5, padx=(0, padding))

        self.cell46 = StringVar()
        self.cell46_entry = Entry(self.root, width=cell_size, font=font, justify=CENTER,
                                  borderwidth=0, highlightthickness=1, highlightbackground="black",
                                  textvariable=self.cell46, bg="light grey",
                                  validate='all', validatecommand=(validate_cmd, '%P'))
        self.cell46_entry.grid(row=4, column=6)

        self.cell47 = StringVar()
        self.cell47_entry = Entry(self.root, width=cell_size, font=font, justify=CENTER,
                                  borderwidth=0, highlightthickness=1, highlightbackground="black",
                                  textvariable=self.cell47, bg="light grey",
                                  validate='all', validatecommand=(validate_cmd, '%P'))
        self.cell47_entry.grid(row=4, column=7)

        self.cell48 = StringVar()
        self.cell48_entry = Entry(self.root, width=cell_size, font=font, justify=CENTER,
                                  borderwidth=0, highlightthickness=1, highlightbackground="black",
                                  textvariable=self.cell48, bg="light grey",
                                  validate='all', validatecommand=(validate_cmd, '%P'))
        self.cell48_entry.grid(row=4, column=8)

        # sixth row
        self.cell50 = StringVar()
        self.cell50_entry = Entry(self.root, width=cell_size, font=font, justify=CENTER,
                                  borderwidth=0, highlightthickness=1, highlightbackground="black",
                                  textvariable=self.cell50, bg="white",
                                  validate='all', validatecommand=(validate_cmd, '%P'))
        self.cell50_entry.grid(row=5, column=0, pady=(0, padding))

        self.cell51 = StringVar()
        self.cell51_entry = Entry(self.root, width=cell_size, font=font, justify=CENTER,
                                  borderwidth=0, highlightthickness=1, highlightbackground="black",
                                  textvariable=self.cell51, bg="white",
                                  validate='all', validatecommand=(validate_cmd, '%P'))
        self.cell51_entry.grid(row=5, column=1, pady=(0, padding))

        self.cell52 = StringVar()
        self.cell52_entry = Entry(self.root, width=cell_size, font=font, justify=CENTER,
                                  borderwidth=0, highlightthickness=1, highlightbackground="black",
                                  textvariable=self.cell52, bg="white",
                                  validate='all', validatecommand=(validate_cmd, '%P'))
        self.cell52_entry.grid(row=5, column=2, pady=(0, padding), padx=(0, padding))

        self.cell53 = StringVar()
        self.cell53_entry = Entry(self.root, width=cell_size, font=font, justify=CENTER,
                                  borderwidth=0, highlightthickness=1, highlightbackground="black",
                                  textvariable=self.cell53, bg="light grey",
                                  validate='all', validatecommand=(validate_cmd, '%P'))
        self.cell53_entry.grid(row=5, column=3, pady=(0, padding))

        self.cell54 = StringVar()
        self.cell54_entry = Entry(self.root, width=cell_size, font=font, justify=CENTER,
                                  borderwidth=0, highlightthickness=1, highlightbackground="black",
                                  textvariable=self.cell54, bg="light grey",
                                  validate='all', validatecommand=(validate_cmd, '%P'))
        self.cell54_entry.grid(row=5, column=4, pady=(0, padding))

        self.cell55 = StringVar()
        self.cell55_entry = Entry(self.root, width=cell_size, font=font, justify=CENTER,
                                  borderwidth=0, highlightthickness=1, highlightbackground="black",
                                  textvariable=self.cell55, bg="light grey",
                                  validate='all', validatecommand=(validate_cmd, '%P'))
        self.cell55_entry.grid(row=5, column=5, pady=(0, padding), padx=(0, padding))

        self.cell56 = StringVar()
        self.cell56_entry = Entry(self.root, width=cell_size, font=font, justify=CENTER,
                                  borderwidth=0, highlightthickness=1, highlightbackground="black",
                                  textvariable=self.cell56, bg="white",
                                  validate='all', validatecommand=(validate_cmd, '%P'))
        self.cell56_entry.grid(row=5, column=6, pady=(0, padding))

        self.cell57 = StringVar()
        self.cell57_entry = Entry(self.root, width=cell_size, font=font, justify=CENTER,
                                  borderwidth=0, highlightthickness=1, highlightbackground="black",
                                  textvariable=self.cell57, bg="white",
                                  validate='all', validatecommand=(validate_cmd, '%P'))
        self.cell57_entry.grid(row=5, column=7, pady=(0, padding))

        self.cell58 = StringVar()
        self.cell58_entry = Entry(self.root, width=cell_size, font=font, justify=CENTER,
                                  borderwidth=0, highlightthickness=1, highlightbackground="black",
                                  textvariable=self.cell58, bg="white",
                                  validate='all', validatecommand=(validate_cmd, '%P'))
        self.cell58_entry.grid(row=5, column=8, pady=(0, padding))

        # seventh row
        self.cell60 = StringVar()
        self.cell60_entry = Entry(self.root, width=cell_size, font=font, justify=CENTER,
                                  borderwidth=0, highlightthickness=1, highlightbackground="black",
                                  textvariable=self.cell60, bg="light grey",
                                  validate='all', validatecommand=(validate_cmd, '%P'))
        self.cell60_entry.grid(row=6, column=0)

        self.cell61 = StringVar()
        self.cell61_entry = Entry(self.root, width=cell_size, font=font, justify=CENTER,
                                  borderwidth=0, highlightthickness=1, highlightbackground="black",
                                  textvariable=self.cell61, bg="light grey",
                                  validate='all', validatecommand=(validate_cmd, '%P'))
        self.cell61_entry.grid(row=6, column=1)

        self.cell62 = StringVar()
        self.cell62_entry = Entry(self.root, width=cell_size, font=font, justify=CENTER,
                                  borderwidth=0, highlightthickness=1, highlightbackground="black",
                                  textvariable=self.cell62, bg="light grey",
                                  validate='all', validatecommand=(validate_cmd, '%P'))
        self.cell62_entry.grid(row=6, column=2, padx=(0, padding))

        self.cell63 = StringVar()
        self.cell63_entry = Entry(self.root, width=cell_size, font=font, justify=CENTER,
                                  borderwidth=0, highlightthickness=1, highlightbackground="black",
                                  textvariable=self.cell63, bg="white",
                                  validate='all', validatecommand=(validate_cmd, '%P'))
        self.cell63_entry.grid(row=6, column=3)

        self.cell64 = StringVar()
        self.cell64_entry = Entry(self.root, width=cell_size, font=font, justify=CENTER,
                                  borderwidth=0, highlightthickness=1, highlightbackground="black",
                                  textvariable=self.cell64, bg="white",
                                  validate='all', validatecommand=(validate_cmd, '%P'))
        self.cell64_entry.grid(row=6, column=4)

        self.cell65 = StringVar()
        self.cell65_entry = Entry(self.root, width=cell_size, font=font, justify=CENTER,
                                  borderwidth=0, highlightthickness=1, highlightbackground="black",
                                  textvariable=self.cell65, bg="white",
                                  validate='all', validatecommand=(validate_cmd, '%P'))
        self.cell65_entry.grid(row=6, column=5, padx=(0, padding))

        self.cell66 = StringVar()
        self.cell66_entry = Entry(self.root, width=cell_size, font=font, justify=CENTER,
                                  borderwidth=0, highlightthickness=1, highlightbackground="black",
                                  textvariable=self.cell66, bg="light grey",
                                  validate='all', validatecommand=(validate_cmd, '%P'))
        self.cell66_entry.grid(row=6, column=6)

        self.cell67 = StringVar()
        self.cell67_entry = Entry(self.root, width=cell_size, font=font, justify=CENTER,
                                  borderwidth=0, highlightthickness=1, highlightbackground="black",
                                  textvariable=self.cell67, bg="light grey",
                                  validate='all', validatecommand=(validate_cmd, '%P'))
        self.cell67_entry.grid(row=6, column=7)

        self.cell68 = StringVar()
        self.cell68_entry = Entry(self.root, width=cell_size, font=font, justify=CENTER,
                                  borderwidth=0, highlightthickness=1, highlightbackground="black",
                                  textvariable=self.cell68, bg="light grey",
                                  validate='all', validatecommand=(validate_cmd, '%P'))
        self.cell68_entry.grid(row=6, column=8)

        # eighth row
        self.cell70 = StringVar()
        self.cell70_entry = Entry(self.root, width=cell_size, font=font, justify=CENTER,
                                  borderwidth=0, highlightthickness=1, highlightbackground="black",
                                  textvariable=self.cell70, bg="white",
                                  validate='all', validatecommand=(validate_cmd, '%P'))
        self.cell70_entry.grid(row=7, column=0)

        self.cell71 = StringVar()
        self.cell71_entry = Entry(self.root, width=cell_size, font=font, justify=CENTER,
                                  borderwidth=0, highlightthickness=1, highlightbackground="black",
                                  textvariable=self.cell71, bg="white",
                                  validate='all', validatecommand=(validate_cmd, '%P'))
        self.cell71_entry.grid(row=7, column=1)

        self.cell72 = StringVar()
        self.cell72_entry = Entry(self.root, width=cell_size, font=font, justify=CENTER,
                                  borderwidth=0, highlightthickness=1, highlightbackground="black",
                                  textvariable=self.cell72, bg="white",
                                  validate='all', validatecommand=(validate_cmd, '%P'))
        self.cell72_entry.grid(row=7, column=2, padx=(0, padding))

        self.cell73 = StringVar()
        self.cell73_entry = Entry(self.root, width=cell_size, font=font, justify=CENTER,
                                  borderwidth=0, highlightthickness=1, highlightbackground="black",
                                  textvariable=self.cell73, bg="light grey",
                                  validate='all', validatecommand=(validate_cmd, '%P'))
        self.cell73_entry.grid(row=7, column=3)

        self.cell74 = StringVar()
        self.cell74_entry = Entry(self.root, width=cell_size, font=font, justify=CENTER,
                                  borderwidth=0, highlightthickness=1, highlightbackground="black",
                                  textvariable=self.cell74, bg="light grey",
                                  validate='all', validatecommand=(validate_cmd, '%P'))
        self.cell74_entry.grid(row=7, column=4)

        self.cell75 = StringVar()
        self.cell75_entry = Entry(self.root, width=cell_size, font=font, justify=CENTER,
                                  borderwidth=0, highlightthickness=1, highlightbackground="black",
                                  textvariable=self.cell75, bg="light grey",
                                  validate='all', validatecommand=(validate_cmd, '%P'))
        self.cell75_entry.grid(row=7, column=5, padx=(0, padding))

        self.cell76 = StringVar()
        self.cell76_entry = Entry(self.root, width=cell_size, font=font, justify=CENTER,
                                  borderwidth=0, highlightthickness=1, highlightbackground="black",
                                  textvariable=self.cell76, bg="white",
                                  validate='all', validatecommand=(validate_cmd, '%P'))
        self.cell76_entry.grid(row=7, column=6)

        self.cell77 = StringVar()
        self.cell77_entry = Entry(self.root, width=cell_size, font=font, justify=CENTER,
                                  borderwidth=0, highlightthickness=1, highlightbackground="black",
                                  textvariable=self.cell77, bg="white",
                                  validate='all', validatecommand=(validate_cmd, '%P'))
        self.cell77_entry.grid(row=7, column=7)

        self.cell78 = StringVar()
        self.cell78_entry = Entry(self.root, width=cell_size, font=font, justify=CENTER,
                                  borderwidth=0, highlightthickness=1, highlightbackground="black",
                                  textvariable=self.cell78, bg="white",
                                  validate='all', validatecommand=(validate_cmd, '%P'))
        self.cell78_entry.grid(row=7, column=8)

        # ninth row
        self.cell80 = StringVar()
        self.cell80_entry = Entry(self.root, width=cell_size, font=font, justify=CENTER,
                                  borderwidth=0, highlightthickness=1, highlightbackground="black",
                                  textvariable=self.cell80, bg="light grey",
                                  validate='all', validatecommand=(validate_cmd, '%P'))
        self.cell80_entry.grid(row=8, column=0)

        self.cell81 = StringVar()
        self.cell81_entry = Entry(self.root, width=cell_size, font=font, justify=CENTER,
                                  borderwidth=0, highlightthickness=1, highlightbackground="black",
                                  textvariable=self.cell81, bg="light grey",
                                  validate='all', validatecommand=(validate_cmd, '%P'))
        self.cell81_entry.grid(row=8, column=1)

        self.cell82 = StringVar()
        self.cell82_entry = Entry(self.root, width=cell_size, font=font, justify=CENTER,
                                  borderwidth=0, highlightthickness=1, highlightbackground="black",
                                  textvariable=self.cell82, bg="light grey",
                                  validate='all', validatecommand=(validate_cmd, '%P'))
        self.cell82_entry.grid(row=8, column=2, padx=(0, padding))

        self.cell83 = StringVar()
        self.cell83_entry = Entry(self.root, width=cell_size, font=font, justify=CENTER,
                                  borderwidth=0, highlightthickness=1, highlightbackground="black",
                                  textvariable=self.cell83, bg="white",
                                  validate='all', validatecommand=(validate_cmd, '%P'))
        self.cell83_entry.grid(row=8, column=3)

        self.cell84 = StringVar()
        self.cell84_entry = Entry(self.root, width=cell_size, font=font, justify=CENTER,
                                  borderwidth=0, highlightthickness=1, highlightbackground="black",
                                  textvariable=self.cell84, bg="white",
                                  validate='all', validatecommand=(validate_cmd, '%P'))
        self.cell84_entry.grid(row=8, column=4)

        self.cell85 = StringVar()
        self.cell85_entry = Entry(self.root, width=cell_size, font=font, justify=CENTER,
                                  borderwidth=0, highlightthickness=1, highlightbackground="black",
                                  textvariable=self.cell85, bg="white",
                                  validate='all', validatecommand=(validate_cmd, '%P'))
        self.cell85_entry.grid(row=8, column=5, padx=(0, padding))

        self.cell86 = StringVar()
        self.cell86_entry = Entry(self.root, width=cell_size, font=font, justify=CENTER,
                                  borderwidth=0, highlightthickness=1, highlightbackground="black",
                                  textvariable=self.cell86, bg="light grey",
                                  validate='all', validatecommand=(validate_cmd, '%P'))
        self.cell86_entry.grid(row=8, column=6)

        self.cell87 = StringVar()
        self.cell87_entry = Entry(self.root, width=cell_size, font=font, justify=CENTER,
                                  borderwidth=0, highlightthickness=1, highlightbackground="black",
                                  textvariable=self.cell87, bg="light grey",
                                  validate='all', validatecommand=(validate_cmd, '%P'))
        self.cell87_entry.grid(row=8, column=7)

        self.cell88 = StringVar()
        self.cell88_entry = Entry(self.root, width=cell_size, font=font, justify=CENTER,
                                  borderwidth=0, highlightthickness=1, highlightbackground="black",
                                  textvariable=self.cell88, bg="light grey",
                                  validate='all', validatecommand=(validate_cmd, '%P'))
        self.cell88_entry.grid(row=8, column=8)

        self.solve_with_animation_button = Button(self.root, text="solve with\nanimation", command=self.solve_with_animation)
        self.solve_with_animation_button.grid(row=9, column=3, columnspan=3, pady=5)

        self.solve_without_animation_button = Button(self.root, text="solve without\nanimation",
                                                  command=self.solve_without_animation)
        self.solve_without_animation_button.grid(row=9, column=0, columnspan=3, pady=5)

        self.reset_button = Button(self.root, text="reset",
                                                  command=self.reset)
        self.reset_button.grid(row=9, column=6, columnspan=3, pady=5)


        self.message_label_stringvar = StringVar()
        self.message_label = Label(self.root, textvariable=self.message_label_stringvar, justify=CENTER)
        self.message_label.grid(row=10, column=0, columnspan=9)


        # define a list that is built like the Sudoku.lines, each element is a string var
        self.cells = [
            [self.cell00, self.cell01, self.cell02, self.cell03, self.cell04, self.cell05, self.cell06, self.cell07, self.cell08],
            [self.cell10, self.cell11, self.cell12, self.cell13, self.cell14, self.cell15, self.cell16, self.cell17, self.cell18],
            [self.cell20, self.cell21, self.cell22, self.cell23, self.cell24, self.cell25, self.cell26, self.cell27, self.cell28],
            [self.cell30, self.cell31, self.cell32, self.cell33, self.cell34, self.cell35, self.cell36, self.cell37, self.cell38],
            [self.cell40, self.cell41, self.cell42, self.cell43, self.cell44, self.cell45, self.cell46, self.cell47, self.cell48],
            [self.cell50, self.cell51, self.cell52, self.cell53, self.cell54, self.cell55, self.cell56, self.cell57, self.cell58],
            [self.cell60, self.cell61, self.cell62, self.cell63, self.cell64, self.cell65, self.cell66, self.cell67, self.cell68],
            [self.cell70, self.cell71, self.cell72, self.cell73, self.cell74, self.cell75, self.cell76, self.cell77, self.cell78],
            [self.cell80, self.cell81, self.cell82, self.cell83, self.cell84, self.cell85, self.cell86, self.cell87, self.cell88]
                      ]

        self.root.title("Sudoku Solver")
        # run the app
        self.root.mainloop()

    def allow_only_one_digit(self, P):
        if len(P) > 1:  # allow only one character
            return False
        if str.isdigit(P) and int(P) == 0:  # don't allow zero
            return False
        if str.isdigit(P) or P == "":  # make sure it is a digit
            return True
        else:
            return False

    def solve_with_animation(self):
        self.message_label_stringvar.set("")  # so if the user presses solve_with_animation and there is an error message so it will delete it
        self.sudoku = self.extract_sudoku_out_of_gui()

        # Checking the sudoku is valid
        try:
            self.sudoku = Sudoku.Sudoku(self.sudoku)
        except ValueError as e:
            self.message_label_stringvar.set(str(e) + "\nFix this and then try again.")
            return

        self.sudoku.solve()
        self.animate_solving(sudoku_history=self.sudoku.lines_history, counter=1, prev_i=0, prev_j=-1)

    def animate_solving(self, sudoku_history, counter, prev_i, prev_j):
        """Animate the solving, showing how the back tracking works"""

        # stop condition
        try:
            sudoku = sudoku_history[counter]
        except IndexError:
            self.message_label_stringvar.set("Solved!")
            self.callId = None
            return # stop animation

        j = prev_j + 1
        i = prev_i
        if j > 8:
            i += 1
            j = 0
        if i > 8:
            counter += 1
            i = 0
            j = -1

        digit = sudoku[i][j]

        if digit == 0:
            digit = ""
            sleep_time = 1
        else:
            digit = str(digit)
            sleep_time = 20
        if self.cells[i][j]:
            sleep_time = 1
        self.cells[i][j].set(digit)

        prev_i, prev_j = i, j
        self.callId = self.root.after(sleep_time, self.animate_solving, sudoku_history, counter, prev_i, prev_j)

    def solve_without_animation(self):
        self.message_label_stringvar.set("")  # so if the user presses solve_without_animation and there is an error message so it will delete it
        self.sudoku = self.extract_sudoku_out_of_gui()

        # Checking the sudoku is valid
        try:
            self.sudoku = Sudoku.Sudoku(self.sudoku)
        except ValueError as e:
            self.message_label_stringvar.set(str(e) + "\nFix this and then try again.")
            return

        self.sudoku.solve()  # solve the sudoku using the Sudoku class
        # fill all the cells with the proper values
        for i in range(9):
            for j in range(9):
                self.cells[i][j].set(self.sudoku.lines[i][j])

        self.message_label_stringvar.set("Solved!")
        self.callId = None

    def reset(self):
        self.message_label_stringvar.set("")
        # if solve with animation is going on then stop it
        if self.callId is not None:
            self.root.after_cancel(self.callId)

            # set the board to the initial user input
            sudoku = self.sudoku.lines_history[0]
            for i in range(9):
                for j in range(9):
                    digit = sudoku[i][j]
                    digit = '' if digit == 0 else str(digit)
                    self.cells[i][j].set(digit)

        else:
            # reset all the cells
            for i in range(9):
                for j in range(9):
                    self.cells[i][j].set("")

        self.callId = None

    def extract_sudoku_out_of_gui(self):
        sudoku = []
        for i in range(9):
            line = []
            for j in range(9):
                curr_cell = self.cells[i][j]
                digit = curr_cell.get()
                if digit == "":
                    digit = 0
                else:
                    digit = int(digit)

                line.append(digit)
            sudoku.append(line)
        return sudoku


if __name__ == '__main__':
    SudokuGui()