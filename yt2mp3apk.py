"""The Yt MP 3 App"""

import flet
from pytube import YouTube
import os



def main(ft:flet.page):
    ft.title = "Yt2Mp3"
    ft.theme_mode = "light"
    ft.window_height = 200
    ft.window_width = 400
    # ft.window_frameless = True
    ft.window_title_bar_hidden = True
    ft.window_title_bar_buttons_hidden = True
    

    def txt_changed(e):
        link_val = e.control.value
        if link_val != None:
            t.value = "Download " + link_val + "?"
            t.color = "yellow"
        else:
            t.value = "Please enter something"
        
        ft.update()

        

    def on_c(e):
        try:
            link = YouTube(t.value)

            vid = link.streams.filter(only_audio = True).first()
            out = vid.download(output_path = os.getcwd())

            base,ext = os.path.splitext(out)
            nf = base+".mp3"
            t.value = "Downloaded succesfully" 
            t.color = "green"
            tb.value = ""
        except:
            t.color = "red"
            t.value = "That doesn\'t seem  to be a link"         


        ft.update()

    def themeChange(e):
        if ft.theme_mode == "light":
            ft.theme_mode = "dark"
        else:
            ft.theme_mode="light"
        
        ft.update()

    

    
    t = flet.Text()
    
    close = flet.IconButton(flet.icons.CLOSE, on_click= lambda _: ft.window_close())
    change_theme = flet.IconButton(flet.icons.WB_SUNNY_OUTLINED,on_click= themeChange)
    
    tb = flet.TextField(
        label = "Enter a link: ",
        on_change=txt_changed,
        
    )
    b1 =flet.FilledTonalButton(text="Download yt video !",
                            on_click=on_c)
    
    row = flet.Row(
        controls=[b1,close,change_theme],alignment=flet.MainAxisAlignment.SPACE_EVENLY
    )

    ft.add(tb,t,row)



flet.app(target=main)
