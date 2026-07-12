screen floating_phone_button():
    if not renpy.get_screen("say"):
        zorder 200
        
        imagebutton:
            xalign 0.95
            yalign 0.92
            idle "gui/phone_icon.png"
            hover "gui/phone_icon_hover.png"
            focus_mask True
            action Show("phone_home")   # Better than Jump for screens
            
            at transform:
                zoom 0.75
                on hover:
                    zoom 0.85
                    ease 0.15 zoom 0.9
                on idle:
                    ease 0.2 zoom 0.75