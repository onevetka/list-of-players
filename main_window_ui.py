from logic import *
from tkinter import *
from tkinter import ttk


class Question:
    central_frame: Frame
    PLAYER_LIST_FILE = 'data/CossacksPlayers.json'
    SETTINGS_FILE = 'data/Settings.txt'

    def __init__(self, main):
        init_list(self.PLAYER_LIST_FILE)
        self.is_take = BooleanVar()

        tab_control = ttk.Notebook(main)

        tab1 = ttk.Frame(tab_control)
        tab2 = ttk.Frame(tab_control)
        tab3 = ttk.Frame(tab_control)

        tab_control.add(tab1, text='Players')
        tab_control.add(tab2, text='List')
        tab_control.add(tab3, text='Rules')

        # TTK Style of widgets -->

        # Tab 1 -->

        self.stat_lbl_style = ttk.Style()
        self.stat_lbl_style.configure("SL.Label",
                                      justify=CENTER)

        self.signature_style = ttk.Style()
        self.signature_style.configure("SS.Label")

        self.terminal_style = ttk.Style()
        self.terminal_style.configure("TS.Label",
                                      foreground="black")

        self.settings_result_style = ttk.Style()
        self.settings_result_style.configure("SR.Label",
                                             foreground='#535353')

        # TTK init widgets -->

        # Tab 1 -->

        self.central_frame = ttk.Frame(tab1)

        self.bg_image = PhotoImage(file='images/LogoLOP.png')

        self.bg = Label(self.central_frame, image=self.bg_image)

        self.stat_lbl = ttk.Label(self.central_frame,
                                  text=get_statistics(),
                                  style="SL.Label")

        self.nick_lbl = ttk.Label(self.central_frame,
                                  text="Nickname:",
                                  style="SS.Label")

        self.profile_lbl = ttk.Label(self.central_frame,
                                     text="Info",
                                     style="SS.Label")

        self.nick_ent = ttk.Entry(self.central_frame,
                                  width=26)

        self.profile_ent = ttk.Entry(self.central_frame,
                                     width=26)

        self.take_chb = ttk.Checkbutton(self.central_frame,
                                        variable=self.is_take,
                                        text="Take?")

        self.label1 = ttk.Label(self.central_frame,
                                style="TS.Label",
                                wraplength=300)

        self.check_btn = ttk.Button(self.central_frame,
                                    text='Check')

        self.add_btn = ttk.Button(self.central_frame,
                                  text='Add')

        # Tab 2 -->

        self.list_of_players = Text(tab2,
                                    width=53)

        # Tab 3 -->

        self.settings_frm = ttk.LabelFrame(tab3, text="Settings")
        self.options_frm = ttk.LabelFrame(tab3, text="Additional options")

        # Init recent settings

        try:
            settings_file = open(self.SETTINGS_FILE, 'r')
        except FileNotFoundError:
            print("file '" + self.SETTINGS_FILE + "' not found")
            raise SystemExit(1)

        settings = settings_file.readline()
        settings_file.close()
        settings = [int(i) for i in settings.split()]

        if len(settings) != 9:
            print('Incorrect settings. There should be eight indicators. The program overwritten the values')
            settings = [0] * 9

        # Correlation of forces:

        self.corr_of_forces_lbl = ttk.Label(self.settings_frm,
                                            style="SL.Label",
                                            text='Correlation of forces:')

        self.corr_of_forces_cmb = ttk.Combobox(self.settings_frm)

        self.corr_of_forces_cmb['values'] = ('1x1',
                                             '2x2',
                                             '2x2x2',
                                             '2x2x2x2',
                                             '3x3',
                                             '4x4',
                                             'ffa')

        self.corr_of_forces_cmb.current(settings[0])

        # Starting resourses:

        self.starting_resourses_lbl = ttk.Label(self.settings_frm,
                                                style="SL.Label",
                                                text='Starting resourses:')

        self.starting_resourses_cmb = ttk.Combobox(self.settings_frm)

        self.starting_resourses_cmb['values'] = ('1K',
                                                 '4K',
                                                 '5K',
                                                 '1M',
                                                 'random')

        self.starting_resourses_cmb.current(settings[1])

        # Peace time:

        self.peace_time_lbl = ttk.Label(self.settings_frm,
                                        style="SL.Label",
                                        text='Peace time:')

        self.peace_time_cmb = ttk.Combobox(self.settings_frm)

        self.peace_time_cmb['values'] = ('noPT',
                                         '10m',
                                         '15m',
                                         '20m',
                                         '30m',
                                         '45m',
                                         '60m',
                                         '1.5h',
                                         '2h',
                                         '3h',
                                         '4h')

        self.peace_time_cmb.current(settings[2])

        # Map size:

        self.map_size_lbl = ttk.Label(self.settings_frm,
                                      style="SL.Label",
                                      text='Map size:')

        self.map_size_cmb = ttk.Combobox(self.settings_frm)

        self.map_size_cmb['values'] = ('tiny',
                                       'normal',
                                       'large2x',
                                       'huge4x')

        self.map_size_cmb.current(settings[3])

        # Start options:

        self.start_options_lbl = ttk.Label(self.options_frm,
                                           style="SL.Label",
                                           text='Start options:')

        self.start_options_cmb = ttk.Combobox(self.options_frm)

        self.start_options_cmb['values'] = ('default',
                                            'army',
                                            'bigArmy',
                                            'hugeArmy',
                                            'armyOfPeasants',
                                            'differentNations',
                                            'towers',
                                            'cannons',
                                            'cannonsAndHowitzers',
                                            '18thCenturyBarracks',
                                            '17thCenturyBarracks',
                                            'village',
                                            'logCabins',
                                            'union')

        self.start_options_cmb.current(settings[4])

        # Capture

        self.capture_options_lbl = ttk.Label(self.options_frm,
                                             style="SL.Label",
                                             text='Capture:')

        self.capture_options_cmb = ttk.Combobox(self.options_frm)

        self.capture_options_cmb['values'] = ('default',
                                              'noCapPsnts',
                                              'noCapPsnts&Cntrs',
                                              'artOnly')

        self.capture_options_cmb.current(settings[5])

        # Dc and market

        self.dc_and_market_lbl = ttk.Label(self.options_frm,
                                           style="SL.Label",
                                           text='D. center and market:')

        self.dc_and_market_cmb = ttk.Combobox(self.options_frm)

        self.dc_and_market_cmb['values'] = ('default',
                                            'noDc',
                                            'noMarket',
                                            'NoDc&Market',
                                            'expensive',
                                            'marcenaries')

        self.dc_and_market_cmb.current(settings[6])

        # Game speed:

        self.game_speed_lbl = ttk.Label(self.options_frm,
                                        style="SL.Label",
                                        text='Game speed:')

        self.game_speed_cmb = ttk.Combobox(self.options_frm)

        self.game_speed_cmb['values'] = ('normal',
                                         'fast',
                                         'very',
                                         'fast',
                                         'adjustable')

        self.game_speed_cmb.current(settings[7])

        # Barrier

        self.barrier_lbl = ttk.Label(self.options_frm,
                                     style="SL.Label",
                                     text='Barrier:')

        self.barrier_cmb = ttk.Combobox(self.options_frm)

        self.barrier_cmb['values'] = ('+0',
                                      '+10',
                                      '+50',
                                      '+100',
                                      '+200',
                                      '+500',
                                      '+1000')

        self.barrier_cmb.current(settings[8])

        tab_control.pack(expand=1)

        # Copy to buffer button

        self.copy_btn = ttk.Button(tab3,
                                   text='Copy')

        self.settings_result_lbl = ttk.Label(tab3,
                                             text='',
                                             style="SR.Label")

        # Tab 1 -->

        self.show_menu(tab1)

        # Tab 3 -->

        self.settings_frm.grid(padx=10,
                               pady=10,
                               sticky=W)

        self.corr_of_forces_lbl.grid(row=0,
                                     column=0,
                                     padx=5,
                                     pady=5,
                                     sticky=E)

        self.corr_of_forces_cmb.grid(row=0,
                                     column=1,
                                     padx=5,
                                     pady=5,
                                     sticky=E)

        self.starting_resourses_lbl.grid(row=1,
                                         column=0,
                                         padx=5,
                                         pady=5,
                                         sticky=E)

        self.starting_resourses_cmb.grid(row=1,
                                         column=1,
                                         padx=5,
                                         pady=5,
                                         sticky=E)

        self.peace_time_lbl.grid(row=2,
                                 column=0,
                                 padx=5,
                                 pady=5,
                                 sticky=E)

        self.peace_time_cmb.grid(row=2,
                                 column=1,
                                 padx=5,
                                 pady=5,
                                 sticky=E)

        # Map size:

        self.map_size_lbl.grid(row=3,
                               column=0,
                               padx=5,
                               pady=5,
                               sticky=E)

        self.map_size_cmb.grid(row=3,
                               column=1,
                               padx=5,
                               pady=5,
                               sticky=E)

        self.options_frm.grid(padx=10,
                              pady=10,
                              sticky=W)

        # Start options:

        self.start_options_lbl.grid(row=0,
                                    column=0,
                                    padx=5,
                                    pady=5,
                                    sticky=E)

        self.start_options_cmb.grid(row=0,
                                    column=1,
                                    padx=5,
                                    pady=5,
                                    sticky=E)

        # Capture options:

        self.capture_options_lbl.grid(row=1,
                                      column=0,
                                      padx=5,
                                      pady=5,
                                      sticky=E)

        self.capture_options_cmb.grid(row=1,
                                      column=1,
                                      padx=5,
                                      pady=5,
                                      sticky=E)

        # Capture options:

        self.dc_and_market_lbl.grid(row=2,
                                    column=0,
                                    padx=5,
                                    pady=5,
                                    sticky=E)

        self.dc_and_market_cmb.grid(row=2,
                                    column=1,
                                    padx=5,
                                    pady=5,
                                    sticky=E)

        # Game speed:

        self.game_speed_lbl.grid(row=3,
                                 column=0,
                                 padx=5,
                                 pady=5,
                                 sticky=E)

        self.game_speed_cmb.grid(row=3,
                                 column=1,
                                 padx=5,
                                 pady=5,
                                 sticky=E)

        # Barrier

        self.barrier_lbl.grid(row=3,
                              column=0,
                              padx=5,
                              pady=5,
                              sticky=E)

        self.barrier_cmb.grid(row=3,
                              column=1,
                              padx=5,
                              pady=5,
                              sticky=E)

        # Copy to buffer button

        self.copy_btn.grid(row=3,
                           column=0,
                           sticky=W,
                           padx=5,
                           pady=5)

        self.settings_result_lbl.grid(row=2,
                                      column=0,
                                      padx=5,
                                      pady=5)

        # Bindings of the widgets -->

        # Tab 1 bindings -->

        self.check_btn.bind('<Button-1>', self.answer)
        self.add_btn.bind('<Button-1>', self.adding)

        # Tab 2 bindings -->

        self.copy_btn.bind('<Button-1>', self.copy_settings_to_buff)

    # Tab 1 functions -->

    def show_menu(self, event):
        self.central_frame.place(relx=.5, rely=.5, anchor="c", bordermode=OUTSIDE)

        self.stat_lbl.configure(text=get_statistics())
        self.label1.configure(text='')
        self.terminal_style.configure("TS.Label",
                                      foreground="black")

        self.bg.grid(row=0,
                     columnspan=4,
                     padx=5)

        self.stat_lbl.grid(row=1,
                           columnspan=4,
                           padx=5,
                           pady=5)

        self.nick_lbl.grid(row=2,
                           column=0,
                           padx=5,
                           pady=(5, 0),
                           sticky=E)

        self.nick_ent.grid(row=2,
                           column=1,
                           columnspan=2,
                           padx=5,
                           pady=(5, 0))

        self.profile_lbl.grid(row=3,
                              column=0,
                              padx=5,
                              pady=(0, 5),
                              sticky=E)

        self.profile_ent.grid(row=3,
                              column=1,
                              columnspan=2,
                              padx=5,
                              pady=(0, 5))

        self.take_chb.grid(row=2,
                           column=3,
                           padx=5,
                           pady=5)

        self.label1.grid(row=4,
                         columnspan=4,
                         padx=5,
                         pady=5,
                         rowspan=2)

        self.check_btn.grid(row=6,
                            column=1,
                            padx=5,
                            pady=5,
                            sticky=E)

        self.add_btn.grid(row=6,
                          column=2,
                          padx=5,
                          pady=5,
                          sticky=W)

        self.list_of_players.insert(END,
                                    get_list())

        self.list_of_players.grid(row=2,
                                  columnspan=3)

    def reset_gui(self):
        self.label1.configure(text='')
        self.terminal_style.configure("TS.Label",
                                      foreground="black")
        self.check_btn.configure(state='normal')
        self.add_btn.configure(state='normal')
        self.profile_ent.delete(0, 'end')
        self.stat_lbl.configure(text=get_statistics())

    def answer(self, event):
        self.reset_gui()
        profile = str(self.nick_ent.get())
        if profile == '':
            self.label1.configure(text="You have not entered a name")
            self.terminal_style.configure("TS.Label",
                                          foreground="red")
            return False
        self.label1.configure(text=find_player(profile))

    def adding(self, event):

        name = str(self.nick_ent.get())
        description = str(self.profile_ent.get())

        if name == '':
            self.label1.configure(text="You have not entered a name")
            self.terminal_style.configure("TS.Label",
                                          foreground="red")
            return False
        if description == '':
            self.label1.configure(text="You have not entered a description")
            self.terminal_style.configure("TS.Label",
                                          foreground="red")
            return False

        if self.is_take.get():
            if not add_player(name, 'Yes', description):
                increase_stat(True)
        else:
            if not add_player(name, 'No', description):
                increase_stat(False)

        sort_players()
        save_changes(self.PLAYER_LIST_FILE)
        self.reset_gui()
        self.label1.configure(text="Information successfully updated")
        self.terminal_style.configure("TS.Label",
                                      foreground="green")

    # Tab 2 functions -->

    def copy_settings_to_buff(self, event):
        settings = ''
        settings += str(self.corr_of_forces_cmb.get()) + ' ' + \
                    str(self.starting_resourses_cmb.get()) + ' ' + \
                    str(self.peace_time_cmb.get()) + ' ' + \
                    str(self.map_size_cmb.get()) + ' '
        if self.start_options_cmb.current() != 0:
            settings += str(self.start_options_cmb.get()) + ' '
        if self.capture_options_cmb.current() != 0:
            settings += str(self.capture_options_cmb.get()) + ' '
        if self.dc_and_market_cmb.current() != 0:
            settings += str(self.dc_and_market_cmb.get()) + ' '
        settings += str(self.game_speed_cmb.get()) + ' '
        settings += str(self.barrier_cmb.get())

        save_config = str(self.corr_of_forces_cmb.current()) + ' ' + \
                      str(self.starting_resourses_cmb.current()) + ' ' +\
                      str(self.peace_time_cmb.current()) + ' ' +\
                      str(self.map_size_cmb.current()) + ' ' +\
                      str(self.start_options_cmb.current()) + ' ' +\
                      str(self.capture_options_cmb.current()) + ' ' +\
                      str(self.dc_and_market_cmb.current()) + ' ' +\
                      str(self.game_speed_cmb.current()) + ' ' +\
                      str(self.barrier_cmb.current())

        settings_file = open(self.SETTINGS_FILE, 'w')
        settings_file.write(save_config)
        settings_file.close()

        self.settings_result_lbl.configure(text=settings)
        add_to_clipboard(settings)
