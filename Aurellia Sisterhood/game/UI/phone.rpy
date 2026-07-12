screen phone_interface():
    modal True                    # Makes phone take full focus
    zorder 300
    
    # Phone background/frame (add your image here)
    add "gui/phone_frame.png" xalign 0.5 yalign 0.5 zoom 0.85
    
    # Close button (top right)
    textbutton "✕":
        xalign 0.78
        yalign 0.18
        text_size 45
        text_color "#ffffff"
        action Hide("phone_interface")
    
    # Phone content area
    frame:
        xalign 0.5
        yalign 0.5
        xsize 380
        ysize 620
        background "#1a1a1a"
        
        text "Phone Screen" xalign 0.5 yalign 0.4 size 40 color "#ffffff"

# Optional: Label version (if you prefer using labels)
label open_phone:
    call screen phone_interface
    return